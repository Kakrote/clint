import customtkinter as ctk
import tkinter
from frames.login_frame import LoginFrame
class MainPanel(ctk.CTkFrame):
    loginframe=None
    def setActiveFrame(self,frame):
        app.mainpanel.activeframe.grid_forget()
        app.mainpanel.activeframe=frame
        app.mainpanel.activeframe.show()
    def __init__(self,master,**kwargs):
        super().__init__(master=master,fg_color="#00FF00",**kwargs)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.loginframe=LoginFrame(self)
        self.activeframe=self.loginframe
    def show(self):
        self.activeframe.show()
        self.pack(fill=tkinter.BOTH, expand=True,padx=20,pady=20)  # Fills and expands to center


class Clint_App(ctk.CTk):
    hight,width=400,800
    def __init__(self, **kwargs):
        super().__init__(fg_color=None, **kwargs)
        self.geometry(f'{self.width}x{self.hight}')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.mainpanel=MainPanel(self)
    def show(self):
        self.mainpanel.show()
        self.mainloop()
app=None
if __name__=="__main__":
    app=Clint_App()
    app.show()
