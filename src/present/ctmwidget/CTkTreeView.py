from customtkinter import CTkFrame, CTkScrollbar
from tkinter import ttk

class CTkTreeView(CTkFrame):
    def __init__(self, parent, theme="light", **kwargs):
        super().__init__(parent, **kwargs)

        # input table style
        self.theme = theme

        self.style = ttk.Style()
        # light/default theme
        self.style.configure(
            "lightAppearance.Treeview",
            highlightthickness=0,
            bd=0,
            relief="flat",
            rowheight="20",
            borderwidth=0,
            background="#e1e1e1",
            foreground="#202020")
        self.style.configure(
            "lightAppearance.Treeview.Heading",
            borderwidth=0,
            relief="flat",
            font=("Roboto", 9, "bold"),
            background="#b1b1b1",
            foreground="#202020")

        # dark theme
        self.style.configure(
            "darkAppearance.Treeview",
            highlightthickness=0,
            bd=0,
            rowheight="20",
            relief="flat",
            borderwidth=0,
            background="#282828",
            foreground="#d1d1d1")
        self.style.configure(
            "darkAppearance.Treeview.Heading",
            borderwidth=1,
            relief="flat",
            font=("Roboto", 9, "bold"),
            background="#202020",
            foreground="#d1d1d1")
        self.style.layout("lightAppearance.Treeview", [('light Appearance.Treeview.treearea', {'sticky': 'nsew'})])
        self.style.layout("darkAppearance.Treeview", [('light Appearance.Treeview.treearea', {'sticky': 'nsew'})])

        # create product table
        self.treeView = ttk.Treeview(self, selectmode='extended')
        self.table_style(self.theme)

        # create scroll on table
        self.yScroll = CTkScrollbar(self, orientation="vertical")
        self.yScroll.configure(command=self.treeView.yview)
        self.yScroll.pack(side='right', fill='y', anchor="w")
        self.treeView.configure(yscrollcommand=self.yScroll.set)
        self.treeView.pack(side='right', fill='both', expand=True)


    def change_theme(self, new_theme):
        self.theme = new_theme
        self.table_style(self.theme)

    def get_treeview(self):
        return self.treeView

    def table_style(self, table_theme):
        if table_theme == "dark":
            self.treeView["style"] = "darkAppearance.Treeview"
        if table_theme == "light":
            self.treeView["style"] = "lightAppearance.Treeview"
