# imports - fav_tickers.py, a simple ticker bar with users favourite tickers loaded from .json files
import customtkinter as ctk


class FavTickers(ctk.CTkFrame):
    def __init__(self, open_settings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'fav_tickers'
        if len(fav_tickers) > 0:
            self.front_frame = ctk.CTkFrame(self)
            self.front_frame.pack(fill=ctk.X)
            self.ticker_labels: list[
                tuple[str, ctk.CTkLabel, float]] = []  # symbol str, label to config later, prev price
            self.settings_redirect = open_settings
            self.updating: bool = True
            self.threads: list[threading.Thread] = []
            self.deprecated = None

            for ticker in fav_tickers:
                try:
                    price = exchange.get_symbol_price(ticker)
                except KeyError:
                    try:
                        price = exchange.get_crypto_price(ticker)
                    except KeyError:
                        price = 0
                        fav_tickers.remove(ticker)
                        with open('./fav_tick.json', 'w') as file:
                            content = json.dumps(fav_tickers)
                            file.write(content)
                        dialog = popup("Ticker Warning",
                                       f"AY! One of your favourited tickers ('{ticker}') is unavailable for live pricing\n"
                                       f"on the Favourite Tickers bar! This is likely due to the Rest API only\n"
                                       f"supporting crypto symbols. It will be automatically removed, and the app will shutdown.\n"
                                       f"You will need to manually re-open the app.\n"
                                       f"from the favourites bar to prevent further errors. If you would like to\n"
                                       f"re-add it and try again, you can do so in Settings.",
                                       [('Ok', 0)], self)
                        self.deprecated = dialog
                        exit_gracefully()
                        # dialog.mainloop()
                ticker_frame = ctk.CTkFrame(self.front_frame)
                ticker_title = ctk.CTkLabel(ticker_frame, text=ticker, font=theme['font']['normal'])
                ticker_title.pack(side=ctk.LEFT, anchor=ctk.NW, padx=theme['pad'][1], pady=theme['pad'][1])
                ticker_price = ctk.CTkLabel(ticker_frame, text=f"{'{:,.3f}'.format(price)}=",
                                            font=theme['font']['normal'])
                ticker_price.pack(side=ctk.LEFT, anchor=ctk.NW, padx=theme['pad'][1], pady=theme['pad'][1])
                self.ticker_labels.append((ticker, ticker_price, price))
                update_thread = threading.Thread(target=lambda: self.update_tickers(
                    index=self.ticker_labels.index((ticker, ticker_price, price))))
                self.threads.append(update_thread)
                update_thread.start()
                ticker_frame.pack(side=ctk.LEFT, padx=theme['pad'][1], pady=theme['pad'][1])

            self.config_button = ctk.CTkButton(self.front_frame, text="Manage Tickers", command=self.settings_redirect)
            self.config_button.pack(side=ctk.RIGHT, padx=theme['pad'][1], pady=theme['pad'][1])
            self.notice_label = ctk.CTkLabel(self.front_frame, text='Live (60s)', font=theme['font']['normal'])
            self.notice_label.pack(side=ctk.RIGHT, padx=theme['pad'][1], pady=theme['pad'][1])

    def update_tickers(self, index):
        try:
            if self.updating:
                time.sleep(60)
                ticker_label = self.ticker_labels[index]
                symbol, label, prev_price = ticker_label
                try:
                    cur_price = exchange.get_symbol_price(symbol)
                except KeyError:
                    try:
                        cur_price = exchange.get_crypto_price(symbol)
                    except KeyError:
                        cur_price = prev_price
                        label.configure(text="ERROR", text_color='red')
                if cur_price > prev_price:
                    label.configure(text=f"{'{:,.3f}'.format(cur_price)}▲", text_color='green')
                elif cur_price < prev_price:
                    label.configure(text=f"{'{:,.3f}'.format(cur_price)}▼", text_color='red')
                else:
                    label.configure(text=f"{'{:,.3f}'.format(cur_price)}=", text_color='white')

                label.update()
                self.ticker_labels[index] = (symbol, label, cur_price)
                self.update_tickers(index=index)
        except RuntimeError:  # program closes
            self.updating = False
