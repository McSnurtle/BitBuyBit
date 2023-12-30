# imports - navigation.py, a simple navigation bar to get around BitBuyBit
import customtkinter as ctk
import random
import json

with open('assets/quotes.json', 'r') as fp:
    quotes = json.load(fp)


class NavigationBar(ctk.CTkFrame):
    def __init__(self, master, pages, theme, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.id = 'nav_bar'

        for page in pages:
            nav_button = ctk.CTkButton(self, text=page[0], command=page[1])
            nav_button.pack(side=ctk.LEFT, padx=(theme['pad'][2], 0), pady=theme['pad'][1])
        self.time_label = ctk.CTkLabel(self, text='Woopie!')
        self.time_label.pack(side=ctk.RIGHT, padx=theme['pad'][2], pady=theme['pad'][0])
        self.quote = ctk.CTkLabel(self, text=f"As a bozo once said, \"{random.choice(quotes)}\"")
        self.quote.pack(side=ctk.RIGHT, padx=theme['pad'][0], pady=theme['pad'][0])
