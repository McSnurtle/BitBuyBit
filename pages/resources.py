# imports - resources.py, a reference page for users to navigate outside BitBuyBit
import customtkinter as ctk
import json
<<<<<<< HEAD
=======
import webbrowser
from pages.base_frame import BaseFrame
from popup import Dialog
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2

with open('./assets/user-references.json', 'r') as fp:
    user_references: list[list] = json.load(fp)


def save_reference(title: str, link: str):
    user_references.append([title, link])
    with open('./assets/user-references.json', 'w') as file:
        content = json.dumps(user_references)
        file.write(content)


def remove_reference(title: str, link: str):
    try:
        user_references.remove([title, link])
        with open('./assets/user-references.json', 'w') as file:
            content = json.dumps(user_references)
            file.write(content)
    except IndexError:
        pass


def visit_reference(link: str):
    dialog = Dialog("External Services Warning", "Warning! Continuing will take you to an external site on an\n"
                                                 "external browser. BitBuyBit cannot verify the safety of the site\n"
                                                 "nor browser. Only proceed if you put this here!\n"
                                                 "\n"
                                                 "Continue?", options=[("Continue", 0), ("Abort", 1)])
    flag = dialog.finish()
    if flag == 0:
        webbrowser.open(link, new=0, autoraise=False)


<<<<<<< HEAD
class ResourcesPage(ctk.CTkFrame):
=======
class ResourcesPage(BaseFrame):
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
    def __init__(self, master, theme: dict, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.id = 'accounts'

        self.title = ctk.CTkLabel(self, text="Resources", font=theme['font']['title'])
        self.title.pack(anchor=ctk.NW, padx=theme['pad'][1], pady=theme['pad'][1])

        # Dev Resources
        self.subheader = ctk.CTkLabel(self, text="Developer References",
                                      font=theme['font']['subtitle'])
        self.subheader.pack(anchor=ctk.NW, padx=theme['pad'][1], pady=(0, theme['pad'][1]))

        # User Resources
        self.user_subheader = ctk.CTkLabel(self, text="User References",
                                           font=theme['font']['subtitle'])
        self.user_subheader.pack(anchor=ctk.NW, padx=theme['pad'][1], pady=(0, theme['pad'][1]))
        self.user_frame = ctk.CTkFrame(self)
        for reference in user_references:
            reference_frame = ctk.CTkFrame(self.user_frame)
<<<<<<< HEAD
            reference_frame.pack(padx=theme['pad'][1], pady=theme['pad'][1], anchor=ctk.W, fill=ctk.X)
            reference_link = ctk.CTkLabel(reference_frame, text=reference[1], font=theme['font']['normal'])
=======
            reference_frame.pack(padx=theme['pad'][1], pady=theme['pad'][1], anchor=ctk.W, fill=ctk.X, expand=True)
            reference_link = ctk.CTkEntry(reference_frame, placeholder_text=reference[1], font=theme['font']['normal'])
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
            reference_link.pack(padx=theme['pad'][1], side=ctk.BOTTOM, anchor=ctk.NW)
            reference_title = ctk.CTkEntry(reference_frame, placeholder_text=reference[0],
                                           font=theme['font']['subtitle'])
            save_button = ctk.CTkButton(reference_frame, text="Save",
                                        command=lambda: save_reference(title=reference_title.get(),
                                                                       link=reference_link.get()))
            save_button.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.RIGHT)
            remove_button = ctk.CTkButton(reference_frame, text="Remove",
                                          command=lambda: remove_reference(title=reference_title.get(),
                                                                           link=reference_link.get()))
            remove_button.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.RIGHT)
<<<<<<< HEAD
            visit_button = ctk.CTkButton(reference_frame, text="Save",
=======
            visit_button = ctk.CTkButton(reference_frame, text="Visit",
>>>>>>> 2b7be910f8dba4fa842ad7415db4844ba8062aa2
                                         command=lambda: visit_reference(link=reference_link.get()))
            visit_button.pack(padx=theme['pad'][1], pady=theme['pad'][1], side=ctk.RIGHT)
            reference_title.pack(padx=theme['pad'][1], pady=(theme['pad'][1], 0), side=ctk.LEFT, anchor=ctk.W,
                                 fill=ctk.X)
        self.user_frame.pack(padx=theme['pad'][2], pady=(0, theme['pad'][2]), fill=ctk.BOTH)
