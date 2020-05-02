translate Japanese style normal:
    outlines [(2, "#444", 0, 0), (1, "#444", 2, 2)]

translate Japanese style button_text:
    font gui.interface_font

translate Japanese style button_text_dark:
    font gui.interface_font

translate Japanese style edited:
    font jpfonts.VLGothic

translate Japanese style poemgame_text_def:
    font jpfonts.Mikachan

translate Japanese style poemgame_text_dark:
    font jpfonts.Mikachan

translate Japanese style pref_def_label_text:
    font gui.name_font

translate Japanese style pref_dark_label_text:
    font gui.name_font

translate Japanese style game_menu_label:
    font gui.name_font

translate Japanese style game_menu_label_dark:
    font gui.name_font

translate Japanese style choice_button_text:
    font gui.default_font

translate Japanese style choice_dark_button_text:
    font gui.default_font

translate Japanese style check_button_text:
    font jpfonts.Mikachan

translate Japanese style check_dark_button_text:
    font jpfonts.Mikachan

translate Japanese style game_menu_label_text:
    font jpfonts.VLGothic

translate Japanese style game_menu_label_dark_text:
    font jpfonts.VLGothic

translate Japanese style hkb_button_text:
    font gui.default_font

translate Japanese style hkb_dark_button_text:
    font gui.default_font

translate Japanese style music_menu_button_text:
    font jpfonts.VLGothic

translate Japanese style music_menu_dark_button_text:
    font jpfonts.VLGothic

translate Japanese style navigation_dark_button_text:
    font jpfonts.VLGothic

translate Japanese style quick_button_text:
    font gui.default_font

translate Japanese style quick_dark_button_text:
    font gui.default_font

translate Japanese style radio_button_text:
    font jpfonts.Mikachan

translate Japanese style radio_dark_button_text:
    font jpfonts.Mikachan

translate Japanese style scrollable_menu_button_text:
    font gui.default_font

translate Japanese style scrollable_menu_dark_button_text:
    font gui.default_font

translate Japanese style twopane_scrollable_menu_button_text:
    font gui.default_font

translate Japanese style twopane_scrollable_menu_dark_button_text:
    font gui.default_font

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
