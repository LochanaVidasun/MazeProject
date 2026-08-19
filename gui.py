import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class MazeGUI:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("Maze Game")
        self.root.iconphoto(True, ImageTk.PhotoImage(file= 'my_image.png'))

        #Grid positioning  
        self.label = tk.Label(self.root, text="Welcome to the Maze Game!")
        self.label.grid(row=0, column=0)

        #Canvas Drawing = 

        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=4, rowspan=3)

        self.canvas.create_rectangle (0, 0, 50, 50, fill="blue")

        self.image = ImageTk.PhotoImage(file = "my_image.png")
        self.canvas.create_image (50, 50, image=self.image, anchor="nw")

        #Event Handling =

        tk.Button(self.root, text="Up").grid(row=4, column=1)
        tk.Button(self.root, text="Down").grid(row=6, column=1)
        tk.Button(self.root, text="Left").grid(row=5, column=0)
        tk.Button(self.root, text="Right").grid(row=5, column=2)

        #Menu bar =
        self. menubar = tk. Menu (self.root)
        self. helpmenu = tk.Menu (self.menubar, tearoff = 0)
        self. helpmenu.add_command(label="Help", command=lambda: messagebox.showinfo ("Help", "This is the help message."))
        self. helpmenu.add_command (label= " About ...", command=lambda: messagebox.showinfo ("About", "This is the about message."))

        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menubar)

def main ():
    root = tk.Tk()
    maze_gui=MazeGUI (root)
    root.mainloop()

if __name__ == "__main__":
    main()
