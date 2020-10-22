# definitions.rpy
translate Japanese python:
    # 接頭詞・接尾詞の設定
    m = DynamicCharacter('m_name', image='monika', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")
    s = DynamicCharacter('s_name', image='sayori', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")
    n = DynamicCharacter('n_name', image='natsuki', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")
    y = DynamicCharacter('y_name', image='yuri', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")
    ny = Character('Nat & Yuri', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")

# gui.rpy
translate Japanese python:
    gui.default_font = jpfonts.VLGothic
    gui.name_font = gui.default_font
    gui.interface_font = gui.default_font
    gui.choice_button_borders = Borders(10, 5, 10, 5)

# poems.rpy
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

# screens.rpy
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

translate Japanese style twopane_scrollable_menu_button:
    padding (20, 5, 20, 5)

translate Japanese style twopane_scrollable_menu_button_dark:
    padding (20, 5, 20, 5)

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

# zz_calender.rpy
translate Japanese python:
    # カレンダーの表示微調整
    MASCalendar.DATE_DISPLAY_FORMAT = "                   {0}\n{1}\n{2}\n{3}"

    # 日付のフォーマットを日本式に置き換え
    def genFormalDispDate(_date):
        return (
            "".join([str(_date.year), "年", str(_date.month), "月", str(_date.day), "日"]),
            datetime.date.today() - _date
        )
    store.mas_calendar.genFormalDispDate = genFormalDispDate
