from customtkinter import CTkFrame, CTkLabel, CTkImage
from PIL import Image

from utils import Assets

class HomePage(CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkFrame.__init__(self, parent)

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2 ,3), weight=1)

        self.logo_image = CTkImage(
            light_image=Image.open(Assets.asset_path("./salitrato.png")),
            dark_image=Image.open(Assets.asset_path("./salitrato.png")),
            size=(411, 100))
        self.logo_img_label=CTkLabel(self, image=self.logo_image, text="")
        self.logo_img_label.grid(row=0, column=1, columnspan=2)

        self.folder_frame = CTkFrame(self, width=160, corner_radius=0)
        self.folder_frame.grid(row=1, column=0, rowspan=3, columnspan=4, padx=10, pady=10 ,sticky="nsew")
        self.folder_frame.grid_rowconfigure((1, 2, 3), weight=1)
        self.folder_frame.grid_columnconfigure((1, 2, 3), weight=1)
