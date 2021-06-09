import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames),borderwidth=0)
            self.after(self.delay, self.next_frame)


def register_window():
    root = tk.Toplevel(bg="black")
    root.geometry("1024x350+0+50")
    root.overrideredirect(1)
    # root = tk.Tk()
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('animations/ready_for_scan.gif')
    
    label_instruction = tk.Label(root, text="Place your finger on the fingerprint sensor for 5 times", 
                                 bg="black", fg="white")
    Font_tuple = ("Modern", 15, "bold")
    label_instruction.config(font = Font_tuple)
    label_instruction.pack()
    
    # root.mainloop()

def login_window():
    root = tk.Toplevel(bg="black")
    root.geometry("1024x350+0+50")
    root.overrideredirect(1)
    # root = tk.Tk()
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('animations/ready_for_scan.gif')
    
    label_instruction = tk.Label(root, text="Place your finger on the fingerprint sensor", 
                                 bg="black", fg="white")
    Font_tuple = ("Modern", 15, "bold")
    label_instruction.config(font = Font_tuple)
    label_instruction.pack()

# register_window()