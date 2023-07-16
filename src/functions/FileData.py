from utils import boyer, text_process

class FileData():
    def __init__(self):
        self.current_folder = None
        self.data = None
        self.bad_character = None
        self.result = None
        self.current_file = None

    def set_current_file(self, file):
        self.current_file = file

    def get_current_file(self):
        return self.current_file

    def reset_data(self):
        self.data = None
        self.result = None
        self.bad_character = None
        self.current_folder = None

    def set_current_folder(self, current_folder):
        self.current_folder = current_folder

    def set_data_for_process(self):
        self.data = text_process.process_csv_and_text(self.current_folder)

    def set_match_result(self, pattern):
        self.result = text_process.find_pattern_in_data(self.data, pattern, self.bad_character)

    def set_bad_character_pattern(self, pattern):
        self.bad_character = boyer.set_badchar_array(pattern)
