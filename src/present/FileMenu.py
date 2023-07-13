from customtkinter import CTkButton

from .ctmwidget import CTkListPage

class FileMenu(CTkListPage):
    def __init__(self, parent, controller):
        self.controller = controller
        CTkListPage.__init__(self, parent)

        self.list_label_text("Replace with current folder")

        self.start_button = CTkButton(self.sidebar_frame,
            text="START SEARCH",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 14, "bold"),
            command=lambda: print("goto preview"))
        self.start_button.grid(row=1, column=0, sticky="we")

        self.add_file_button = CTkButton(self.sidebar_frame,
            text="ADD FILE",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 14, "bold"),
            command=lambda: print("add folder"))
        self.add_file_button.grid(row=2, column=0, sticky="we")

        self.remove_file_button = CTkButton(self.sidebar_frame,
            text="REMOVE FILE",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 14, "bold"),
            command=lambda: print("remove file"))
        self.remove_file_button.grid(row=3, column=0, sticky="we")

        self.back_button = CTkButton(self.sidebar_frame,
            text="EXIT",
            corner_radius=0,
            height=50,
            fg_color="#202020",
            font=("Verdana", 14, "bold"),
            command=lambda: print("goto homepage function"))
        self.back_button.grid(row=7, column=0, sticky="swe")

        self.insert(1, "File 1")

