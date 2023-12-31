# imports - welcome.py, simple welcome landing page
import customtkinter as ctk
<<<<<<< HEAD


class Welcome(ctk.CTkFrame):
=======
from pages.base_frame import BaseFrame


class Welcome(BaseFrame):
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
    def __init__(self, master, theme: dict, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.id = 'welcome'
        self.title = ctk.CTkLabel(self, text='Welcome to BitBuyBit', font=theme['font']['title'])
        self.title.pack(anchor=ctk.N, side=ctk.TOP, pady=theme['pad'][2])
        self.subheader = ctk.CTkLabel(self,
<<<<<<< HEAD
                                      text='This is an exchange, programmed by Mc_Snurtle, using the Yahoo!Finance API as a backend, and CustomTkinter as a frontend.')
=======
                                      text='This is an exchange, programmed by Mc_Snurtle, using the Yahoo!Finance '
                                           'API as a backend, and CustomTkinter as a frontend.')
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
        self.subheader.pack(anchor=ctk.N, side=ctk.TOP, pady=(0, theme['pad'][2]))
