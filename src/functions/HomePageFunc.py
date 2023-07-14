from utils import folder_opts

class HomePageFunc():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_folder_event(self, folder_name):
        folder_opts.create_subfolder(folder_name)

    def remove_folder_event(self, folder_name):
        if folder_name is not None:
            folder_opts.delete_subfolder(folder_name)
