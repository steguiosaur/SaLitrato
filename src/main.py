from customtkinter import CTkFrame, set_appearance_mode
from tkinter import PhotoImage, Tk

from utils import Assets
from present import *

class Main(Tk):
    def __init__(self):
        super().__init__()

        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in [HomePage]:
            page = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page] = frame

        self.show_frame

    def show_frame(self, page, id=None):
        self.id = id
        self.frames[page].tkraise()


set_appearance_mode("Dark")

app = Main()
app.title("SaLitrato")
app.resizable(True, True)
width = 1024
height = 576
x = (app.winfo_screenwidth()/2) - width/2
y = (app.winfo_screenheight()/2) - height/2
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.minsize(1024, 576)
app.iconphoto(True, PhotoImage(file=Assets.asset_path('salitrato_icon.png')))
app.mainloop()