define config.default_language = "Japanese"
define config.language = "Japanese"

init -990 python hide:
    # ビルド時に git describe の文字列に置き換えられる
    version = "${PATCH_VERSION}"

    if version.isdecimal():
        # リリースビルド (例: 200413)
        name_suffix = ""
        is_unstable = False

    elif "-" in version:
        # カナリアビルド (例: 200413-3-g98d0e7f)
        name_suffix = " Canary Build"
        is_unstable = True

        # サブ MOD のバージョンは . 区切りの数値である必要がある
        # コミットハッシュを 10 進数に変換し、- を . に置き換えてそれっぽくする
        version_split = version.split('-')
        version_split[2] = str(int(version[-7:], 16))
        version = ".".join(version_split)

    else:
        # ビルドされていない
        name_suffix = " In Develop"
        is_unstable = True
        version = "0"

    jp_submod = store.mas_submod_utils.Submod(
        author = "DDLC translate club JP",
        name = "Japanese Language Submod" + name_suffix,
        description = (
            "This is a Submod that adds Japanese translation."
            + (" This version is unstable. Use the latest stable version if possible." if is_unstable else "")
        ),
        version = version,
        dependencies={},
        settings_pane="japanese_submod_screen",
        version_updates={}
    )

    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod=jp_submod,
            user_name="proudust",
            repository_name="ddlc-mas-jp-patch",
            update_dir="" # Updates will be installed in the base directory.
        )

screen japanese_submod_screen():
    pass

translate Japanese strings:
    old "by DDLC translate club JP"
    new "by DDLC翻訳部"

    old "Japanese Language Submod"
    new "日本語化パッチ"

    old "Japanese Language Submod Canary Build"
    new "日本語化パッチ カナリアビルド"

    old "Japanese Language Submod In Develop"
    new "日本語化パッチ 開発中"

    old "This is a Submod that adds Japanese translation."
    new "日本語訳を追加するSubmodです。"

    old "This is a Submod that adds Japanese translation. This version is unstable. Use the latest stable version if possible."
    new "日本語訳を追加するSubmodです。このバージョンは不安定です。可能であれば最新の安定バージョンを使用して下さい。"
