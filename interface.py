import tkinter as tk
import os

root = tk.Tk()

myLabel = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="String template")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

# canvas = tk.Canvas(root, height=1000, width=1000, bg="#26DDFF")
# canvas.pack()

root.mainloop()