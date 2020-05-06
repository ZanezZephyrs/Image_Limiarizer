import tkinter as tk
import tkinter.filedialog as tkf
import os
import cv2
import numpy as np
import Limiarization_methods as lm
import constants as co
import input_validation as iv
from tkinter import messagebox

global entrada
global estado
global saida
estado = 0

image_path = ["image.png"]


def btn_func():
    tk.filedialog
    dialog = tk.filedialog.askopenfilename(
        initialdir="/",
        title="Select a image to limiarize",
        filetypes=(("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg"),
                   ("Others", "*.*")))
    print(dialog)
    image_path[0] = dialog
    entrada.delete(0, tk.END)
    entrada.insert(0, dialog)


def show_state(state):
    print("selected state is: ", state)


def Apply():
    try:
        img = cv2.imread(image_path[0], cv2.IMREAD_GRAYSCALE)
        limiarizado = img
        if (estado == 0):
            limiarizado = lm.global_method_adjustive_treshold(
                img, co.global_method_parameters["treshold"])
        elif (estado == 1):
            limiarizado = lm.mean_method(img,
                                         co.mean_method_parameters["size"])
        elif (estado == 2):
            limiarizado = lm.bernsen(img, co.bernsen_method_parameters["size"])
        elif (estado == 3):
            limiarizado = lm.Phansalskar(
                img, co.Phansalskar_method_parameters["size"],
                co.Phansalskar_method_parameters["k"],
                co.Phansalskar_method_parameters["r"],
                co.Phansalskar_method_parameters["p"],
                co.Phansalskar_method_parameters["q"])
        limiarizado = np.uint8(255 * limiarizado)
        return limiarizado

    except:
        tk.messagebox.showerror(
            "Wrong Input File",
            "Please, Select a valid input file, it must be an image with one of the following formats:\n png, jpg, jpeg"
        )
        print("wrong input")
        return


def show_image():
    print("show image")

    resp = Apply()
    if (resp):
        cv2.imshow("Image", resp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def change(it):
    print("changed ", it)
    if (it == "Global Limiarization"):
        estado = 0
    elif (it == "Mean Method"):
        estado = 1
    elif (it == "Bernsen Method"):
        estado = 2
    elif (it == "Phansalskar Method"):
        estado = 3


def save_image():
    print("saving")
    output_name = saida.get()
    if (iv.validate_output_name(output_name)):
        resp = Apply()
        if (resp):
            cv2.imwrite(output_name, resp)
    else:
        tk.messagebox.showerror(
            "Output Name wrong or Undefined",
            "Please, write a valid output Name!\nThe output shouldn't contain any space and must end with .(png,jpeg,jpg)"
        )


root = tk.Tk()
root.title("Python Image Limiarizer")
root.geometry("600x600")

Label1 = tk.Label(root, text="Selecione sua imagem")
Label1.pack()

drop_ans = tk.StringVar()
drop_ans.set("Global Limiarization")
drop = tk.OptionMenu(root,
                     drop_ans,
                     "Global Limiarization",
                     "Mean Method",
                     "Bernsen Method",
                     "Phansalskar Method",
                     command=change)

drop.pack()

entrada = tk.Entry(root, width=50)
entrada.pack(pady=5, padx=5)
entrada.insert(0, "Selecione sua imagem")

saida = tk.Entry(root, width=50)
saida.pack(pady=5, padx=5)
saida.insert(0, "Digite o nome da imagem de saida")

button = tk.Button(root,
                   text="Selecione sua imagem",
                   command=btn_func,
                   height=10,
                   width=20)
button.pack(pady=5, padx=5, side=tk.LEFT)
# canvas = tk.Canvas(root, height=1000, width=1000, bg="#26DDFF")
# canvas.pack()

button2 = tk.Button(root,
                    text="Apply and show image",
                    command=show_image,
                    height=10,
                    width=20)
button2.pack(pady=5, padx=5, side=tk.LEFT)

button3 = tk.Button(root,
                    text="Apply and save image",
                    command=save_image,
                    height=10,
                    width=20)
button3.pack(pady=5, padx=5, side=tk.LEFT)

root.mainloop()