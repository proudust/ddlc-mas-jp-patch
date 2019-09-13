define config.default_language = "Japanese"

# フォント設定
translate Japanese python:
    gui.default_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.name_font = gui.default_font
    gui.interface_font = gui.default_font
    gui.choice_button_borders = Borders(10, 5, 10, 5)

translate Japanese style normal:
    outlines [(2, "#444", 0, 0), (1, "#444", 2, 2)]

translate Japanese style check_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style check_dark_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style choice_button_text:
    font gui.default_font

translate Japanese style choice_dark_button_text:
    font gui.default_font

translate Japanese style gui_label_text:
    font gui.default_font

translate Japanese style edited:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style edited_def:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style edited_dark:
    font "gui/font/VL-Gothic-Regular.ttf"

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
    font "gui/font/Mikachan.ttf"

translate Japanese style poemgame_text_def:
    font "gui/font/Mikachan.ttf"

translate Japanese style poemgame_text_dark:
    font "gui/font/Mikachan.ttf"

translate Japanese style pref_label_text:
    font gui.default_font

translate Japanese style radio_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style radio_dark_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style radio_dark_button_text:
    font "gui/font/Mikachan.ttf"

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
