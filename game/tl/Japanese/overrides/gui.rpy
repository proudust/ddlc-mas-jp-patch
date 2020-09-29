define -2 jpfonts.VLGothic = "gui/font/VL-Gothic-Regular.ttf"
define -2 jpfonts.Mikachan = "gui/font/Mikachan.ttf"
define -2 jpfonts.HolidayMDJP = "gui/font/HolidayMDJP.otf"
define -2 jpfonts.TegakiZatsu = "gui/font/851tegaki_zatsu_normal.ttf"
define -2 jpfonts.GataSosyo = "gui/font/gatasosyo.ttf"
define -2 jpfonts.SanaFon = "gui/font/SNsanafonP.ttf"
define -2 jpfonts.Ruriiro = "gui/font/Ruriiro_font.ttf"

translate Japanese python:
    gui.default_font = jpfonts.VLGothic
    gui.name_font = gui.default_font
    gui.interface_font = gui.default_font
    gui.choice_button_borders = Borders(10, 5, 10, 5)
