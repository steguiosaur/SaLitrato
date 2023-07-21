from customtkinter import END, CTkFrame, CTkEntry, CTkImage, CTkLabel, CTkButton, CTkTextbox
from PIL import Image

from functions import FileData
from utils import Assets, file_opts, text_process
from .ctmwidget import CTkList, ImagePreview

class Previewer(CTkFrame, FileData):
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
            light_image=Image.open(Assets.asset_path("./salitrato_white.png")),
            dark_image=Image.open(Assets.asset_path("./salitrato_white.png")),
            size=(200, 42))
        self.logo_img_label=CTkLabel(self.sidebar_frame, image=self.logo_image, text="")
        self.logo_img_label.grid(row=0, column=0, padx=25, pady=25)

        self.search_entry = CTkEntry(self.sidebar_frame, placeholder_text="Search pattern")
        self.search_entry.grid(row=1, column=0, padx=25, pady=(0, 15), sticky="ew")
        self.search_entry.bind("<KeyRelease>", lambda event: self.search_entry_changed(event))

        self.position_list = CTkList(self.sidebar_frame, xscroll=True, font_size=9)
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

        self.image_preview_frame = CTkFrame(self, fg_color='#202020')
        self.image_preview_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=15, pady=15, sticky="nsew")
        self.image_preview_frame.rowconfigure((0, 1, 2), weight=1)
        self.image_preview_frame.columnconfigure((0, 1, 2), weight=1)
        self.image_preview_frame.grid_propagate(False)

        self.image_view = ImagePreview(self.image_preview_frame,
                                       image_path=self.get_image_path(None), res=(1000, 1000))
        self.image_view.grid(row=1, column=1, padx=10, pady=10, sticky="news")

        self.image_info_frame = CTkFrame(self)
        self.image_info_frame.grid(row=0, column=4, rowspan=3, padx=(0, 15), pady=15, sticky="nsew")
        self.image_info_frame.columnconfigure((0, 2), weight=1)
        self.image_info_frame.grid_propagate(False)

        self.folder_label = CTkLabel(self.image_info_frame, text="Folder_Name", font=("Verdana", 16, "bold"))
        self.folder_label.grid(row=0, column=1, padx=15, pady=15, sticky="ew")

        self.filename_label = CTkLabel(self.image_info_frame, text="", font=("Verdana", 11, "bold"))
        self.filename_label.grid(row=1, column=1, padx=5, pady=5, sticky="")

        self.row_label = CTkLabel(self.image_info_frame, text="Row", font=("Verdana", 11, "bold"))
        self.row_label.grid(row=2, column=1, padx=5, pady=(5, 0), sticky="ew")

        self.row_count_label = CTkLabel(self.image_info_frame, text="N/A", font=("Verdana", 25, "bold"))
        self.row_count_label.grid(row=3, column=1, padx=5, pady=(2, 5), sticky="ew")

        self.col_label = CTkLabel(self.image_info_frame, text="Column", font=("Verdana", 11, "bold"))
        self.col_label.grid(row=4, column=1, padx=5, pady=(5, 0), sticky="ew")

        self.col_count_label = CTkLabel(self.image_info_frame, text="N/A", font=("Verdana", 25, "bold"))
        self.col_count_label.grid(row=5, column=1, padx=5, pady=(2, 5), sticky="ew")

        self.text_preview = CTkTextbox(self)
        self.text_preview.grid(row=3, column=1, rowspan=1, columnspan=4, padx=15, pady=(0, 15), sticky="nsew")

    def read_current_folder(self, text: str):
        if len(text) > 18:
            text = text[:18-3] + "..."
        self.folder_label.configure(text= text + "/")

    def get_image_path(self, filename):
        return file_opts.get_file_path_from_csv(self.controller.get_cur_folder(), filename)

    def return_filemenu_command(self, controller):
        self.focus_set()
        controller.show_frame("FileMenu", controller.id)
        self.position_list.delete(0, END)
        self.search_entry.delete(0, END)
        self.text_preview.delete("1.0", "end")
        self.image_view.update_image(self.get_image_path(None))
        self.filename_label.configure(text="")
        self.row_count_label.configure(text="N/A")
        self.col_count_label.configure(text="N/A")
        self.reset_data()

    def position_list_selected(self, event):
        selection = self.listbox.curselection()
        if selection:
            key = self.item_key_map.get(int(selection[0]))
            if key:
                filename, row, index = key
                self.load_text_file(filename)
                self.image_view.update_image(self.get_image_path(filename))
                self.highlight_position(row, index)
                if len(filename) > 25:
                    filename = filename[:25-3] + "..."
                self.filename_label.configure(text=filename)
                self.row_count_label.configure(text=row+1)
                self.col_count_label.configure(text=index)

    def search_entry_changed(self, event):
        search_pattern = self.search_entry.get()
        self.position_list.delete(0, END)
        self.text_preview.delete("1.0", "end")
        self.image_view.update_image(self.get_image_path(None))
        self.filename_label.configure(text="")
        self.row_count_label.configure(text="N/A")
        self.col_count_label.configure(text="N/A")
        if search_pattern:
            self.set_bad_character_pattern(search_pattern)
            self.set_match_result(search_pattern)
            self.refresh_position_list()
            self.listbox.selection_set('0')
            self.position_list_selected(event)

    def load_data_structure(self):
        self.set_data_for_process()

    def refresh_position_list(self):
        self.item_key_map = {}  # Map item index to key
        if self.result is not None and self.data is not None:
            item_index = 0
            for filename, matched_rows in self.result.items():
                for row, indexes in matched_rows.items():
                    for index in indexes:
                        row_text = self.data[filename][row]
                        if len(row_text) > 100:
                            row_text = row_text[:100-3] + "..."
                        item = f"{filename}:{row+1}:{index}: -> {row_text}"
                        self.position_list.insert(END, item)
                        self.item_key_map[item_index] = (filename, row, index)
                        item_index += 1
        if self.result == {}:
            self.position_list.insert(END, 'Nothing to see here.')

    def load_text_file(self, filename):
        contents = text_process.get_text_in_txt(self.current_folder, filename)
        try:
            self.text_preview.delete("1.0", "end")
            self.text_preview.insert("1.0", contents)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    def highlight_position(self, row, column):
        start_index = f"{row + 1}.{column}"
        end_index = f"{row + 1}.{column + len(self.search_entry.get())}"
        self.text_preview.tag_config("highlight", background="#e1e1e1", foreground="#202020")
        self.text_preview.tag_add("highlight", start_index, end_index)
        self.text_preview.see(start_index)
