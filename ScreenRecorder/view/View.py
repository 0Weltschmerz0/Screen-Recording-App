import tkinter as Tk
from tkinter import Button, PhotoImage, OptionMenu, Entry, StringVar
from PIL import ImageTk


class View:

    def __init__(self, root, controller):
        self.frame = Tk.Frame(root)
        self.canvas = Tk.Canvas(width=900, height=600, background='#242424')
        self.canvas.create_rectangle(0, 455, 900, 600, fill='#504E4E')
        self.canvas.pack(fill="both", expand=False)
        start = PhotoImage(file = "resources/start.png")
        stop = PhotoImage(file="resources/stop.png")
        save = PhotoImage(file="resources/save.png")
        self.play_button = Button(root, bg="#504E4E", image=start, command=lambda: controller.start_recording())
        self.play_button.image = start
        self.play_button.place(height=50, width=50, x="20", y = "500")
        self.stop_button = Button(root, bg="#504E4E", image=stop, command=lambda: controller.stop_recording())
        self.stop_button.image = stop
        self.stop_button.place(height=50, width=50, x="100", y="500")
        self.save_button = Button(root, bg="#504E4E", image=save, command=lambda: controller.save_video())
        self.save_button.image = save
        self.save_button.place(height=50, width=50, x="180", y="500")
        self.screenshot_button = Button(root, bg="#504E4E", text="Screenshot", fg="white", command=lambda: controller.screenshot())
        self.screenshot_button.place(height=60, width=100, x="600", y="495")
        fill = StringVar()
        fill.set('1')
        self.timer = Entry(root, textvariable=fill)
        self.timer.place(height=30, width=80, x="720", y="510")

