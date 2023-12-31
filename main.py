# main.py - a rudimentary exchange interface using Binance API to trade, by Mc_Snurtle
# imports
import datetime
import os
import time
import sys
import json
<<<<<<< HEAD
import random
import threading
import customtkinter as ctk
import requests
from tkinter import PhotoImage
from PIL import Image, ImageTk
=======
import customtkinter as ctk
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
from dotenv import load_dotenv

from pages.meme import Meme
from pages.tickers import TickerSearch
from pages.welcome import Welcome
from pages.settings import Settings
from pages.resources import ResourcesPage
<<<<<<< HEAD
from bars.fav_tickers import FavTickers
from bars.navigation import NavigationBar
from popup import CreateToolTip, Dialog, popup
=======
from pages.base_frame import BaseFrame, BaseScrollableFrame
from bars.fav_tickers import FavTickers
from bars.navigation import NavigationBar
from popup import popup

import random
import threading
import requests
from tkinter import PhotoImage
from PIL import Image, ImageTk
from dotenv import load_dotenv
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

import chart
import exchange


class App(ctk.CTk):
    def __init__(self, title: str, geometry: tuple[int, int], *args, **kwargs):
        self.width, self.height = geometry
        super(App, self).__init__(*args, **kwargs)
        self.geometry(f"{self.width}x{self.height}")
        self.iconbitmap(os.path.join(proj_dir, 'assets', 'icons', 'icon.ico'))
        self.title(title)
        self.minsize(self.width, self.height)
        self.frame_id = 'meme'

        # TEMP SECURITY WARNING
        warning = popup('Critical Security Alert',
                        "BitBuyBit is currently using plain text .env files to store credential data.\n"
                        "This is very unsecure and is not recommended. Use any account / wallet\n"
                        "linking at your own risk. BitBuyBit will use much safer encrypted files to\n"
                        "store documents in the near future, and it is not recommended to link your\n"
                        "TradingView / Wallets at this time. Please be advised!\n"
                        "\n"
                        "Would you like to proceed?", [('Proceed', 1), ('Abort', 0)], self)
        # warning.mainloop()
        if warning == 0:
            sys.exit(0)

        self.welcome_frame = Welcome(self, theme)
        self.welcome_frame.pack(side=ctk.BOTTOM, padx=theme['pad'][2], pady=theme['pad'][2], fill=ctk.BOTH, expand=True)
<<<<<<< HEAD
        self.meme_frame = Meme(master=self.welcome_frame, proj_dir=proj_dir, parent_geometry=(self.height * 0.5, self.height * 0.5))
        self.meme_frame.pack(side=ctk.BOTTOM, padx=theme['pad'][2], pady=theme['pad'][2], fill=ctk.BOTH, expand=True)
        self.ticker_frame = TickerSearch(self, theme, fav_tickers)
        self.settings_frame = Settings(self, theme, fav_tickers)
        self.resource_frame = ResourcesPage(self, theme)

        # layout
        pages = [('Tickers', lambda frame=self.ticker_frame: self.sel_frame(frame=frame)),
                 ('Resources', lambda frame=self.resource_frame: self.sel_frame(frame=frame)),
                 ('Settings', lambda frame=self.settings_frame: self.sel_frame(frame=frame))]
        self.nav_bar = NavigationBar(self, pages, bg_color=theme['color']['bg2'], theme=theme)
        self.nav_bar.pack(anchor=ctk.NW, side=ctk.TOP, fill=ctk.X)
        if len(fav_tickers) > 0:
            self.fav_tickers = FavTickers(
                open_settings=lambda frame=self.settings_frame: self.sel_frame(frame=frame),
                master=self)
            self.fav_tickers.pack(anchor=ctk.NW, side=ctk.TOP, fill=ctk.X)

        self.frames = [self.welcome_frame, self.ticker_frame, self.resource_frame, self.settings_frame]

        self.update_time()

=======
        self.meme_frame = Meme(master=self.welcome_frame, proj_dir=proj_dir,
                               parent_geometry=(self.height * 0.5, self.height * 0.5))
        self.meme_frame.pack(side=ctk.BOTTOM, padx=theme['pad'][2], pady=theme['pad'][2], fill=ctk.BOTH, expand=True)
        self.ticker_frame = TickerSearch(self, theme, charting_opt, fav_tickers)
        self.settings_frame = Settings(self, theme, fav_tickers, charting_opt, self.exit_gracefully)
        self.resource_frame = ResourcesPage(self, theme)

        # layout
        pages_list = [('Tickers', lambda frame=self.ticker_frame: self.sel_frame(frame=frame)),
                 ('Resources', lambda frame=self.resource_frame: self.sel_frame(frame=frame)),
                 ('Settings', lambda frame=self.settings_frame: self.sel_frame(frame=frame))]
        self.nav_bar = NavigationBar(self, pages_list, bg_color=theme['color']['bg2'], theme=theme)
        self.nav_bar.pack(anchor=ctk.NW, side=ctk.TOP, fill=ctk.X)
        
        if len(fav_tickers) > 0:
            self.fav_tickers = FavTickers(
                open_settings=lambda frame=self.settings_frame: self.sel_frame(frame=frame),

                exit_func=self.exit_gracefully, fav_tickers=fav_tickers, theme=theme, master=self)
            self.fav_tickers.pack(anchor=ctk.NW, side=ctk.TOP, fill=ctk.X)

        self.frames: list[BaseFrame | BaseScrollableFrame] = [self.welcome_frame, self.ticker_frame,
                                                              self.resource_frame, self.settings_frame]

        self.update_time()

    def exit_gracefully(self):
        self.fav_tickers.updating = False
        self.destroy()
        exit(0)

>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
    def update_time(self):
        self.nav_bar.time_label.configure(text=f"{time.strftime('%H:%M:%S')}")
        self.nav_bar.time_label.after(1000, self.update_time)  # after 1 second...

    def sel_frame(self, frame: ctk.CTkFrame):
        [frame.pack_forget() for frame in self.frames]
        if self.frame_id == frame.id:
            frame = self.welcome_frame
        frame.pack(padx=theme['pad'][2], pady=theme['pad'][2], fill=ctk.BOTH, expand=True)
        self.frame_id = frame.id


def exit_gracefully():
    window.fav_tickers.updating = False
    window.destroy()
    exit(0)


if __name__ == '__main__':
    proj_dir = os.path.abspath(os.path.dirname(__file__))
    charting_opt = {'async': True,
                    'legacy': False,
                    'rounding': True,
                    'live': 30}
    load_dotenv('.env')  # supplies COLOR, TV_USER, TV_PASS, etc,..
    with open('assets/theme.json', 'r') as fp:
        theme = json.load(fp)
        theme['font'] = {
            "title": ("Helvetica", 34),
            "subtitle": ("Helvetica", 18),
            "normal": ("Helvetica", 12)
        }
    with open('assets/quotes.json', 'r') as fp:
        quotes = json.load(fp)
    with open('./fav_tick.json', 'r') as fp:
        fav_tickers: list[str] = json.load(fp)
    try:
        ctk.set_default_color_theme(theme['cur_color'])
        ctk.set_appearance_mode(theme['cur_theme'])
    except FileNotFoundError:
        pass
    window = App(geometry=(1280, 720), title="SellBitBuyBit - Mc_Snurtle")
    window.mainloop()
