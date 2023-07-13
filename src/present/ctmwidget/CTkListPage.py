from customtkinter import CTkFrame, CTkImage, CTkLabel
from PIL import Image

from utils import Assets
from .CTkList import CTkList

class CTkListPage(CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure((1, 2 ,3), weight=1)

        self.sidebar_frame = CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_image = CTkImage(
            light_image=Image.open(Assets.asset_path("./salitrato.png")),
            dark_image=Image.open(Assets.asset_path("./salitrato_light.png")),
            size=(200, 49))
        self.logo_img_label=CTkLabel(self.sidebar_frame, image=self.logo_image, text="")
        self.logo_img_label.grid(row=0, column=0, padx=25, pady=25)

        self.list_frame = CTkFrame(self, fg_color="#202020")
        self.list_frame.grid(row=1, column=1, rowspan=3, columnspan=4, padx=75, pady=75, sticky="nsew")
        self.list_frame.grid_rowconfigure(0, weight=0)
        self.list_frame.grid_rowconfigure(1, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)

        self.list_label = CTkLabel(self.list_frame, text="Placeholder List Title", font=("Verdana", 16, "bold"))
        self.list_label.grid(row=0, column=0, padx=30, pady=15, sticky="w")

        self.list_list = CTkList(self.list_frame)
        self.list_list.grid(row=1, column=0, padx=(40, 30), pady=(0, 30), sticky="nsew")

    def list_label_text(self, text: str):
        return self.list_label.configure(text=text)

    def insert(self, index, text):
        return self.list_list.insert(index, text)
