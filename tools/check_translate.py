import os
import re
import subprocess
import sys

def get_mas_version():
    with open('./patch/game/options.rpy', mode='r') as options:
        match = re.search(r'define config.version = "(.+)"', options.read())
        return 'v' + match.group(1) if match else None

def exec_extract_dialogues(mas_version):
    tools_path = os.path.dirname(os.path.abspath(__file__))
    shell_path = os.path.join(tools_path, 'dialogue.sh')
    return_code = subprocess.call([shell_path + ' ' + mas_version], shell=True)
    return True if return_code == 0 else False

def get_dialogues():
    result = {}
    with open('dialogue.tab', mode='r') as dialogue_tab:
        for line in dialogue_tab:
            id, attrs, *_ = line.split('\t')
            result[id] = attrs
    return result

def get_translate_scripts():
    base = './patch/game/tl/Japanese/'

    result = list()
    for path in os.listdir(base):
        _, ext = os.path.splitext(path)
        if ext == '.rpy': result.append(base + path)
    return result

def finditer_translate_dialogues(string):
    pattern = r'translate Japanese (.+_[\da-f]{8}):\s    ([^"]+?) "[^"]+"( nointeract)?'

    result = list()
    for match in re.finditer(pattern, string, re.MULTILINE):
        id, attrs, nointeract = match.group(1, 2, 3)
        if nointeract is not None: attrs += nointeract
        result.append((id, attrs))
    return result

def check_translate(dialogues, translates):
    errors = list()
    for id, attrs in translates:
        find_attrs = dialogues.get(id)

        if find_attrs is None:
            errors.append(('id not found', id))
            print('id not found: ' + id)

        elif find_attrs != attrs:
            errors.append(('attrs unmatch', id, attrs))
            print('attrs unmatch: ' + id + ' ' + attrs)
    return errors

def main():
    # Get MAS version
    mas_version = get_mas_version()
    if mas_version is None:
        print('failed to get MAS version.')
        sys.exit(1)

    # Extract Dialogue
    isExtractSuccess = exec_extract_dialogues(mas_version)
    if not isExtractSuccess:
        print('extract dialogue failed.')
        sys.exit(1)
    dialogues = get_dialogues()

    # Extract translates
    translates = list()
    for path in get_translate_scripts():
        with open(path, mode='r') as file:
            content = file.read()
            translates.extend(finditer_translate_dialogues(content))

    # Check ID and attrs
    errors = check_translate(dialogues, translates)
    if len(errors) > 0:
        with open('./error_report.tab', mode='w') as report:
            for error in errors:
                report.writelines('\t'.join(map(str, error)) + '\n')
        sys.exit(1)

if __name__ == '__main__':
    main()
