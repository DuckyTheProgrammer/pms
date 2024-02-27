import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import tkinter.messagebox as messagebox

#ctk.set_appearance_mode("light")
#ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("system")  # default value
ctk.set_default_color_theme("blue")


loginWindow = ctk.CTk()
loginWindow.title('Login...')
loginWindow.geometry('350x350')

user_info = ['admin', '123']

def validate_uinfo():
    usr = username_entry.get()
    pwd = password_entry.get()

    if usr != user_info[0]:
        messagebox.showerror('...', 'Invalid username or password')
    elif pwd != user_info[1]:
        messagebox.showerror('...', 'Invalid username or password')
    else:
        loginWindow.destroy()

username_entry = ctk.CTkEntry(loginWindow, placeholder_text="Username...")
password_entry = ctk.CTkEntry(loginWindow, placeholder_text="Password...", show="*")
submit_btn = ctk.CTkButton(loginWindow, text="Log In", command=validate_uinfo)

username_entry.pack()
password_entry.pack()
submit_btn.pack()


loginWindow.mainloop()