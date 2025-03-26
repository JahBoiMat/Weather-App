import requests
import tkinter as tk
from tkinter import messagebox
import tkintermapview as tkmap
import time as t
import os
from dotenv import load_dotenv

#Hente API key fra .env fila
load_dotenv(".env")
YOUR_API_KEY = os.getenv('apikey')

print("<<-- Weather App Console -->>     Version: 0.0.3")

# create tkinter window
root_tk = tk.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("Dr.Matvey's Syke Værapp")

# create map widget
map_widget = tkmap.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root_tk.mainloop()


