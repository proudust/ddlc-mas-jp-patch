translate Japanese style edited:
    font jpfonts.VLGothic

translate Japanese style edited_dark:
    font jpfonts.VLGothic

translate Japanese style normal:
    outlines [(2, "#444", 0, 0), (1, "#444", 2, 2)]

translate Japanese style poemgame_text:
    font jpfonts.Mikachan

translate Japanese style poemgame_text_dark:
    font jpfonts.Mikachan

translate Japanese style navigation_button_text:
    font jpfonts.VLGothic

translate Japanese style navigation_button_text_dark:
    font jpfonts.VLGothic

translate Japanese style game_menu_label_text:
    font gui.default_font

translate Japanese style game_menu_label_text_dark:
    font gui.default_font

translate Japanese style pref_label_text:
    font gui.default_font

translate Japanese style pref_label_text_dark:
    font gui.default_font

translate Japanese style radio_button_text:
    font jpfonts.Mikachan

translate Japanese style radio_button_text_dark:
    font jpfonts.Mikachan

translate Japanese style check_button_text:
    font jpfonts.Mikachan

translate Japanese style check_button_text_dark:
    font jpfonts.Mikachan

translate Japanese style outfit_check_button_text:
    font jpfonts.Mikachan

translate Japanese style outfit_check_button_text_dark:
    font jpfonts.Mikachan

# 名前入力の制限撤廃
translate Japanese screen:
    screen name_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
        frame:
            has vbox:
                xalign .5
                yalign .5
                spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input default "" value VariableInputValue("player") length 12 pixel_width 168 exclude "{}"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action
