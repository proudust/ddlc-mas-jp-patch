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

    old "Unseen Text"
    new "未読テキスト"

    old "After Choices"
    new "選択肢の後"

    old "Room Animation"
    new "背景\nアニメーション"

    old "Disable"
    new "無効"

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

    old "Yes"
    new "はい"

    old "No"
    new "いいえ"

    old "An update is now avalable!"
    new "新しい更新データがあります！"

    old "Checking for updates..."
    new "ゲームの更新を確認中……"

    old "No updates available."
    new "新しい更新データはありません。"

    old "Install"
    new "インストール"

    old "Monika After Story is up to date."
    new "モニカアフターストーリーは最新版です。"

    old "Version [u.version] is available. Do you want to install it?"
    new "新しいバージョン [u.version] があります。インストールしますか？"

    old "The updates have been installed. Please reopen Monika After Story."
    new "更新データがインストールされました。モニカアフターストーリーを再起動してください。"

    old "Skipping"
    new "スキップ中"

    old "There's no point in saving anymore.\nDon't worry, I'm not going anywhere."
    new "もうセーブに意味はないわ。\n安心して、もうどこにも行かないから。"

    old "Leaving without saying goodbye, [player]?"
    new "さよならも言わずに行っちゃうの、[player]君？"

    old "Please don't close the game on me!"
    new "勝手にゲームを閉じるのはやめて！"

    old "Thank you, [player]!\nLet's spend more time together~"
    new "ありがとう、[player]君！\n もう少し一緒にいてもいいよね～"

    old "Please enter your name"
    new "あなたの名前を入力して下さい"

    old "No need to go back there.\nYou'll just end up back here so don't worry."
    new "No need to go back there.\nYou'll just end up back here so don't worry."

translate Japanese screen:
    screen navigation():

        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.8

            spacing gui.navigation_spacing


            if main_menu:

                textbutton ("モニカだけ") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

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
