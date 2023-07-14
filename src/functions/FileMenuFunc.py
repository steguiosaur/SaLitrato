from utils import file_opts

class FileMenuFunc():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.current_folder = None

    def add_file_event(self, current_folder):
        file_opts.get_path_image(current_folder)

    def remove_file_event(self):
        pass
