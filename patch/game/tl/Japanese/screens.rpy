define config.default_language = "Japanese"

init python:
    config.language = "Japanese"
    m = DynamicCharacter('m_name', image='monika', what_prefix='「', what_suffix='」', ctc="ctc", ctc_position="fixed")

translate Japanese python:
    gui.default_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.name_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.interface_font = "gui/font/VL-Gothic-Regular.ttf"
    gui.choice_button_borders = Borders(10, 5, 10, 5)

translate Japanese style _default:
    font "gui/font/MTLc3m.ttf"

translate Japanese style button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style check_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style choice_button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style edited:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style game_menu_label_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style navigation_button_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style poemgame_text:
    font "gui/font/Mikachan.ttf"

translate Japanese style pref_label_text:
    font "gui/font/VL-Gothic-Regular.ttf"

translate Japanese style radio_button_text:
    font "gui/font/Mikachan.ttf"

translate Japanese strings:
    old "History"
    new "ヒストリー"

    old "Skip"
    new "スキップ"

    old "Auto"
    new "オート"

    old "Save"
    new "セーブ"

    old "Load"
    new "ロード"

    old "Settings"
    new "オプション"

    old "Just Monika"
    new "モニカだけ"

    old "Save Game"
    new "セーブゲーム"

    old "Load Game"
    new "ロードゲーム"

    old "End Replay"
    new "リプレイ終了"

    old "Main Menu"
    new "メインメニュー"

    old "Help"
    new "ヘルプ"

    old "Quit"
    new "終了"

    old "Return"
    new "戻る"

    old "About"
    new "バージョン情報"

    old "Version [config.version!t]\n"
    new "Version [config.version!t]\n"

    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"

    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%Y年%m月%d日(%a) %H時%M分"

    old "empty slot"
    new "空のスロット"

    old "Display"
    new "ディスプレイ"

    old "Window"
    new "ウィンドウ"

    old "Fullscreen"
    new "フルスクリーン"

    old "Graphics"
    new "Graphics"

    old "Disable Animation"
    new "Disable Animation"

    old "Change Renderer"
    new "Change Renderer"

    old "Gameplay"
    new "Gameplay"

    old "Unstable"
    new "Unstable"

    old "Repeat Topics"
    new "Repeat Topics"

    old " "
    new " "

    old "Sensitive Mode"
    new "Sensitive Mode"

    old "Sunrise   "
    new "Sunrise   "

    old "Sunset   "
    new "Sunset   "

    old "Random Chatter   "
    new "Random Chatter   "

    old "Text Speed"
    new "文字表示速度"

    old "Auto-Forward Time"
    new "オート待ち時間"

    old "Music Volume"
    new "音楽の音量"

    old "Sound Volume"
    new "効果音の音量"

    old "Test"
    new "テスト"

    old "Voice Volume"
    new "ボイスの音量"

    old "Mute All"
    new "全てミュート"

    old "Update Version"
    new "アップデート"

    old "Import DDLC Save Data"
    new "DDLCセーブデータをインポートする"

    old "The dialogue history is empty."
    new "ヒストリーはありません。"

    old "OK"
    new "OK"

    old "QUIT"
    new "終了"

    old "-"
    new "-"

    old "Yes"
    new "はい"

    old "No"
    new "いいえ"

    old "An update is now avalable!"
    new "新しい更新データがあります！"

    old "Checking for updates..."
    new "ゲームの更新を確認中……"

    old "No update available."
    new "新しい更新データはありません。"

    old "Timeout occured while checking for updates. Try again later."
    new "更新の確認中にタイムアウトが発生しました。後でもう一度お試しください。"

    old "Install"
    new "インストール"

    old "Cancel"
    new "Cancel"

    old "Monika After Story is up to date."
    new "モニカアフターストーリーは最新版です。"

    old "Version [u.version] is available. Do you want to install it?"
    new "新しいバージョン [u.version] があります。インストールしますか？"

    old "Downloading the updates. (Progress bar may not advance during download)"
    new "Downloading the updates. (Progress bar may not advance during download)"

    old "The updates have been installed. Please reopen Monika After Story."
    new "更新データがインストールされました。モニカアフターストーリーを再起動してください。"

    old "The updates have been installed."
    new "The updates have been installed."

    old "Skipping"
    new "スキップ中"

    old "Introduction"
    new "Introduction"

    old "Route Part 1, How To Make A Mod"
    new "Route Part 1, How To Make A Mod"

    old "Route Part 2, Music"
    new "Route Part 2, Music"

    old "Route Part 3, Scene"
    new "Route Part 3, Scene"

    old "Route Part 4, Dialogue"
    new "Route Part 4, Dialogue"

    old "Route Part 5, Menu"
    new "Route Part 5, Menu"

    old "Route Part 6, Logic Statement"
    new "Route Part 6, Logic Statement"

    old "Route Part 7, Sprite"
    new "Route Part 7, Sprite"

    old "Route Part 8, Position"
    new "Route Part 8, Position"

    old "Route Part 9, Ending"
    new "Route Part 9, Ending"

    old "That's enough for now."
    new "That's enough for now."

    old "Go Back"
    new "Go Back"

    old "Please restart Monika After Story."
    new "Please restart Monika After Story."

translate Japanese screen:
   screen navigation():

       vbox:
           style_prefix "navigation"

           xpos gui.navigation_xpos
           yalign 0.8

           spacing gui.navigation_spacing

           if main_menu:

               textbutton ("Just Monika") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

           else:

               textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

               textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

           textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

           if _in_replay:

               textbutton _("End Replay") action EndReplay(confirm=True)

           elif not main_menu:
               textbutton _("Main Menu") action NullAction(), Show(screen="dialog", message="No need to go back there.\nYou'll just end up back here so don't worry.", ok_action=Hide("dialog"))

           textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

           #textbutton _("About") action ShowMenu("about")

           if renpy.variant("pc"):

               ## Help isn't necessary or relevant to mobile devices.
               textbutton _("Help") action Help("README.html")

               ## The quit button is banned on iOS and unnecessary on Android.
               textbutton _("Quit") action Quit(confirm=not main_menu)

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
