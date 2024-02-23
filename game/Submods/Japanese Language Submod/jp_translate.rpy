# https://github.com/proudust/ddlc-mas-jp-patch/issues/67
translate Japanese monika_haterReaction_91847127:
    if not persistent._mas_pm_cares_about_dokis:
        $ menuOption = renpy.substitute("You're not one of those haters, are you [player]?")
    m "[menuOption!t]{nw}"
