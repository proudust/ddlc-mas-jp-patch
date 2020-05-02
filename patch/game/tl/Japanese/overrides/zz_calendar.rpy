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
