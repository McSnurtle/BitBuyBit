# imports - base_frame.py, simple file to allow inheriting of required attributes such as self.id that is referenced
# elsewhere. This is to fix IDE context errors where id could raise AttributeErrors
import customtkinter as ctk


class BaseFrame(ctk.CTkFrame):
    """Solely for IDE context with frame.id referenced in App class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = ''


class BaseScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = ''
