from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkLabel

class CTkInputBox(CTkFrame):
    def __init__(self, parent, *args,
                 width: int = 100,
                 height: int = 32,
                 text = "Placeholder Text",
                 placeholder_text="",
                 ok_command=None,
                 cancel_command=None,
                 **kwargs):
        super().__init__(parent, *args, width=width, height=height, **kwargs)

        self.configure(fg_color="#202020")

        self.text = text
        self.placeholder_text = placeholder_text
        self.ok_command = ok_command
        self.cancel_command = cancel_command
        self.current_input = None

        self.grid_rowconfigure((0, 4), weight=1)
        self.grid_columnconfigure((0, 4), weight=1)

        self.input_label = CTkLabel(self, text=self.text, font=("Verdana", 14, "bold"))
        self.input_label.grid(row=1, column=1, columnspan=3, sticky="ew")

        self.input_field = CTkEntry(self, placeholder_text=self.placeholder_text)
        self.input_field.grid(row=2, column=1, columnspan=3, padx=10, pady=10, stick="ew")

        self.ok_button = CTkButton(self, text="Ok", command=self.ok_button_callback)
        self.ok_button.grid(row=3, column=1, padx=10, pady=10)

        self.cancel_button = CTkButton(self, text="Cancel", command=self.cancel_button_callback)
        self.cancel_button.grid(row=3, column=3, padx=10, pady=10)

    def get_input(self):
        return self.current_input

    def ok_button_callback(self):
        self.current_input = self.input_field.get()
        if self.ok_command is not None:
            self.ok_command()
        self.input_field.delete(0, "end")
        self.destroy()

    def cancel_button_callback(self):
        self.current_input = None
        if self.cancel_command is not None:
            self.cancel_command()
        self.input_field.delete(0, "end")
        self.destroy()

