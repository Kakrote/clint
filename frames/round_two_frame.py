from typing import Any, Tuple
import customtkinter as ctk
import tkinter
class Quation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500, height=500, **kwargs)
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=2)
        self.option_1=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        self.option_2=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        self.option_3=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        self.option_4=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
    def show(self):
        self.desplay_quations.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)
        self.option_1.grid(row=1,column=0,padx=10,pady=10,sticky='nw')
        self.option_2.grid(row=1,column=1,padx=10,pady=10,sticky='ne')
        self.option_3.grid(row=2,column=0,padx=10,pady=10,sticky='nw')
        self.option_4.grid(row=2,column=1,padx=10,pady=10,sticky='ne')
    
class Round_Two(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        #adding title to the page
        self.page_title=ctk.CTkLabel(self,text="BUJHO TO JANO\n ROUND-2",fg_color="transparent",font=('Garamond', 50),text_color="#00FF00")
        # adding logo label
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        # adding timer label
        self.timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')
        # adding image for the quation in the frame
        self.image=ctk.CTkLabel(self,text='Image will be display here',fg_color='white',text_color='black',width=400,height=500)
    def show(self):
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.image.grid(row=1,column=0,sticky='nw',padx=40,pady=20)
        self.quation_frame=Quation_Frame(self)
        self.quation_frame.grid(row=1,column=0,sticky='ne',padx=40,pady=20)
        self.quation_frame.show()
        self.grid_columnconfigure(0, weight=1) 
        self.pack( fill=tkinter.BOTH,expand=True, padx=20, pady=20)