from tkinter import END
from customtkinter import CTkButton

from functions import FileMenuFunc
from .ctmwidget import CTkListPage
from utils import file_opts

class FileMenu(CTkListPage, FileMenuFunc):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkListPage.__init__(self, parent)

        self.start_button = CTkButton(self.sidebar_frame,
            text="       START SEARCH",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda: self.start_search_command(controller))
        self.start_button.grid(row=1, column=0, sticky="we")

        self.add_image_button = CTkButton(self.sidebar_frame,
            text="       ADD IMAGE",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda: self.add_image_command())
        self.add_image_button.grid(row=2, column=0, sticky="we")

        self.remove_image_button = CTkButton(self.sidebar_frame,
            text="       REMOVE IMAGE",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda: self.remove_image_command())
        self.remove_image_button.grid(row=3, column=0, sticky="we")

        self.back_button = CTkButton(self.sidebar_frame,
            text="       BACK",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda:self.return_home_command(controller))
        self.back_button.grid(row=7, column=0, sticky="swe")

    def read_current_folder(self, text: str):
        self.list_label_text("Folder: " + text + "/")

    def start_search_command(self, controller):
        controller.show_frame("Previewer", controller.id)

    def add_image_command(self):
        self.add_file_event(self.controller.get_cur_folder())
        self.refresh_file_list()

    def remove_image_command(self):
        pass

    def return_home_command(self, controller):
        controller.show_frame("HomePage", controller.id)
        self.controller.set_cur_folder(None)

    def refresh_file_list(self):
        self.list_list.delete(0, END)
        file_data_array = file_opts.get_all_imgfiles(self.controller.get_cur_folder())
        if file_data_array is not None:
            file_data_array.sort()
            for file_data in file_data_array:
                file_key, file_name = file_data
                self.list_list.insert(file_key, file_name)
