# login panel
from typing import Any, Tuple
import tkinter
import customtkinter as ctk
class Entery(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='green', **kwargs)
        self.userid = ctk.CTkLabel(self, text="UserID", font=('Helvetica', 10), text_color='#DAA520')
        self.e_userid = ctk.CTkEntry(self, placeholder_text="Enter the #id", font=('Helvetica', 10), text_color='black')

    def show(self):
        self.userid.grid(row=0, column=0, padx=20, pady=20, sticky='we')
        self.e_userid.grid(row=0, column=1, padx=20, pady=20, sticky='we')
        self.pack()

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='white', **kwargs)
        self.title_page = ctk.CTkLabel(self, text="Login", fg_color='transparent', font=('Garamond', 50), text_color='#00FF00')
        self.entry = Entery(self)

    def show(self):
        self.title_page.grid(row=0, column=0, sticky='nsew')  # Top row, centered

        # Center the Entery class within LoginFrame using grid
        self.entry.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        # Configure LoginFrame's grid to allow centering
        self.grid_columnconfigure(0, weight=1)  # Make the single column flexible

        # Use `pack` to fill remaining space (optional for padding)
        self.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)  # Optional for padding


