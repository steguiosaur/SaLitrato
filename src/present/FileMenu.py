from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkProgressBar, END

from functions import FileMenuFunc
from .ctmwidget import CTkListPage, ImagePreview
from utils import file_opts

class FileMenu(CTkListPage, FileMenuFunc):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkListPage.__init__(self, parent)

        # Bind the list box selection event to the command
        self.list_list.listbox_instance().bind('<<ListboxSelect>>', lambda event: self.update_image_by_cursorlist(event))

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

        self.image_view_frame = CTkFrame(self.sidebar_frame)
        self.image_view_frame.grid(row=4, column=0, rowspan=3, pady=10, sticky="")
        self.image_view_frame.rowconfigure(0, weight=1)
        self.image_view_frame.rowconfigure(1, weight=0)
        self.image_view_frame.columnconfigure(0, weight=1)

        self.image_view_label = CTkLabel(self.image_view_frame, text="Image View", font=("Verdana", 12, "bold"))
        self.image_view_label.grid(row=0, column=0, sticky="ew")

        self.image_view = ImagePreview(self.image_view_frame, image_path=self.read_cursor_filepath())
        self.image_view.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

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

    def update_image_by_cursorlist(self, event):
        selection = self.list_list.listbox_instance().curselection()
        if selection:
            selected_index = selection[0]
            selected_value = self.list_list.listbox_instance().get(selected_index)
            image_path = self.get_file_path_event(self.controller.get_cur_folder(), selected_value)
            self.image_view.update_image(image_path)

    def read_cursor_filepath(self):
        return self.get_file_path_event(self.controller.get_cur_folder(), self.list_list.get_selected_text())

    def start_search_command(self, controller):
        if hasattr(self, "add_image_command") and hasattr(self, "progressbar") and self.progressbar.winfo_exists():
            return
        self.focus_set()
        controller.show_frame("Previewer", controller.id)

    def add_image_command(self):
        self.progressbar = CTkProgressBar(self.list_frame, orientation="horizontal", mode="indeterminate")
        self.progressbar.grid(row=4, column=0, rowspan=4, sticky="ew")
        self.progressbar.start()
        self.add_file_event(self.controller.get_cur_folder())
        self.refresh_file_list()
        self.progressbar.stop()
        self.progressbar.destroy()

    def remove_image_command(self):
        self.remove_file_event(self.controller.get_cur_folder(), self.list_list.get_selected_text())
        self.list_list.remove_selected_text()

    def return_home_command(self, controller):
        if hasattr(self, "add_image_command") and hasattr(self, "progressbar") and self.progressbar.winfo_exists():
            return
        self.image_view.update_image(self.get_file_path_event(None, None))
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
