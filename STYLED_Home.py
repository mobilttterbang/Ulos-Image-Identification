# import libraries
# pip install ttkbootstrap
# GUI
import os
from tkinter import *

import ttkbootstrap as tb

# define app window
app = tb.Window(themename="superhero")

# set the window size
app.title("Ulos Image Classification")
app.geometry("800x650")

# functions
def open_predict():
    app.destroy()
    os.system("python STYLED_Predict.py")

# frame of the content
frame = tb.Frame(app)
frame.place(relx=0.5, rely=0.5, anchor=tb.CENTER)

# title48
title_sec = tb.Label(frame, text="ULOS IDENTIFICATION GUI",
                font=("Helvetica", 24, "bold"), 
                justify="center")
title_sec.pack()

# description
desc_sec = tb.Label(frame, text="GUI Aplikasi prediksi kain Ulos \n aplikasi ini dibuat untuk mengidentifikasi jenis ulos \n dengan memasukkan gambar ulos yang ingin dikenali",
                font=("Helvetica", 12), 
                justify="center")
desc_sec.pack()

# button
pred_but = tb.Button(frame, text="Prediksi", command=open_predict)
pred_but.pack(pady=15)

# run in loop
app.mainloop()