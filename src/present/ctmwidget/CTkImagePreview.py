from customtkinter import CTkFrame, CTkCanvas
from PIL import Image, ImageTk

class ImagePreview(CTkFrame):
    def __init__(self, master, image_path):
        CTkFrame.__init__(self, master)
        self.master = master

        self.configure(fg_color='#202020')

        # Load the image using PIL
        self.image = Image.open(image_path)
        self.image.thumbnail((200, 200))  # Limit the maximum size for autoscale

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas = CTkCanvas(self, width=self.image.width, height=self.image.height, bd=0,
                                bg="#202020", highlightthickness=0)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
        self.canvas.pack()

        # Enable autoscale on window resize
        self.bind("<Configure>", self.autoscale)

        # Enable zoom on mouse wheel scroll
        self.canvas.bind("<MouseWheel>", self.zoom)

    def autoscale(self, event):
        # Scale the image to fit within the canvas when the window is resized
        width = event.width
        height = event.height

        if width < self.image.width or height < self.image.height:
            self.image.thumbnail((width, height))
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.image.width, height=self.image.height)
            self.canvas.itemconfig(1, image=self.image_tk)

    def zoom(self, event):
        # Zoom the image based on the mouse wheel scroll
        if event.delta > 0:  # Zoom in
            factor = 1.2
        else:  # Zoom out
            factor = 0.8

        new_width = int(self.image.width * factor)
        new_height = int(self.image.height * factor)
        self.image = self.image.resize((new_width, new_height))
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.itemconfig(1, image=self.image_tk)

    def update_image(self, image_path):
        self.image = Image.open(image_path)
        self.image.thumbnail((200, 200))

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.config(width=self.image.width, height=self.image.height)
        self.canvas.itemconfig(1, image=self.image_tk)
