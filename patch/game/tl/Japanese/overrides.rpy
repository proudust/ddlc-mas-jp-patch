define config.default_language = "Japanese"

init -1 python in jpfonts:
    VLGothic = "gui/font/VL-Gothic-Regular.ttf"
    Mikachan = "gui/font/Mikachan.ttf"
    HolidayMDJP = "gui/font/HolidayMDJP.otf"
    TegakiZatsu = "gui/font/851tegaki_zatsu_normal.ttf"
    GataSosyo = "gui/font/gatasosyo.ttf"
    SanaFon = "gui/font/SNsanafonP.ttf"
    Ruriiro = "gui/font/Ruriiro_font.ttf"

# フォント設定
translate Japanese python:
    gui.default_font = jpfonts.VLGothic
    gui.name_font = gui.default_font
    gui.interface_font = gui.default_font
    gui.choice_button_borders = Borders(10, 5, 10, 5)

translate Japanese style normal:
    outlines [(2, "#444", 0, 0), (1, "#444", 2, 2)]

translate Japanese style check_button_text:
    font jpfonts.Mikachan

translate Japanese style check_dark_button_text:
    font jpfonts.Mikachan

translate Japanese style choice_button_text:
    font gui.default_font

translate Japanese style choice_dark_button_text:
    font gui.default_font

translate Japanese style gui_label_text:
    font gui.default_font

translate Japanese style edited:
    font gui.default_font

translate Japanese style edited_def:
    font gui.default_font

translate Japanese style edited_dark:
    font gui.default_font

translate Japanese style game_menu_label_text:
    font gui.name_font

translate Japanese style navigation_button_text:
    font gui.name_font

translate Japanese style navigation_dark_button_text:
    font gui.name_font

translate Japanese style navigation_button_text_def:
    font gui.name_font

translate Japanese style navigation_button_text_dark:
    font gui.name_font

translate Japanese style poemgame_text:
    font jpfonts.Mikachan

translate Japanese style poemgame_text_def:
    font jpfonts.Mikachan

translate Japanese style poemgame_text_dark:
    font jpfonts.Mikachan

translate Japanese style pref_label_text:
    font gui.default_font

translate Japanese style radio_button_text:
    font jpfonts.Mikachan

translate Japanese style radio_dark_button_text:
    font jpfonts.Mikachan

translate Japanese style radio_dark_button_text:
    font jpfonts.Mikachan

translate Japanese style scrollable_menu_button_text:
   font gui.default_font

translate Japanese style scrollable_menu_button_dark_text:
   font gui.default_font

translate Japanese style scrollable_menu_dark_button_text:
   font gui.default_font

translate Japanese style twopane_scrollable_menu_button_text:
   font gui.default_font

translate Japanese style twopane_scrollable_menu_dark_button_text:
   font gui.default_font

translate Japanese style hkb_button_text:
   font gui.default_font

translate Japanese style hkb_dark_button_text:
   font gui.default_font

translate Japanese style island_button_dark_text:
   font gui.default_font

translate Japanese style quick_dark_button_text:
   font gui.default_font

# 詩
translate Japanese style yuri_text:
    font jpfonts.TegakiZatsu
    size 28

translate Japanese style yuri_text_2:
    font jpfonts.GataSosyo
    size 36

translate Japanese style yuri_text_3:
    font jpfonts.GataSosyo
    size 27
    kerning -12
    language "western"

translate Japanese style natsuki_text:
    font jpfonts.SanaFon
    size 30

translate Japanese style sayori_text:
    font jpfonts.HolidayMDJP
    size 30

translate Japanese style monika_text:
    font jpfonts.Ruriiro
    size 30

translate Japanese python:
    # 接頭詞・接尾詞の設定
    m = DynamicCharacter('m_name', image='monika', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")

init python:
    # 日本語固定
    config.language = "Japanese"

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
            input default "" value VariableInputValue("player") length 12 pixel_width 168
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action
