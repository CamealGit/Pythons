import tkinter as tk
from customtkinter import *

app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")

btn1 = CTkButton(master=app, text="Hello World", fg_color="#4158D0", corner_radius=32, hover_color="#C850C0,", border_color="#FFCC70")
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
app.mainloop()
