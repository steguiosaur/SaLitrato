from customtkinter import CTkFrame, CTkCanvas
from PIL import Image, ImageTk

class ImagePreview(CTkFrame):
    def __init__(self, master, image_path, res=(200, 200)):
        CTkFrame.__init__(self, master)
        self.master = master

        self.configure(fg_color='#202020')
        self.res = res

        # Load the image using PIL
        self.image = Image.open(image_path)
        self.image.thumbnail(self.res)  # Limit the maximum size for autoscale

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas = CTkCanvas(self, width=self.res[0], height=self.res[1], bd=0,
                                bg="#202020", highlightthickness=0)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
        self.canvas.pack()

        # Enable autoscale on window resize
        self.bind("<Configure>", self.autoscale)

        # Enable zoom on mouse wheel scroll
        self.canvas.bind("<MouseWheel>", self.zoom)

    def autoscale(self, event):
        # Scale the image to fit within the canvas while maintaining aspect ratio
        width = event.width
        height = event.height

        aspect_ratio = self.image.width / self.image.height
        canvas_ratio = width / height

        if canvas_ratio > aspect_ratio:
            new_width = int(height * aspect_ratio)
            new_height = height
        else:
            new_width = width
            new_height = int(width / aspect_ratio)

        self.image_tk = ImageTk.PhotoImage(self.image.resize((new_width, new_height)))
        self.canvas.config(width=new_width, height=new_height)
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
        self.image.thumbnail(self.res)

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.config(width=self.res[0], height=self.res[1])
        self.canvas.itemconfig(1, image=self.image_tk)

