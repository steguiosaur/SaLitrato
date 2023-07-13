from customtkinter import CTkButton

from functions import FileMenuFunc
from .ctmwidget import CTkListPage

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
            command=lambda: print("goto preview"))
        self.start_button.grid(row=1, column=0, sticky="we")

        self.add_file_button = CTkButton(self.sidebar_frame,
            text="       ADD FILE",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda: print("add folder"))
        self.add_file_button.grid(row=2, column=0, sticky="we")

        self.remove_file_button = CTkButton(self.sidebar_frame,
            text="       REMOVE FILE",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda: print("remove file"))
        self.remove_file_button.grid(row=3, column=0, sticky="we")

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
        self.current_folder = text

    def start_search_command(self):
        pass

    def remove_file_command(self):
        pass

    def add_file_command(self):
        pass

    def return_home_command(self, controller):
        controller.show_frame("HomePage", controller.id)
