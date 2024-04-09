from typing import Any, Tuple
import customtkinter as ctk
import tkinter
from PIL import Image
class Quation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500, height=500, **kwargs)
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=2)
        # quation is here
        qaution="who is this persion shown in the image"
        # quation label
        self.quation_label=ctk.CTkLabel(self.desplay_quations,text=qaution,fg_color='white',text_color='black',width=500,height=200)
        # fiting the quation level into the quation frame 
        self.quation_label.pack(expand=True,padx=20,pady=20,fill=tkinter.BOTH)

        self.option_1=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        # option 1 lebel
        option1="Anshul"
        self.option_1_label=ctk.CTkLabel(self.option_1,text=option1,fg_color='black',text_color='white',height=100,width=200)
        #packing the option 1 into the frame option frame
        self.option_1_label.pack(expand=True,fill=tkinter.BOTH,padx=10,pady=10)

        self.option_2=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        # option 2 lebel
        option2="Abhay"
        self.option_2_label=ctk.CTkLabel(self.option_2,text=option2,fg_color='black',text_color='white',height=100,width=200)
        #packing the option 1 into the frame option frame
        self.option_2_label.pack(expand=True,fill=tkinter.BOTH,padx=10,pady=10)


        self.option_3=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        # option 3 lebel
        option3="Maghan"
        self.option_3_label=ctk.CTkLabel(self.option_3,text=option3,fg_color='black',text_color='white',height=100,width=200)
        #packing the option 1 into the frame option frame
        self.option_3_label.pack(expand=True,fill=tkinter.BOTH,padx=10,pady=10)

        self.option_4=ctk.CTkFrame(self,width=200,height=100,border_width=1,border_color='black')
        # option 4 lebel
        option4="Don"
        self.option_4_label=ctk.CTkLabel(self.option_4,text=option4,fg_color='black',text_color='white',height=100,width=200)
        #packing the option 1 into the frame option frame
        self.option_4_label.pack(expand=True,fill=tkinter.BOTH,padx=10,pady=10)

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
        x="roundtwoimage/test.png"
        img=ctk.CTkImage(Image.open(x),size=(50,50))
        self.image=ctk.CTkLabel(self,image=img,fg_color='white',text_color='black',width=400,height=500)
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