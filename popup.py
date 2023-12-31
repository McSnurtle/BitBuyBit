# imports - popup.py, file containing all custom popups used in BitBuyBit
import customtkinter as ctk


class Dialog(ctk.CTkToplevel):
    def __init__(self, title: str, dialog: str, options: list[tuple[str, int]], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.dialog_label = ctk.CTkLabel(self, text=dialog)
        self.dialog_label.pack(side=ctk.TOP, anchor=ctk.CENTER, fill=ctk.BOTH, padx=10, pady=10)
        self.flag = None
        for option in options:
            option_button = ctk.CTkButton(self, text=option[0], command=lambda flag=option[1]: self.trigger(flag=flag))
            option_button.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=10, pady=10)

    def trigger(self, flag):
        self.flag = flag
        self.destroy()

    def finish(self):
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_window(self)
        return self.flag


class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500  # milliseconds
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None
        self.deprecated = None

    def enter(self, event=None):
        self.deprecated = event
        self.schedule()

    def leave(self, event=None):
        self.deprecated = event
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        idx = self.id
        self.id = None
        if idx:
            self.widget.after_cancel(idx)

    def showtip(self, event=None):
        self.deprecated = event
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = ctk.CTkToplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = ctk.CTkLabel(self.tw, text=self.text, justify='left')
        label.pack(ipadx=1, padx=10, pady=10)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


def popup(title, dialog, options, parent):
    dialog = Dialog(title, dialog, options, parent)
    result = dialog.finish()
    return result
