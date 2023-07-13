from customtkinter import CTkFrame, CTkScrollbar
from tkinter import ANCHOR, Listbox, SINGLE

class CTkList(CTkFrame):
    def __init__(self, parent, theme="dark", selectmode=SINGLE, **kwargs):
        super().__init__(parent, **kwargs)

        self.theme = theme
        self.selectmode = selectmode

        self.list_box = Listbox(self,
            selectmode=self.selectmode,
            highlightthickness=0,
            relief="flat",
            bd=0,
            font=("Source Code", 10))
        self.list_style(self.theme)
        self.list_box.pack(side='left', fill='both', expand=True)

        self.yScroll = CTkScrollbar(self, orientation="vertical")
        self.yScroll.configure(command=self.list_box.yview)
        self.yScroll.pack(side='right', fill='y', anchor="w")
        self.list_box.configure(yscrollcommand=self.yScroll.set)

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
