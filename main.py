import requests
#import tkinter as tk
#from tkinter import messagebox
#import tkintermapview as tkmap
import os
from dotenv import load_dotenv

#Hente API key fra .env fila
load_dotenv(".env")
YOUR_API_KEY = os.getenv('apikey')
print("<<-- Top Secret Weather App Admin Debug Console Log-->>     Version: 0.0.4")


# - - - - LOGIKK

def getweather(city):
    print("Current Function: getweather()")
    print("Api call init")
    api_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={YOUR_API_KEY}&units=metric")
    data = api_response.json()
    if api_response.status_code==200:
        print("[ Ack ] - Status: ", api_response.status_code)
        print("[ Ack ] - Retruned Data: ", data)
        print("[ Sys ] - Expected Results:")

        country = data["sys"]["country"]
        city = data["name"]
        condition = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print("[ Sys ] - Refined: ",city ,country, condition, temperature, humidity)
        
    elif api_response.status_code==404:
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - server could not find a client-requested webpage")
        print("[ Err ] Denied - Data: ", data)
    else:
        print("[ Exp ] Request Failed: Other - Status: ", api_response.status_code)


    
    

# - - - - UTSEENDE
"""#opprette tkinter vindu med navn og størrelse
root_tk = tk.Tk()
root_tk.geometry(f"{800}x{500}")
root_tk.title("Dr.Matvey's Syke Værapp")
root_tk.resizable(False, False)

# map widget config størrelse og plassering osv
map_widget = tkmap.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)
map_widget.place(x=0, y=0)
map_widget.set_position(59.669199, 9.647202)
map_widget.set_zoom(12)

root_tk.mainloop()"""


cityname = input("City: ")
getweather(cityname)

