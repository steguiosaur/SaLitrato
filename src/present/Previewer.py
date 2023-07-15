from customtkinter import CTkFrame, CTkEntry, CTkImage, CTkLabel, CTkButton, CTkTextbox
from PIL import Image

from utils import Assets, file_opts
from .ctmwidget import CTkList, ImagePreview

class Previewer(CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkFrame.__init__(self, parent)

        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure((1, 2 ,3), weight=1)

        self.sidebar_frame = CTkFrame(self, width=200, corner_radius=0, fg_color='#202020')
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3), weight=0)
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_image = CTkImage(
            light_image=Image.open(Assets.asset_path("./salitrato.png")),
            dark_image=Image.open(Assets.asset_path("./salitrato_light.png")),
            size=(200, 49))
        self.logo_img_label=CTkLabel(self.sidebar_frame, image=self.logo_image, text="")
        self.logo_img_label.grid(row=0, column=0, padx=25, pady=25)

        self.search_entry = CTkEntry(self.sidebar_frame, placeholder_text="Search pattern")
        self.search_entry.grid(row=1, column=0, padx=25, pady=(0, 15), sticky="ew")

        self.position_list = CTkList(self.sidebar_frame)
        self.position_list.grid(row=2, column=0, rowspan=5, padx=(10, 0), sticky="nsew")
        self.listbox = self.position_list.listbox_instance()
        self.listbox.bind('<<ListboxSelect>>', lambda event: self.position_list_selected(event))

        self.back_button = CTkButton(self.sidebar_frame,
            text="       BACK",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda:self.return_filemenu_command(controller))
        self.back_button.grid(row=7, column=0, sticky="swe")

        self.image_preview_frame = CTkFrame(self)
        self.image_preview_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=15, pady=15, sticky="nsew")
        self.image_preview_frame.rowconfigure(0, weight=1)
        self.image_preview_frame.columnconfigure(0, weight=1)

        self.image_view = ImagePreview(self.image_preview_frame, image_path=self.read_cursor_filepath())
        self.image_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.image_info_frame = CTkFrame(self)
        self.image_info_frame.grid(row=0, column=4, rowspan=3, padx=(0, 15), pady=15, sticky="nsew")

        self.text_preview_frame = CTkTextbox(self)
        self.text_preview_frame.grid(row=3, column=1, rowspan=1, columnspan=4, padx=15, pady=(0, 15), sticky="nsew")

    def return_filemenu_command(self, controller):
        controller.show_frame("FileMenu", controller.id)

    def position_list_selected(self, event):
        print("list presss")
        pass

    def read_cursor_filepath(self):
        return file_opts.get_file_path_from_csv(None, None)
