import tkinter as Tk
from tkinter import filedialog
from View import View
from Video import Video
from Capturer import Capturer
import ntpath
import cv2


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.view = View(self.root, self)
        self.video_model = Video()
        self.user_input = ''
        self.recording = False
        self.video_data = ''
        self.output = ''

    def run(self):
        self.root.title("Screen Recorder")
        self.root.deiconify()
        self.root.resizable(0, 0)
        self.root.geometry("900x600")
        while True:
            Capturer.show_video(self.root, self.view.canvas)
            Capturer.record(self.recording, self.output)
        self.root.mainloop()

    def start_recording(self):

        self.video_data = filedialog.asksaveasfilename(title="Select file", defaultextension="*.mp4",filetypes = (("MP4","*.mp4"),("AVI","*.avi")))
        name, extension = ntpath.splitext(self.video_data)
        self.video_model.name = name
        self.video_model.format = extension
        self.video_model.path = self.video_data
        if self.video_model.format == ".mp4":
            codec = cv2.VideoWriter_fourcc(*'X264')
        else:
            codec = cv2.VideoWriter_fourcc(*'XVID')
        self.output = cv2.VideoWriter(self.video_model.name + self.video_model.format, codec,  60.0, (1920, 1080))
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def save_video(self):
        self.output.release()

    def toInt(self):
        self.value = self.view.timer.get()
        try:
            return int(self.value)
        except ValueError:
            return None

    def screenshot(self):
        timer = self.toInt()
        Capturer.take_screenshot(timer, self.root)







