from typing import Tuple
import customtkinter as ctk
import tkinter
class Quation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,border_width=2,border_color='white',width=700,height=400, **kwargs)
        qaution="who is prime minister of India"
        self.quation_label=ctk.CTkLabel(self,text=qaution,fg_color='white',text_color='black',width=500,height=200)
    def show(self):
        self.quation_label.grid(row=0,column=0,sticky='nesw',padx=20,pady=20)
        
class Round_Frame(ctk.CTkFrame,ctk.CTk):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.page_title=ctk.CTkLabel(self,text="STRAIGHT FORWARD\n ROUND-1",fg_color="transparent",font=('Garamond', 50),text_color="#00FF00")
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
    def show(self):
        self.quation_frame=Quation_Frame(self)
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.quation_frame.grid(row=1, column=0, padx=20, pady=20)
        self.quation_frame.show()
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.grid_columnconfigure(0, weight=1) 
        self.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)