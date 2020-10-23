define config.default_language = "Japanese"
define config.language = "Japanese"

define -2 jpfonts.VLGothic = "mod_assets/font/VL-Gothic-Regular.ttf"
define -2 jpfonts.Mikachan = "mod_assets/font/Mikachan.ttf"
define -2 jpfonts.HolidayMDJP = "mod_assets/font/HolidayMDJP.otf"
define -2 jpfonts.TegakiZatsu = "mod_assets/font/851tegaki_zatsu_normal.ttf"
define -2 jpfonts.GataSosyo = "mod_assets/font/gatasosyo.ttf"
define -2 jpfonts.SanaFon = "mod_assets/font/SNsanafonP.ttf"
define -2 jpfonts.Ruriiro = "mod_assets/font/Ruriiro_font.ttf"

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
        version_updates={
            "ddlc_translate_club_jp_japanese_language_submod_v200413": "ddlc_translate_club_jp_japanese_language_submod_v201023",
            "ddlc_translate_club_jp_japanese_language_submod_v200504": "ddlc_translate_club_jp_japanese_language_submod_v201023",
            "ddlc_translate_club_jp_japanese_language_submod_v200704": "ddlc_translate_club_jp_japanese_language_submod_v201023",
            "ddlc_translate_club_jp_japanese_language_submod_v200920": "ddlc_translate_club_jp_japanese_language_submod_v201023",
        }
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

label ddlc_translate_club_jp_japanese_language_submod_v201023(version="v201023"):
    python hide:
        import shutil
        def trydel(path):
            try:
                shutil.rmtree(path)
            except Exception as e:
                pass

        # Move /tl/Japanese/overrides/ to /Submods/Japanese Language Submod/
        trydel(renpy.config.gamedir + "/tl/Japanese/overrides")

        # Move /gui/font/ to mod_assets/font/
        trydel(renpy.config.gamedir + "/gui/font")
    return
