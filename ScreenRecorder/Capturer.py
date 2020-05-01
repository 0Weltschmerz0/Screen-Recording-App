from PIL import Image
from PIL import ImageTk
import time
import numpy as np
import mss
import PIL.ImageGrab as ImageGrab
from tkinter import Tk, filedialog
import cv2

class Capturer(object):

    @staticmethod
    def grab_screen():
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screen_image = sct.grab(monitor) 
            screen_image = Image.frombytes("RGB", screen_image.size, screen_image.bgra, "raw", "BGRX")
        image_array = np.array(screen_image)
        return image_array

    @staticmethod
    def show_video(master, canvas):
            image_array = Capturer.grab_screen()
            image = Image.fromarray(image_array, mode='RGB')
            image = image.resize((600, 350), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            canvas.create_image(105, 50, image=image, anchor="nw")
            master.update()

    @staticmethod
    def record(recording, output):
        if recording:
            current = Capturer.grab_screen()
            frame = cv2.cvtColor(current, cv2.COLOR_RGB2BGR)
            output.write(frame)

    @staticmethod
    def take_screenshot(timer, master):
        time.sleep(timer)
        img = ImageGrab.grab()
        master.filename = filedialog.asksaveasfilename(title="Select file", defaultextension="*.*", filetypes=(
            ("JPEG", "*.jpg"), ("PNG", "*.png"), ("TIFF", "*.tiff"), ("all files", "*.*")))
        img.save(master.filename)




        


