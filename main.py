import requests
import tkinter as tk
from tkinter import messagebox
import tkintermapview as tkmap
import os
from dotenv import load_dotenv
from datetime import datetime

#Get API from .env file
load_dotenv(".env")
YOUR_API_KEY = os.getenv('apikey')
print("")
print("<<-- Dr.Matvey's Weather App Console Log-->>     Version: 0.0.5")
print("""
Log Actor List: 
[ Ack ] (Acknowledge) = Api acknowledge message
[ Sys ] (System) = Process related message / Process Status
[ Err ] (Error) = Error/Exeption - Related to current process
[=STR=] (Start) = Marks start of a process - The following logs are related to this process until next [=STR=] is called
This console is used for debugging only, please look to TkInter Window
""")
print("[=STR=] - Weather App initialised - Awaiting input")


# - - - - LOGIC

def getweathercurrent(lat, lon):
    print("[=STR=] - Get Current Weather Data")
    print("[ Sys ] - Current Function: getweathercurrent")
    print("[ Sys ] - Api call Start")
    api_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={YOUR_API_KEY}&units=metric")
    data = api_response.json()
    if api_response.status_code==200:
        print("[ Ack ] - Api Status: ", api_response.status_code)
        print("[ Ack ] - Api Returned Data: ", data)
        print("[ Sys ] - Assigning Variables")

        country = data["sys"]["country"]
        city = data["name"]
        condition = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print("[ Sys ] - Readable Format: ","City: ", city ,"Country: ", country,"Condition: ", condition,"Temperature: ", temperature,"Humidity: ", humidity)
        
    elif api_response.status_code==404:
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - Server could not find a client-requested webpage")
        print("[ Err ] Denied - Text: ", api_response.text)
        print("[ Err ] Denied - Data: ", data)
    else:
        print("[ Err ] Request Failed: Other - Status: ", api_response.status_code)
        print("[ Err ] Request Failed: Other - Text: ", api_response.text)

def getweatherforecast(lat, lon):
    print("[=STR=] - Get Weather Forecast Data")
    print("[ Sys ] - Current Function: getweatherforecast")
    print("[ Sys ] - Api call Start")
    api_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={YOUR_API_KEY}&units=metric")
    data = api_response.json()
    if api_response.status_code==200:
        print("[ Ack ] - Api Status: ", api_response.status_code)
        print("[ Ack ] - Api Returned Data: ", data)
        print("[ Sys ] - Assigning Variables")

        country = data["sys"]["country"]
        city = data["name"]
        condition = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print("[ Sys ] - Readable Format: ","City: ", city ,"Country: ", country,"Condition: ", condition,"Temperature: ", temperature,"Humidity: ", humidity)
        
    elif api_response.status_code==404:
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - Server could not find a client-requested webpage")
        print("[ Err ] Denied - Text: ", api_response.text)
        print("[ Err ] Denied - Data: ", data)
    else:
        print("[ Err ] Request Failed: Other - Status: ", api_response.status_code)
        print("[ Err ] Request Failed: Other - Text: ", api_response.text)

def place_marker(coords):
    print("[=STR=] - Click Map Data")
    print("[ Sys ] - Current Function: place_marker")
    lat, lon = coords
    print("[ Sys ] - User Interaction : Lat-", lat, "Lon-", lon)
    print("[ Sys ] - Function Call : getweathercurrent")
    getweathercurrent(lat, lon)
    print("[ Sys ] - Function Call : getweatherforecast")
    getweatherforecast(lat, lon)

    
    

# - - - - VISUAL
#opprette tkinter vindu med navn og størrelse
root_tk = tk.Tk()
root_tk.geometry(f"{800}x{500}")
root_tk.title("Dr.Matvey's Syke Værapp")
root_tk.resizable(False, False)

# map widget config størrelse og plassering osv
map_widget = tkmap.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)
map_widget.grid(rowspan = 2, padx = 0, pady = 0)
map_widget.set_position(59.669199, 9.647202)
map_widget.set_zoom(12)
map_widget.add_left_click_map_command(place_marker)


root_tk.mainloop()
