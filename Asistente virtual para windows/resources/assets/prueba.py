 
import tkinter as tk
from PIL import Image,ImageTk
import os
import shutil
import time

class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("90x90")

        # to remove the title bar
        self.root.wm_overrideredirect(True)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both",expand=True)

        self.image_label = tk.Label(self.main_frame,image="")
        self.image_label.pack()

        os.mkdir('gif_frames')
        self.start = time.time()

        self.gif_frames = []
        self.images = []
        self.animation()
        self.root.mainloop()

    def animation(self):
        gif = Image.open('2.gif')
        self.no_of_frames = gif.n_frames

        for i in range(self.no_of_frames):
            gif.seek(i)
            gif.save(os.path.join('gif_frames',f'gif{i}.png'))
            self.gif_frames.append(os.path.join('gif_frames',f'gif{i}.png'))

        for images in self.gif_frames:
            im = Image.open(images)
            im = im.resize((90,90),Image.ANTIALIAS)
            im = ImageTk.PhotoImage(im)
            self.images.append(im)

        self.show_animation(0)

    def show_animation(self,count):
        image = self.images[count]
        self.image_label.configure(image=image)
        count += 1
        if count == len(self.images)-1:
            count = 0

        # to show the gif only for 10 seconds
        if int(time.time()-self.start) != 4:
            self.x = self.root.after(80,self.show_animation,count)
        else:
            self.root.after_cancel(self.x)
            self.first_screen(self.main_frame)

            """
            to delete the gif_frames folder and images inside it so that when we run the program again
            then we don't get the error saying gif_frames folder already exists.
            """
            shutil.rmtree('gif_frames')

            # to show the title bar
             

    def first_screen(self,f):
        f.pack_forget()


Screen()