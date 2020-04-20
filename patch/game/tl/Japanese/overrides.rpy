define config.default_language = "Japanese"

init -990 python in mas_submod_utils:
    name = "Japanese Language Submod"
    description = "This is a Submod that adds Japanese translation."
    version = "${PATCH_VERSION}"

    if "-" in version:
        name += " (Canary)"
        description += " This version is unstable. Use the latest stable version if possible."
        version_split = version.split('-')
        version_split[2] = str(int(version[-7:], 16))
        version = ".".join(version_split)
    elif "$" in version:
        name += " (In Develop)"
        description += " This version is unstable. Use the latest stable version if possible."
        version = "0"

    Submod(
        author = "DDLC translate club (JP)",
        name = name,
        description = "This is a Submod that adds Japanese translation.",
        version = version,
        dependencies={},
        settings_pane="japanese_submod_screen",
        version_updates={}
    )

screen japanese_submod_screen():
    pass

translate Japanese strings:
    old "by DDLC translate club (JP)"
    new "by DDLC翻訳部"

    old "Japanese Language Submod"
    new "日本語化パッチ"

    old "Japanese Language Submod (Canary)"
    new "日本語化パッチ (カナリア版)"

    old "Japanese Language Submod (In Develop)"
    new "日本語化パッチ (開発中版)"

    old "This is a Submod that adds Japanese translation."
    new "日本語訳を追加するSubmodです。"

    old "This is a Submod that adds Japanese translation. This version is unstable. Use the latest stable version if possible."
    new "日本語訳を追加するSubmodです。このバージョンは不安定です。可能であれば最新の安定バージョンを使用して下さい。"

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

translate Japanese style navigation_button_text:
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
    # カレンダーの表示微調整
    MASCalendar.DATE_DISPLAY_FORMAT = "                   {0}\n{1}\n{2}\n{3}"
    # 日付のフォーマットを日本式に置き換え
    def genFormalDispDate(_date):
        return (
            "".join([str(_date.year), "年", str(_date.month), "月", str(_date.day), "日"]),
            datetime.date.today() - _date
        )
    store.mas_calendar.genFormalDispDate = genFormalDispDate

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
            input default "" value VariableInputValue("player") length 12 pixel_width 168 exclude "{}"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action
