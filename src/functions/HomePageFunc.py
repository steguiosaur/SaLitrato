from customtkinter import CTkInputDialog

from utils import folder_opts

class HomePageFunc():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_folder_dialog_event(self):
        self.add_folder_dialog = CTkInputDialog(text="Create Folder", title="Salitrato - Create Folder")
        folder_opts.create_subfolder(self.add_folder_dialog.get_input())

    def remove_folder_event(self, folder_name):
        if folder_name is not None:
            folder_opts.delete_subfolder(folder_name)
