from customtkinter import CTkFrame, CTkScrollbar
from tkinter import Listbox, SINGLE

class CTkList(CTkFrame):
    def __init__(self, parent, theme="dark", selectmode=SINGLE, command=None, xscroll=False,
                 font_size=11, **kwargs):
        super().__init__(parent, **kwargs)

        self.theme = theme
        self.selectmode = selectmode
        self.command = command
        self.xscroll = xscroll
        self.font_size = font_size

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.list_box = Listbox(self,
            selectmode=self.selectmode,
            highlightthickness=0,
            relief="flat",
            bd=0,
            font=("Verdana", self.font_size))
        self.list_style(self.theme)
        self.list_box.grid(row=0, column=0, sticky="nsew")

        self.yScroll = CTkScrollbar(self, orientation="vertical")
        self.yScroll.configure(command=self.list_box.yview)
        self.yScroll.grid(row=0, column=1, sticky="ns")
        self.list_box.configure(yscrollcommand=self.yScroll.set)

        if self.xscroll:
            self.xScroll = CTkScrollbar(self, orientation="horizontal")
            self.xScroll.configure(command=self.list_box.xview)
            self.xScroll.grid(row=1, column=0, sticky="ew")
            self.list_box.configure(xscrollcommand=self.xScroll.set)

    def listbox_instance(self):
        return self.list_box

    def insert(self, index, text):
        return self.list_box.insert(index, text)

    def delete(self, first, last):
        return self.list_box.delete(first, last)

    def change_theme(self, new_theme):
        self.theme = new_theme

    def list_style(self, list_theme):
        if list_theme == "dark":
            self.list_box.configure(
                bg='#202020',
                fg='#e1e1e1',
                selectbackground='#e1e1e1',
                selectforeground='#202020',
                highlightcolor='#202020')
        if list_theme == "light":
            self.list_box.configure(
                bg='#e1e1e1',
                fg='#202020',
                selectbackground='#202020',
                selectforeground='#e1e1e1',
                highlightcolor='#e1e1e1')

    def get_selected_text(self):
        # Get the index of the selected item
        selected_index = self.list_box.curselection()
        if selected_index:
            # Retrieve the text at the selected index
            selected_text = self.list_box.get(selected_index[0])
            return(selected_text)

    def remove_selected_text(self):
        selected_index = self.list_box.curselection()
        if selected_index:
            self.list_box.delete(selected_index)

    def configure(self, **kwargs):
        if 'command' in kwargs:
            self.command = kwargs['command']
