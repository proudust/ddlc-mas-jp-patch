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

translate Japanese style chibika_note_text:
    font jpfonts.Mikachan

translate Japanese style twopane_scrollable_menu_button:
    padding (17, 5, 17, 5)

translate Japanese style twopane_scrollable_menu_button_dark:
    padding (17, 5, 17, 5)

# styles.rpy
translate Japanese style generic_fancy_check_button_text:
    font jpfonts.Mikachan

translate Japanese style generic_fancy_check_button_text_dark:
    font jpfonts.Mikachan

translate Japanese screen:
    # 名前入力の制限撤廃
    screen name_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add mas_getTimeFile("gui/overlay/confirm.png")
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
    # カレンダーのフォント変更
    MASCalendar.NOTE_FONT = jpfonts.Ruriiro

    # カレンダーの表示微調整
    MASCalendar.DATE_DISPLAY_FORMAT = "                   {0}\n{1}\n{2}\n{3}"

    # 日付のフォーマットを日本式に置き換え
    def genFormalDispDate(_date):
        return (
            "".join([str(_date.year), "年", str(_date.month), "月", str(_date.day), "日"]),
            datetime.date.today() - _date
        )
    store.mas_calendar.genFormalDispDate = genFormalDispDate

    # カレンダーの文字の書式調整
    def _setupDayButtons(self):
            """
            Sets up the day buttons used in the calendar
            """

            # button backgrounds
            button_day_bg = Image(
                ("mod_assets/calendar/calendar_day_bg.png" if self.day_mode else "mod_assets/calendar/calendar_day_bg-n.png")
            )

            button_day_bg_disabled = Image(
                ("mod_assets/calendar/calendar_day_disabled_bg.png" if self.day_mode else "mod_assets/calendar/calendar_day_disabled_bg-n.png")
            )

            button_day_bg_hover = Image(
                "mod_assets/calendar/calendar_day_hover_bg.png"
            )

            button_today_bg = Image(
                ("mod_assets/calendar/calendar_today_bg.png" if self.day_mode else "mod_assets/calendar/calendar_today_bg-n.png")
            )

            button_today_bg_disabled = Image(
                ("mod_assets/calendar/calendar_today_disabled_bg.png" if self.day_mode else "mod_assets/calendar/calendar_today_disabled_bg-n.png")
            )

            button_today_bg_hover = Image(
                "mod_assets/calendar/calendar_today_hover_bg.png"
            )


            # constant month and year text labels
            self.text_current_month = Text(
                "{#month}" + self.MONTH_NAMES[self.selected_month],
                font=gui.default_font,
                size=21,
                color=self.DAY_NUMBER_COLOR,
                outlines=[]
            )

            self.text_current_year = Text(
                str(self.selected_year),
                font=gui.default_font,
                size=21,
                color=self.DAY_NUMBER_COLOR,
                outlines=[]
            )

            # init day buttons array
            self.day_buttons = []
            self.day_button_texts = []

            # set the note style attributes
            note_font = self.NOTE_FONT
            note_text_size = self.NOTE_TEXT_SIZE
            note_color = self.NOTE_COLOR
            note_ystart = 1

            # get relevant date info
            day = datetime.timedelta(days=1)
            first_day = datetime.datetime(self.selected_year, self.selected_month, 1)

            # get the first_day of the week that has the first day of current month
            while first_day.weekday() != 6:
                first_day = first_day - day

            # init the array that will hold the dates we're displaying
            self.dates = []

            # get all the dates we'll be displaying  and store them on the array
            for i in range(42):
                self.dates.append(first_day + datetime.timedelta(days=i))

            # get this month's events
            if self.MIN_GLITCH_YEAR < self.selected_year < self.MAX_GLITCH_YEAR:
                events = self.database[self.selected_month]

                #For leap year case, we put F29 into M01
                if self.selected_month == 3 and not mas_isLeapYear(self.selected_year):
                    #We need to copy this because otherwise we break the main calendar db
                    events = copy.deepcopy(events)
                    events[1].update(self.database[2][29])


            #Otherwise glitch events
            else:
                events = self._getEGMonthEvents()

                note_font = gui.default_font
                note_text_size = self.DAY_NUMBER_TEXT_SIZE
                note_color = self.DAY_NUMBER_COLOR
                note_ystart = 5


            # calculation to determine the initial y position
            initial_y = self.INITIAL_POSITION_Y + (self.DAY_NAME_BUTTON_HEIGHT * 2)

            # iterate over rows and columns to create our calendar ui
            for i in range(6):

                for j in range(7):

                    # helper vars for day processing
                    current_date = self.dates[j + (i * 7)]
                    ret_val = None
                    many_events = False
                    day_bg_disabled = button_day_bg_disabled
                    today_bg_disabled = button_today_bg_disabled

                    # current day events display helpers
                    event_labels = list()

                    # if this day is on the current month process the events that it may have
                    if current_date.month == self.selected_month:
                        _todays_events = events[current_date.day]

                        # iterate through them
                        for k in _todays_events:
                            e = _todays_events[k]

                            # check for event type
                            if e[0] == CAL_TYPE_EV:
                                # retrieve the event
                                ev = mas_getEV(k)

                                if self._isEvInYear(ev, self.selected_year):
                                    event_labels.append(mas_getEVCL(k))

                            # non event type
                            if e[0] == CAL_TYPE_REP:
                                # if the year is not None or it's contained in it's range
                                if e[2] is not None and ( not e[2] or self.selected_year in e[2]):
                                    # add the non event
                                    event_labels.append(e[1])

                        if len(event_labels) > 3:
                            many_events = True
                            if not self.can_select_date:
                                ret_val = event_labels

                    # if we don't have any labels or less than 3
                    if not event_labels or len(event_labels) < 3:

                        # we can safely add 3 empty ones
                        event_labels.extend([""] * 3)

                    # Add button behaviour to it
                    if current_date.month == self.selected_month:
                        day_bg_disabled = button_day_bg
                        today_bg_disabled = button_today_bg

                        if self.can_select_date:
                            ret_val = current_date

                    # The button itself

                    # Set the final BGs for the day button
                    final_bg_idle = button_day_bg
                    final_bg_hover = button_day_bg_hover
                    final_bg_disabled = day_bg_disabled

                    # The date in current iteration is today
                    if (current_date.day == self.today.day) and (current_date.month == self.today.month) and (current_date.year == self.today.year):
                        final_bg_idle = button_today_bg
                        final_bg_hover = button_today_bg_hover
                        final_bg_disabled = today_bg_disabled

                    button_pos = (self.INITIAL_POSITION_X + (j * self.DAY_BUTTON_WIDTH),
                        initial_y + (i * self.DAY_BUTTON_HEIGHT))

                    day_button = MASButtonDisplayable(
                        Null(),
                        Null(),
                        Null(),
                        final_bg_idle,
                        final_bg_hover,
                        final_bg_disabled,
                        button_pos[0],
                        button_pos[1],
                        self.DAY_BUTTON_WIDTH,
                        self.DAY_BUTTON_HEIGHT,
                        hover_sound=gui.hover_sound,
                        activate_sound=gui.activate_sound,
                        return_value=ret_val
                    )

                    # if this day isn't on the current month
                    if current_date.month != self.selected_month or (not self.can_select_date and not many_events):
                        # disable the button
                        day_button.disable()

                    self.day_buttons.append(day_button)

                    # Button text
                    text_container = Container(
                        pos=button_pos,
                        xsize=self.DAY_BUTTON_WIDTH,
                        ysize=self.DAY_BUTTON_HEIGHT
                    )

                    # Day number
                    day_number_text = Text(
                        str(current_date.day),
                        font=gui.default_font,
                        size=self.DAY_NUMBER_TEXT_SIZE,
                        color=self.DAY_NUMBER_COLOR,
                        outlines=[],
                        pos=(self.DAY_BUTTON_WIDTH - 7, 5),
                        xanchor=1.0
                    )
                    text_container.add(day_number_text)

                    # Day notes
                    # TODO: implement font switching depending on the day (e.g., holidays)
                    for k in range(3):
                        # This way we don't have to iterate and try to render empty text surfaces
                        if len(event_labels[k]) != 0:
                            note_text = Text(
                                __(event_labels[k]),
                                font=note_font,
                                size=note_text_size,
                                color=note_color,
                                outlines=[],
                                xsize=110, # 長いと日付表示と被るのでその対策
                                pos=(8, note_ystart + k * 17)
                            )
                            text_container.add(note_text)

                    # Create an ellipsis if needed
                    if many_events:
                        ellipsis_text = Text(
                            "...",
                            font=gui.default_font,
                            size=16,
                            color=self.DAY_NUMBER_COLOR,
                            outlines=[],
                            pos=(self.DAY_BUTTON_WIDTH - 7, 43),
                            xanchor=1.0
                        )
                        text_container.add(ellipsis_text)

                    self.day_button_texts.append((text_container, button_pos))
    # 後のバージョンで使用した際にバグるのを回避するための安全策
    if config.version in ['0.11.9', '0.12.0', '0.12.1', '0.12.2', '0.12.3', '0.12.4', '0.12.5', '0.12.6', '0.12.7', '0.12.8']:
        MASCalendar._setupDayButtons = _setupDayButtons

# zz_games.rpy
translate Japanese python in mas_games:
    # https://github.com/proudust/ddlc-mas-jp-patch/issues/66#issuecomment-1493194550
    def getGameEVByPrompt(gamename):
        """
        Gets the game ev using the prompt of its event (gamename)

        IN:
            gamename - Name of the game we want to get

        OUT:
            event object for the game entered if found. None if not found
        """
        global game_db

        #Adjust the gamename to be lower prior to looping
        gamename = gamename.lower()

        #Now search
        for ev in game_db.itervalues():
            if renpy.substitute(ev.prompt, translate=False).lower() == gamename:
                return ev
        return None
    getGameEVByPrompt = getGameEVByPrompt

# zz_poems.rpy
translate Japanese style mas_monika_poem_text:
    font jpfonts.Ruriiro
    size 30
