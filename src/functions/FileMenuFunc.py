from utils import file_opts

class FileMenuFunc():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_file_event(self, current_folder):
        file_opts.get_path_image(current_folder)

    def remove_file_event(self, current_dir, img_name):
        file_opts.delete_row_by_key(current_dir, img_name)

    def get_file_path_event(self, current_dir, img_name):
        return file_opts.get_file_path_from_csv(current_dir, img_name)
