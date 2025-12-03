import tkinter
import random
from PIL import Image, ImageTk

# init Tkinter window
tk = tkinter.Tk()

# configure window
tk.attributes("-fullscreen", True)
tk.attributes("-topmost", True)
tk.attributes("-transparentcolor", "black")

# create canvas and load spider image
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
canvas = tkinter.Canvas(tk, width=width, height=height, bg="black", highlightthickness=0)
canvas.pack()

# load spider image
img = Image.open("spider.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)


# function to add spiders at random positions
def add_spider():
    x = random.randint(0, width)
    y = random.randint(0, height)
    canvas.create_image(x, y, image=img)
    tk.after(500, add_spider)


# tk.protocol("WM_DELETE_WINDOW", lambda: None)  # disable close button
add_spider()
tk.mainloop()
