<<<<<<< HEAD
# imports - settings.py, an ugly abomination of unoptimized code that was meant for a settings page, not a disgusting mess
import customtkinter as ctk
from popup import CreateToolTip


class Settings(ctk.CTkScrollableFrame):
    def __init__(self, master, theme, fav_tickers: list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.id = 'settings'
        self.fav_tickers = fav_tickers
        self.theme = ctk.get_appearance_mode()

        # layout
        self.title = ctk.CTkLabel(self, text='Settings', font=theme['font']['title'])
        self.title.pack(anchor=ctk.NW, padx=theme['pad'][2], pady=theme['pad'][2])
=======
# imports - settings.py, an unholy abomination of unoptimized code that was meant for a settings menu, not a disgusting
# mess that should be annihilated with a  blowtorch to cleanse the earth of it's existence
import customtkinter as ctk
from pages.base_frame import BaseScrollableFrame
import json
from popup import CreateToolTip, Dialog, popup


class Settings(BaseScrollableFrame):
    def __init__(self, master, theme, fav_tickers: list, charting_opt, exit_func, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.id = 'settings'
        self.charting_opt = charting_opt
        self.theme = theme
        self.exit_gracefully = exit_func
        self.fav_tickers = fav_tickers

        # layout
        self.title = ctk.CTkLabel(self, text='Settings', font=self.theme['font']['title'])
        self.title.pack(anchor=ctk.NW, padx=self.theme['pad'][2], pady=self.theme['pad'][2])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

        # appearance
        self.colors = ['blue', 'dark-blue', 'green']
        self.themes = ['system', 'dark', 'light']
        try:
<<<<<<< HEAD
            self.sel_color = ctk.IntVar(value=self.colors.index(theme['cur_color']))
            self.sel_theme = ctk.IntVar(value=self.themes.index(theme['cur_theme']))
        except ValueError:
            Dialog(title='Colour Warning',
                   dialog=f"An invalid colour scheme was loaded ({theme['cur_color']}) and there was an error loading \n"
                          "your selected theme from ./assets/theme.json. The program will now\n"
=======
            self.sel_color = ctk.IntVar(value=self.colors.index(self.theme['cur_color']))
            self.sel_theme = ctk.IntVar(value=self.themes.index(self.theme['cur_theme']))
        except ValueError:
            Dialog(title='Colour Warning',
                   dialog=f"An invalid colour scheme was loaded ({self.theme['cur_color']}) and there was an error"
                          f"loading \n your selected theme from ./assets/theme.json. The program will now\n"
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
                          "fallback to blue as it's default colour scheme, system as it's default\n"
                          "theme, and will automatically restart. You will have to manually\n"
                          "reboot it later. Navigate to settings to change the colour scheme later.",
                   options=[('Ok', 0)])
            self.sel_color = ctk.IntVar(value=0)
            self.sel_theme = ctk.IntVar(value=0)
            self.update_theme(verbose=False)
<<<<<<< HEAD
        self.appearance_subheader = ctk.CTkLabel(self, text='Appearance', font=theme['font']['subtitle'])
        self.appearance_subheader.pack(anchor=ctk.W, padx=theme['pad'][2])
        self.appearance_desc = ctk.CTkLabel(self,
                                            text='Change the theme of the program, options with (*) require a restart',
                                            font=theme['font']['normal'])
        self.appearance_desc.pack(anchor=ctk.W, padx=theme['pad'][2])
        self.appearance_options_frame = ctk.CTkFrame(self)
        self.appearance_note = ctk.CTkLabel(self.appearance_options_frame, text="Accent Colour * :",
                                            font=theme['font']['normal'])
        self.appearance_note.pack(anchor=ctk.NW, side=ctk.TOP, padx=theme['pad'][1], pady=theme['pad'][1])
=======
        self.appearance_subheader = ctk.CTkLabel(self, text='Appearance', font=self.theme['font']['subtitle'])
        self.appearance_subheader.pack(anchor=ctk.W, padx=self.theme['pad'][2])
        self.appearance_desc = ctk.CTkLabel(self,
                                            text='Change the theme of the program, options with (*) require a restart',
                                            font=self.theme['font']['normal'])
        self.appearance_desc.pack(anchor=ctk.W, padx=self.theme['pad'][2])
        self.appearance_options_frame = ctk.CTkFrame(self)
        self.appearance_note = ctk.CTkLabel(self.appearance_options_frame, text="Accent Colour * :",
                                            font=self.theme['font']['normal'])
        self.appearance_note.pack(anchor=ctk.NW, side=ctk.TOP, padx=self.theme['pad'][1], pady=self.theme['pad'][1])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        for x, color in enumerate(self.colors):
            color_radial = ctk.CTkRadioButton(self.appearance_options_frame,
                                              text='-'.join([word[0].upper() + word[1:] for word in color.split('-')]),
                                              command=self.update_theme, variable=self.sel_color, value=x)
<<<<<<< HEAD
            color_radial.pack(side=ctk.LEFT, padx=theme['pad'][1], pady=(0, theme['pad'][1]))
        self.appearance_options_frame.pack(anchor=ctk.W, padx=theme['pad'][2])

        self.appearance_options_frame1 = ctk.CTkFrame(self)
        self.appearance_note1 = ctk.CTkLabel(self.appearance_options_frame1, text='Theme:',
                                             font=theme['font']['normal'])
        self.appearance_note1.pack(anchor=ctk.NW, side=ctk.TOP, padx=theme['pad'][1], pady=theme['pad'][1])
=======
            color_radial.pack(side=ctk.LEFT, padx=self.theme['pad'][1], pady=(0, self.theme['pad'][1]))
        self.appearance_options_frame.pack(anchor=ctk.W, padx=self.theme['pad'][2])

        self.appearance_options_frame1 = ctk.CTkFrame(self)
        self.appearance_note1 = ctk.CTkLabel(self.appearance_options_frame1, text='Theme:',
                                             font=self.theme['font']['normal'])
        self.appearance_note1.pack(anchor=ctk.NW, side=ctk.TOP, padx=self.theme['pad'][1], pady=self.theme['pad'][1])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        for x, theming in enumerate(self.themes):
            theme_radial = ctk.CTkRadioButton(self.appearance_options_frame1,
                                              text=f'{theming[0].upper()}{theming[1:]}', command=self.update_theme,
                                              variable=self.sel_theme, value=x)
<<<<<<< HEAD
            theme_radial.pack(side=ctk.LEFT, padx=theme['pad'][1], pady=(0, theme['pad'][1]))
        self.appearance_options_frame1.pack(anchor=ctk.W, padx=theme['pad'][2], pady=theme['pad'][1])

        # tickers
        self.ticker_subheader = ctk.CTkLabel(self, text='Favourite Tickers', font=theme['font']['subtitle'])
        self.ticker_subheader.pack(anchor=ctk.W, padx=theme['pad'][2])
        self.ticker_desc = ctk.CTkLabel(self,
                                        text='Add or remove tickers from the Favourite Tickers bar (requires restart)',
                                        font=theme['font']['normal'])
        self.ticker_desc.pack(anchor=ctk.W, padx=theme['pad'][2])
=======
            theme_radial.pack(side=ctk.LEFT, padx=self.theme['pad'][1], pady=(0, self.theme['pad'][1]))
        self.appearance_options_frame1.pack(anchor=ctk.W, padx=self.theme['pad'][2], pady=self.theme['pad'][1])

        # tickers
        self.ticker_subheader = ctk.CTkLabel(self, text='Favourite Tickers', font=self.theme['font']['subtitle'])
        self.ticker_subheader.pack(anchor=ctk.W, padx=self.theme['pad'][2])
        self.ticker_desc = ctk.CTkLabel(self,
                                        text='Add or remove tickers from the Favourite Tickers bar (requires restart)',
                                        font=self.theme['font']['normal'])
        self.ticker_desc.pack(anchor=ctk.W, padx=self.theme['pad'][2])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.ticker_options_frame = ctk.CTkFrame(self)

        if len(self.fav_tickers) > 0:
            self.tickers_frame = ctk.CTkFrame(self.ticker_options_frame, width=400, height=90)
            for ticker in self.fav_tickers:
                ticker_frame = ctk.CTkFrame(self.tickers_frame)
<<<<<<< HEAD
                ticker_name = ctk.CTkLabel(ticker_frame, text=ticker, font=theme['font']['normal'])
                ticker_name.pack(side=ctk.LEFT, padx=theme['pad'][1], pady=theme['pad'][1])
                ticker_remove = ctk.CTkButton(ticker_frame, text='Remove', width=1, font=theme['font']['normal'],
                                              command=lambda: self.remove_ticker(ticker))
                ticker_remove.pack(side=ctk.LEFT, padx=theme['pad'][1], pady=theme['pad'][1])
                ticker_frame.pack(anchor=ctk.NW, side=ctk.LEFT, padx=theme['pad'][1], pady=theme['pad'][1])
            self.tickers_frame.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.BOTTOM)
        else:
            ticker_notice = ctk.CTkLabel(self.ticker_options_frame, text='Add Tickers for them to show up here.',
                                         font=theme['font']['subtitle'])
            ticker_notice.pack(anchor=ctk.CENTER, side=ctk.BOTTOM, pady=theme['pad'][1])
        self.ticker_note = ctk.CTkLabel(self.ticker_options_frame, text='Add Ticker:', font=theme['font']['normal'])
        self.ticker_note.pack(anchor=ctk.W, padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.LEFT)
        self.ticker_add = ctk.CTkButton(self.ticker_options_frame, text="Save", command=self.add_ticker)
        self.ticker_add.pack(anchor=ctk.E, padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.RIGHT)
        self.ticker_entry = ctk.CTkEntry(self.ticker_options_frame, placeholder_text='e.g. BTC, ETH | <Return> to add')
        self.ticker_entry.bind('<Return>', self.add_ticker)
        self.ticker_entry.pack(anchor=ctk.W, padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.LEFT, fill=ctk.X,
                               expand=True)
        self.ticker_options_frame.pack(padx=theme['pad'][2], pady=(0, theme['pad'][2]), anchor=ctk.W)
=======
                ticker_name = ctk.CTkLabel(ticker_frame, text=ticker, font=self.theme['font']['normal'])
                ticker_name.pack(side=ctk.LEFT, padx=self.theme['pad'][1], pady=self.theme['pad'][1])
                ticker_remove = ctk.CTkButton(ticker_frame, text='Remove', width=1, font=self.theme['font']['normal'],
                                              command=lambda: self.remove_ticker(ticker))
                ticker_remove.pack(side=ctk.LEFT, padx=self.theme['pad'][1], pady=self.theme['pad'][1])
                ticker_frame.pack(anchor=ctk.NW, side=ctk.LEFT, padx=self.theme['pad'][1], pady=self.theme['pad'][1])
            self.tickers_frame.pack(padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.BOTTOM)
        else:
            ticker_notice = ctk.CTkLabel(self.ticker_options_frame, text='Add Tickers for them to show up here.',
                                         font=self.theme['font']['subtitle'])
            ticker_notice.pack(anchor=ctk.CENTER, side=ctk.BOTTOM, pady=self.theme['pad'][1])
        self.ticker_note = ctk.CTkLabel(self.ticker_options_frame, text='Add Ticker:',
                                        font=self.theme['font']['normal'])
        self.ticker_note.pack(anchor=ctk.W, padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT)
        self.ticker_add = ctk.CTkButton(self.ticker_options_frame, text="Save", command=self.add_ticker)
        self.ticker_add.pack(anchor=ctk.E, padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.RIGHT)
        self.ticker_entry = ctk.CTkEntry(self.ticker_options_frame, placeholder_text='e.g. BTC, ETH | <Return> to add')
        self.ticker_entry.bind('<Return>', self.add_ticker)
        self.ticker_entry.pack(anchor=ctk.W, padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT,
                               fill=ctk.X,
                               expand=True)
        self.ticker_options_frame.pack(padx=self.theme['pad'][2], pady=(0, self.theme['pad'][2]), anchor=ctk.W)
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

        # charting options
        self.async_charting = ctk.BooleanVar(value=True)
        self.legacy_charting = ctk.BooleanVar(value=False)
        self.chart_rounding = ctk.BooleanVar(value=True)
        self.live_charting = ctk.BooleanVar(value=True)
<<<<<<< HEAD
        self.charting_subheader = ctk.CTkLabel(self, text='Chart Options', font=theme['font']['subtitle'])
        self.charting_subheader.pack(anchor=ctk.W, padx=theme['pad'][2])
        self.charting_desc = ctk.CTkLabel(self,
                                          text='Configure charting behaviour when interacting and viewing charts',
                                          font=theme['font']['normal'])
        self.charting_desc.pack(anchor=ctk.W, padx=theme['pad'][2])
=======
        self.charting_subheader = ctk.CTkLabel(self, text='Chart Options', font=self.theme['font']['subtitle'])
        self.charting_subheader.pack(anchor=ctk.W, padx=self.theme['pad'][2])
        self.charting_desc = ctk.CTkLabel(self,
                                          text='Configure charting behaviour when interacting and viewing charts',
                                          font=self.theme['font']['normal'])
        self.charting_desc.pack(anchor=ctk.W, padx=self.theme['pad'][2])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.charting_options_frame = ctk.CTkFrame(self)

        self.charting_options_frame = ctk.CTkFrame(self)
        self.async_chart = ctk.CTkCheckBox(self.charting_options_frame, text="Asynchronous charting",
                                           command=self.update_async_chart, variable=self.async_charting, onvalue=True,
                                           offvalue=False)
        CreateToolTip(self.async_chart,
                      "Whether launching new ChartView widgets should be done asynchronously in it's\n"
                      "own thread (shouldn't cause multithreading problems when closing application).\n"
                      "\n"
                      "Modifying properties such as chart interval uses a callback that\n"
                      "requires the main thread of the ChartView to be blocking, thus needing it's own\n"
                      "thread to prevent crashing in the mainloop. Disabling this will prevent changing\n"
                      "intervals from 1h in the ChartView. Note that disabling this does not prevent\n"
                      "other ChartViews from being launched, as this only affects if there should be a\n"
                      "new thread spawned containing a blocking ChartView, or just\n"
                      "launch a non-blocking ChartView.")
<<<<<<< HEAD
        self.async_chart.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.LEFT)
=======
        self.async_chart.pack(padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT)
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.legacy_chart = ctk.CTkCheckBox(self.charting_options_frame, text="Legacy ChartView widget",
                                            command=self.update_chart_type, variable=self.legacy_charting, onvalue=True,
                                            offvalue=False)
        CreateToolTip(self.legacy_chart,
                      "Whether to use the legacy ChartView widget or not.\n"
                      "\n"
                      "To quote a beta-tester; the ''clunky'' legacy ChartView widgets used MatPlotLib for charting\n"
                      "and thus had bad performance and a ''janky'' interface. Only use this if you are having\n"
                      "trouble getting the latest ''modern'' ChartView widget working.")
<<<<<<< HEAD
        self.legacy_chart.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.LEFT)
=======
        self.legacy_chart.pack(padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT)
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.rounding = ctk.CTkCheckBox(self.charting_options_frame, text="Chart rounding",
                                        command=self.update_chart_rounding, variable=self.chart_rounding, onvalue=True,
                                        offvalue=False)
        CreateToolTip(self.rounding,
                      "Whether to round the chart data to the nearest 1/10 cent.\n"
                      "\n"
                      "Disable when charts that have extremely low values (e.g. values beyond 0.000).\n"
                      "Using rounding on highly precise charts such as these causes extreme visual bugs where\n"
                      "the min and max price of the asset is zero, and the current price is not.")
<<<<<<< HEAD
        self.rounding.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.LEFT)
=======
        self.rounding.pack(padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT)
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.live = ctk.CTkCheckBox(self.charting_options_frame, text="Live Charting",
                                    command=self.update_live_charting, variable=self.live_charting, onvalue=True,
                                    offvalue=False)
        CreateToolTip(self.live, "Whether to live update chart data every 30 seconds.\n"
                                 "\n"
                                 "Disable this if concerned about data usage, as when the chart refreshes all\n"
                                 "of the market's context data / history for the current interval is re-downloaded.")
<<<<<<< HEAD
        self.live.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.LEFT)
        self.charting_options_frame.pack(padx=theme['pad'][2], pady=(0, theme['pad'][2]), anchor=ctk.W)

    def update_live_charting(self):
        charting_opt['live'] = self.live_charting.get()

    def update_chart_rounding(self):
        charting_opt['rounding'] = self.chart_rounding.get()

    def update_async_chart(self):
        charting_opt['async'] = self.async_charting.get()

    def update_chart_type(self):
        charting_opt['legacy'] = self.legacy_charting.get()
=======
        self.live.pack(padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT)
        self.charting_options_frame.pack(padx=self.theme['pad'][2], pady=(0, self.theme['pad'][2]), anchor=ctk.W)

    def update_live_charting(self):
        self.charting_opt['live'] = self.live_charting.get()

    def update_chart_rounding(self):
        self.charting_opt['rounding'] = self.chart_rounding.get()

    def update_async_chart(self):
        self.charting_opt['async'] = self.async_charting.get()

    def update_chart_type(self):
        self.charting_opt['legacy'] = self.legacy_charting.get()
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

    def remove_ticker(self, symbol, verbose=True):
        try:
            self.fav_tickers.remove(symbol)
            if verbose:
                dialog = popup("Ticker Warning", "Modifying favourite tickers requires an app restart!\n"
                                                 "\n"
                                                 "Would you like to restart now?",
                               [('Save & Restart', 0), ('Save & Restart Later', 1), ('Abort', 2)], self)
                # dialog.mainloop()
                flag = dialog
            else:
                flag = 1
            if flag < 2:
                with open('./fav_tick.json', 'w') as file:
                    content = json.dumps(self.fav_tickers)
                    file.write(content)
            if flag == 0:
<<<<<<< HEAD
                exit_gracefully()
=======
                self.exit_gracefully()
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        except IndexError:
            pass

    def add_ticker(self, verbose=True):
        symbol = self.ticker_entry.get()
        self.fav_tickers.append(symbol)
        if verbose:
            dialog = popup("Ticker Warning", "Modifying favourite tickers requires an app restart!\n"
                                             "\n"
                                             "Would you like to restart now?",
                           [('Save & Restart', 0), ('Save & Restart Later', 1), ('Abort', 2)], self)
            # dialog.mainloop()
            flag = dialog
        else:
            flag = 1
        if flag < 2:
            with open('./fav_tick.json', 'w') as file:
                content = json.dumps(self.fav_tickers)
                file.write(content)
        if flag == 0:
<<<<<<< HEAD
            exit_gracefully()
=======
            self.exit_gracefully()
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

    def update_theme(self, verbose=True):
        if verbose:
            dialog = popup("Colour Warning", "Changing colour themes requires an app restart!\n"
                                             "\n"
                                             "Would you like to restart now?",
                           [('Save & Restart', 0), ('Save & Restart Later', 1), ('Abort', 2)], self)
            # dialog.mainloop()
            flag = dialog
        else:
            flag = 1
        if flag is not None:
            if flag < 2:
                with open('./assets/theme.json', 'w') as file:
<<<<<<< HEAD
                    theme['cur_color'] = self.colors[self.sel_color.get()]
                    theme['cur_theme'] = self.themes[self.sel_theme.get()]
                    content = json.dumps(theme)
                    file.write(content)
            if flag == 0:
                exit_gracefully()
=======
                    self.theme['cur_color'] = self.colors[self.sel_color.get()]
                    self.theme['cur_theme'] = self.themes[self.sel_theme.get()]
                    content = json.dumps(self.theme)
                    file.write(content)
            if flag == 0:
                self.exit_gracefully()
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

        ctk.set_appearance_mode(self.themes[self.sel_theme.get()])
        ctk.set_default_color_theme(self.colors[self.sel_color.get()])
