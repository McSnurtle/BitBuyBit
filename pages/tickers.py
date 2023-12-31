# imports - tickers.py, a CTkFrame to search and launch chart views of symbols
import customtkinter as ctk
import exchange
<<<<<<< HEAD


class TickerSearch(ctk.CTkFrame):
    def __init__(self, master, theme, fav_tickers: list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.theme = theme
        self.id = 'ticker_search'
        self.deprecated = None  # used to prevent some IDE's from complaining about errors when handling tkinter event's. i.e. self.search_tickers()
=======
import requests
import threading
import chart
from pages.base_frame import BaseFrame


class TickerSearch(BaseFrame):
    def __init__(self, master, theme, chart_opt, fav_tickers: list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.theme = theme
        self.charting_opt = chart_opt
        self.id = 'ticker_search'
        self.deprecated = None  # used to prevent some IDE's from complaining about errors when handling tkinter
        # event's. i.e. self.search_tickers()
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.results = None
        self.results_frame = ctk.CTkScrollableFrame(self)
        self.results_frame.pack(fill=ctk.BOTH, expand=True, side=ctk.BOTTOM, anchor=ctk.SW, padx=self.theme['pad'][2],
                                pady=self.theme['pad'][2])
        self.label = ctk.CTkLabel(self, text='Tickers')
        self.label.pack(anchor=ctk.NW, padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT)
<<<<<<< HEAD
        self.search = ctk.CTkEntry(self, placeholder_text='e.g. BTCUSDT, ETH, Ethereum, AAPL, crypto')
=======
        self.search = ctk.CTkEntry(self, placeholder_text='e.g. BTC-USD, AAPL, MARA')
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.search.bind("<Return>", self.search_tickers)  # any key_press will update search
        self.search.pack(anchor=ctk.NW, padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.LEFT, fill=ctk.X,
                         expand=True)
        self.search_button = ctk.CTkButton(self, text='Search', command=self.search_tickers)
        self.search_button.pack(anchor=ctk.NE, padx=self.theme['pad'][1], pady=self.theme['pad'][1], side=ctk.RIGHT)
        self.results_widgets = []
        self.favourites_label = ctk.CTkLabel(self.results_frame, text="Favourites", font=self.theme['font']['title'])
        self.favourites_label.pack(anchor=ctk.W, side=ctk.TOP, padx=self.theme['pad'][2],
                                   pady=(self.theme['pad'][2], self.theme['pad'][1]))
        for ticker in fav_tickers:
            results = exchange.check_symbol(ticker)
            self.show_ticker_card(results, hidden=True)
        self.ticker_sep = ctk.CTkLabel(self.results_frame, text="Results", font=self.theme['font']['title'])
        self.ticker_sep.pack(anchor=ctk.W, side=ctk.TOP, padx=self.theme['pad'][2], pady=(self.theme['pad'][2], 0))

    def search_tickers(self, event=None):

        term = self.search.get()
        self.deprecated = event
        [widget.pack_forget() for widget in self.results_widgets]
        try:
            self.results = exchange.check_symbol(term)
            results = self.results
            self.show_ticker_card(results)
        except requests.exceptions.HTTPError:
            error_frame = ctk.CTkFrame(self.results_frame)
            self.results_widgets.append(error_frame)
            error_frame.pack(anchor=ctk.CENTER)
            result_face = ctk.CTkLabel(error_frame, text="😵", font=self.theme['font']['title'])
            self.results_widgets.append(result_face)
            result_face.pack(anchor=ctk.S, side=ctk.LEFT, padx=self.theme['pad'][1], pady=self.theme['pad'][1])
            result_notice = ctk.CTkLabel(error_frame, text=f"No results found for '{term}'",
                                         font=self.theme['font']['subtitle'])
            self.results_widgets.append(result_notice)
            result_notice.pack(anchor=ctk.W, side=ctk.LEFT, padx=self.theme['pad'][1], pady=self.theme['pad'][1])

    def show_ticker_card(self, results: exchange.check_symbol, hidden=False):
        result_frame = ctk.CTkFrame(self.results_frame)
        result_frame.pack(anchor=ctk.CENTER, fill=ctk.X, padx=self.theme['pad'][2], pady=self.theme['pad'][0])
        ticker_name = ctk.CTkLabel(result_frame, font=self.theme['font']['normal'])
        try:
            ticker_name.configure(text=results['longName'])
        except KeyError:
            ticker_name.configure(text='No longName available')
        ticker_name.pack(anchor=ctk.W, side=ctk.BOTTOM, padx=self.theme['pad'][1], pady=(0, self.theme['pad'][2]))
        ticker_title = ctk.CTkLabel(result_frame, text=results['symbol'], font=self.theme['font']['subtitle'])
        ticker_title.pack(anchor=ctk.SW, side=ctk.LEFT, padx=self.theme['pad'][1], pady=(self.theme['pad'][1], 0))
        data = f"OPEN {results['open']} | HIGH {results['dayHigh']} | LOW {results['dayLow']}"
        ticker_data = ctk.CTkLabel(result_frame, text=data, font=self.theme['font']['normal'])
        ticker_data.pack(anchor=ctk.W, side=ctk.LEFT, pady=(self.theme['pad'][2], 0))
        chart_button = ctk.CTkButton(result_frame, text="Launch Chart",
                                     command=lambda: self.decide_chart(results))
        chart_button.pack(anchor=ctk.E, side=ctk.RIGHT, padx=self.theme['pad'][2], pady=(self.theme['pad'][2], 0))
        if not hidden:
            self.results_widgets.append(result_frame)
            self.results_widgets.append(ticker_name)
            self.results_widgets.append(ticker_title)
            self.results_widgets.append(ticker_data)
            self.results_widgets.append(chart_button)

    def decide_chart(self, results):
<<<<<<< HEAD
        if charting_opt['legacy']:
=======
        if self.charting_opt['legacy']:
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
            self.launch_chart_legacy(results)
            return
        self.launch_chart(results)

    def launch_chart_legacy(self, results):
<<<<<<< HEAD
        chart_view = chart.ChartViewLegacy(results['symbol'], charting_opt['rounding'])
=======
        chart_view = chart.ChartViewLegacy(results['symbol'], self.charting_opt['rounding'])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.deprecated = chart_view.finish()

    def launch_chart(self, results=None):
        response = results
        if type(response) is None:
            response = self.results
<<<<<<< HEAD
        chart_view = chart.ChartView(response['symbol'], charting_opt['rounding'], charting_opt['live'])
        if charting_opt['async']:
=======
        chart_view = chart.ChartView(response['symbol'], self.charting_opt['rounding'], self.charting_opt['live'])
        if self.charting_opt['async']:
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
            chart_thread = threading.Thread(target=lambda: chart_view.show(block=True))
            chart_thread.start()
        else:
            chart_view.show(block=False)
