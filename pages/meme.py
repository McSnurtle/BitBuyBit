# imports - meme.py, simple frame containing a random meme.png
import customtkinter as ctk
import random
import os
from PIL import Image


class Meme(ctk.CTkLabel):
    def __init__(self, master, proj_dir, parent_geometry: tuple[int | float, int | float], *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.id = 'meme'
        self.meme = random.choice([os.path.join(proj_dir, 'assets', 'memes', file) for file in
                                   os.listdir(os.path.join(proj_dir, 'assets', 'memes')) if
                                   file.endswith('.png')])  # returns full path to random png in ./assets/icons/
        self.photo_label = ctk.CTkImage(Image.open(self.meme), size=parent_geometry)
        self.configure(text='', image=self.photo_label)
