from tkinter import END
from customtkinter import CTkButton

from .ctmwidget import CTkListPage, CTkInputBox
from functions import HomePageFunc
from utils import folder_opts

class HomePage(CTkListPage, HomePageFunc):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkListPage.__init__(self, parent)

        self.list_label_text("Folder List")
        self.refresh_folder_list()

        self.open_folder_button = CTkButton(self.sidebar_frame,
            text="       OPEN",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda:self.open_folder_command(controller))
        self.open_folder_button.grid(row=1, column=0, sticky="we")

        self.add_folder_button = CTkButton(self.sidebar_frame,
            text="       CREATE FOLDER",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda:self.add_folder_command())
        self.add_folder_button.grid(row=2, column=0, sticky="we")

        self.remove_folder_button = CTkButton(self.sidebar_frame,
            text="       REMOVE FOLDER",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda:self.remove_folder_command())
        self.remove_folder_button.grid(row=3, column=0, sticky="we")

        self.exit_button = CTkButton(self.sidebar_frame,
            text="       EXIT",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            anchor="w",
            font=("Verdana", 14, "bold"),
            command=lambda: print("exit function"))
        self.exit_button.grid(row=7, column=0, sticky="swe")

    def refresh_folder_list(self):
        self.list_list.delete(0, END)
        for folder in folder_opts.get_folders():
            self.list_list.insert(END, folder)

    def remove_folder_command(self):
        self.remove_folder_event(self.list_list.get_selected_text())
        self.list_list.remove_selected_text()

    def create_folder_callback(self, folder_name):
        self.add_folder_event(folder_name)
        self.refresh_folder_list()

    def add_folder_command(self):
        if hasattr(self, "add_folder_dialog") and self.add_folder_dialog.winfo_exists():
            return
        self.add_folder_dialog = CTkInputBox(self.list_frame, text="Create Folder", corner_radius=5,
            ok_command=lambda: self.create_folder_callback(self.add_folder_dialog.get_input()))
        self.add_folder_dialog.grid(row=0, column=0, rowspan=2, columnspan=1, sticky="nsew")

    def open_folder_command(self, controller):
        if self.list_list.get_selected_text() is not None:
            self.controller.frames["FileMenu"].read_current_folder(self.list_list.get_selected_text())
            controller.show_frame("FileMenu", controller.id)
