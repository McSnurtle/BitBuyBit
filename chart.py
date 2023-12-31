# imports - chart.py, representing pandas df using interactive plotly interface, by Mc_Snurtle
# import plotly.graph_objects as go
import threading
import yfinance as yf
import pandas as pd
import time
import exchange
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import lightweight_charts as lwc
import mplfinance as mpl
import customtkinter as ctk


# pd.options.plotting.backend = 'plotly'


def chart_view_legacy(symbol, interval='1D', rounding=True):
    data = exchange.get_historical(symbol, interval, rounding)
    data['Date'] = data.index
    # data['Date'] = pd.to_datetime(data['Date'])
    # fig = plt.figure(data=[
    #     go.Candlestick(x=data['Date'], open=data['Open'], close=data['Close'], low=data['Low'], high=data['High'])])
    # fig.update_layout(xaxis_rangeslider_visible=False)  # to disable range slider
    # fig.show()
    # market_colors = mpl.make_marketcolors(up='g', down='r', inherit=True)
    # mpl.make_mpf_style(base_mpf_style='nightclouds', marketcolors=market_colors)
    fig, ax = mpl.plot(data, style='mike', type='candle', mav=(3, 6, 9), title=f'{symbol} Asset Value', volume=True,
                       returnfig=True,
                       warn_too_much_data=99999)  # mav == moving_average
    return fig


class ChartView(lwc.Chart):
    def __init__(self, symbol: str, rounding: bool, live: bool | int, *args, **kwargs):
        """ChartView widget class

        :param symbol: str, ticker name abbreviation. e.g. MARA
        :param rounding: bool, whether to round decimal values to the nearest thousandth
        :param live: bool | int, False for static data, int to specify seconds to wait on update"""
        super().__init__(title=f"{symbol} Asset Value", toolbox=True, *args, **kwargs)
        self.symbol = symbol
        self.rounding = rounding
        self.live = live
        self.legend(visible=True)
        self.topbar.switcher('Interval', ('1m', '2m', '5m', '15m', '30m', '1h', '90m', '1d', '1wk'), default='1h',
                             func=self.update_interval)
        data = exchange.get_historical(self.symbol, interval='1h', rounding=rounding)
        self.set(data)

        if isinstance(live, int):
            update_thread = threading.Thread(target=self.refresh_data)
            update_thread.start()

    def refresh_data(self):
        print("REFRESHING DF!")
        self.update_interval(self)
        time.sleep(self.live)
        self.refresh_data()

    def update_interval(self, chart):
        data = exchange.get_historical(symbol=self.symbol, interval=self.topbar['Interval'].value, rounding=self.rounding)
        chart.set(data,
                  False)  # render_drawings re-renders user-drawings at the new scale to prevent them from being deleted


class ChartViewLegacy(ctk.CTkToplevel):
    def __init__(self, symbol, interval='1h', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(f"BitBuyBit - {symbol} Candlestick")
        self.attributes('-topmost', True)
        self.intervals = ["1m", "2m", "5m", '15m', '30m', '1h', '90m', '1d', '5d',
                          '1wk', '1mo', '3mo']
        self.interval = ctk.StringVar(value=interval)
        self.prev_interval = ctk.StringVar(value='0m')
        self.symbol = symbol

        # options
        self.chart_options_top = ctk.CTkFrame(self)
        self.chart_options_top.pack(padx=20, pady=10, fill=ctk.X, side=ctk.TOP)
        self.chart_interval_label = ctk.CTkLabel(self.chart_options_top, text='Interval', font=("Helvetica", 18))
        self.chart_interval_label.pack(padx=10, pady=10, side=ctk.LEFT, anchor=ctk.W)
        self.chart_interval = ctk.CTkOptionMenu(self.chart_options_top,
                                                values=self.intervals, variable=self.interval,
                                                command=self.update_interval)
        self.chart_interval.pack(padx=10, pady=10, side=ctk.LEFT, anchor=ctk.W)
        self.chart_refresh = ctk.CTkButton(self.chart_options_top, text="Refresh", command=self.update_chart_legacy)
        self.chart_refresh.pack(padx=10, pady=10, side=ctk.LEFT, anchor=ctk.W)

        # chart view - LEGACY
        self.chart_frame = ctk.CTkFrame(self)
        self.chart_frame.pack(anchor=ctk.CENTER, padx=20, pady=20, fill=ctk.BOTH, expand=True)
        chart = chart_view_legacy(self.symbol, self.interval.get())
        self.canvas = FigureCanvasTkAgg(chart, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=ctk.BOTTOM, fill=ctk.BOTH, expand=True)
        self.navigation_bar = NavigationToolbar2Tk(self.canvas, self.chart_frame, pack_toolbar=False)
        self.navigation_bar.pack(side=ctk.TOP, fill=ctk.X)

    def update_interval(self, choice):
        self.interval = ctk.StringVar(value=choice)
        self.update_chart_legacy()

    def update_chart_legacy(self):
        chart = chart_view_legacy(self.symbol,
                                  self.interval.get())
        self.canvas.get_tk_widget().pack_forget()
        self.navigation_bar.pack_forget()
        self.canvas = FigureCanvasTkAgg(chart, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=ctk.BOTTOM, fill=ctk.BOTH, expand=True)
        self.navigation_bar = NavigationToolbar2Tk(self.canvas, self.chart_frame, pack_toolbar=False)
        self.navigation_bar.pack(side=ctk.TOP, fill=ctk.X)

    def trigger(self):
        self.destroy()

    def finish(self):
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_window(self)
        return self.chart_frame
