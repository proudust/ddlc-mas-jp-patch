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


def read_dialogue():
    with open('dialogue.tab', mode='r') as dialogue:
        lines = (l.split('\t') for l in dialogue)
        next(lines)
        return {id: attrs for id, attrs, *_ in lines}


def enumrable_tl_scripts():
    base = 'patch/game/tl/Japanese/'
    return [base + p for p in os.listdir(base) if os.path.splitext(p)[1] == '.rpy']


def read_tl_script(path):
    pattern = r'translate \w+ (?!.*strings)([^:]+):\s    ([^"]+?) "[^"]+"( nointeract)?'

    with open(path, mode='r') as file:
        content = file.read()
        result = list()
        for match in re.finditer(pattern, content, re.MULTILINE):
            id, attrs, nointeract = match.group(1, 2, 3)
            if nointeract is not None:
                attrs += nointeract
            line = content.count('\n', 0, match.end(0)) + 1
            result.append((id, attrs, path, line))
        return result


def check_translate(dialogues, translates):
    errors = list()
    for id, attrs, path, line in translates:
        find_attrs = dialogues.get(id)

        if find_attrs is None:
            errors.append(('ID not found', id))
            print(
                '::warning file=' + path + ',line=' + str(line) +
                '::ID not found (id: ' + id + ')'
            )

        elif find_attrs != attrs:
            errors.append(('Attrs unmatch', id, attrs))
            print(
                '::warning file=' + path + ',line=' + str(line) +
                '::Attrs unmatch (id: ' + id + ' attrs:' + find_attrs + ')'
            )
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
    dialogues = read_dialogue()

    # Extract translates
    translates = sum([read_tl_script(p) for p in enumrable_tl_scripts()], [])

    # Check ID and attrs
    errors = check_translate(dialogues, translates)
    if len(errors) > 0:
        with open('./error_report.tab', mode='w') as report:
            for error in errors:
                report.writelines('\t'.join(map(str, error)) + '\n')
        sys.exit(1)


if __name__ == '__main__':
    main()
