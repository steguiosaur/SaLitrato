from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkButton
from PIL import Image

from .ctmwidget import CTkList
from utils import Assets

class HomePage(CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkFrame.__init__(self, parent)

        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure((1, 2 ,3), weight=1)

        self.sidebar_frame = CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)

        self.logo_image = CTkImage(
            light_image=Image.open(Assets.asset_path("./salitrato.png")),
            dark_image=Image.open(Assets.asset_path("./salitrato_light.png")),
            size=(200, 49))
        self.logo_img_label=CTkLabel(self.sidebar_frame, image=self.logo_image, text="")
        self.logo_img_label.grid(row=0, column=0, padx=25, pady=25)

        self.open_folder_button = CTkButton(self.sidebar_frame,
            text="OPEN",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 16, "bold"),
            command=lambda: print("folder open"))
        self.open_folder_button.grid(row=1, column=0, sticky="we")

        self.add_folder_button = CTkButton(self.sidebar_frame,
            text="ADD FOLDER",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 16, "bold"),
            command=lambda: print("add folder"))
        self.add_folder_button.grid(row=2, column=0, sticky="we")

        self.remove_folder_button = CTkButton(self.sidebar_frame,
            text="REMOVE FOLDER",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 16, "bold"),
            command=lambda: print("remove folder"))
        self.remove_folder_button.grid(row=3, column=0, sticky="we")

        self.folder_frame = CTkFrame(self, fg_color="#202020")
        self.folder_frame.grid(row=1, column=1, rowspan=3, columnspan=4, padx=75, pady=75, sticky="nsew")
        self.folder_frame.grid_rowconfigure(0, weight=0)
        self.folder_frame.grid_rowconfigure(1, weight=1)
        self.folder_frame.grid_columnconfigure(0, weight=1)

        self.folder_label = CTkLabel(self.folder_frame, text=" Folder List", font=("Verdana", 16, "bold"))
        self.folder_label.grid(row=0, column=0, padx=30, pady=15, sticky="w")

        self.folder_list = CTkList(self.folder_frame)
        self.folder_list.grid(row=1, column=0, padx=(40, 30), pady=(0, 30), sticky="nsew")
