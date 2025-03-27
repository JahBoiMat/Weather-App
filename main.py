import requests
import tkinter as tk
from tkinter import messagebox
import tkintermapview as tkmap
import os
from dotenv import load_dotenv
from datetime import datetime

print("")
print("<<-- Dr.Matvey's Weather App Console Log-->>     Version: 0.0.9")
print("""
Log Actor List: 
[ Ack ] (Acknowledge) = Api acknowledge message
[ Sys ] (System) = Process related message / Process Status
[ Err ] (Error) = Error/Exeption - Related to current process
[ Idl ] (Idle) = Idle/Waiting, no processes
[=STR=] (Start) = Marks start of a process - The following logs are related to this process until next [=STR=] is called
This console is used for debugging only, please look to TkInter Window for weather data
""")
print("<<===== LOG =====>>")
print("[=STR=] - Main Start")
load_dotenv(".env")
YOUR_API_KEY = os.getenv('apikey') #testkey = test key (t) apikey = main key
set_marker = None
print("[ Idl ] - Idle, Click on map") 

# - - - - LOGIC - - - -

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
        temp = data["main"]["temp"]
        feelslike = data["main"]["feels_like"]
        min_temp = data["main"]["temp_min"]
        max_temp = data["main"]["temp_max"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        print("[ Sys ] - Readable Format: ","City: ", city ,"Country: ", country,"Condition: ", condition,"Temperature: ", temp,"Feels like: ", feelslike, "Minimum Temp: ", min_temp,"Maximum Temp: ", max_temp,"Humidity: ", humidity,"Pressure: ", pressure)
        
    elif api_response.status_code==404:
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - Server could not find the client-requested webpage")
        print("[ Err ] Denied - Text: ", api_response.text)
        print("[ Err ] Denied - Data: ", data)
        messagebox.showerror("Failed to contact server", "Error 404 - could not contact server. Check your internet connection and try again.")
    else:
        print("[ Err ] Request Failed: Other - Status: ", api_response.status_code)
        print("[ Err ] Request Failed: Other - Text: ", api_response.text)
        messagebox.showerror("Unexpected Error", "An unexpected error occurred - Check console or close program")

def getweatherforecast(lat, lon):
    print("[=STR=] - Get Weather Forecast Data")
    print("[ Sys ] - Current Function: getweatherforecast")
    print("[ Sys ] - Api call Start")
    api_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=7&appid={YOUR_API_KEY}")
    data = api_response.json()
    if api_response.status_code==200:
        print("[ Ack ] - Api Status: ", api_response.status_code)
        print("[ Ack ] - Api Returned Data: ", data)
        print("[ Sys ] - Assigning Variables")

        print("[ Sys ] - Rqst empty, for now")
        
    elif api_response.status_code==404:
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - Server could not find the client-requested webpage")
        print("[ Err ] Denied - Text: ", api_response.text)
        print("[ Err ] Denied - Data: ", data)
        messagebox.showerror("Failed to contact server", "Error 404 - could not contact server. Check your internet connection and try again.")
    else:
        print("[ Err ] Request Failed: Other - Status: ", api_response.status_code)
        print("[ Err ] Request Failed: Other - Text: ", api_response.text)
        messagebox.showerror("Unexpected Error", "An unexpected error occurred - Check console or close program")

def place_marker(coords):
    lat, lon = coords
    global set_marker
    print("[=STR=] - Click Map Data")
    print("[ Sys ] - Current Function: place_marker")
    print("[ Sys ] - User Interaction : Lat-", lat, "Lon-", lon)
    if set_marker is not None:
        set_marker.delete()
        print("[ Sys ] - Deleted Previous Marker")
    print("[ Sys ] - Create Marker")
    set_marker = map_widget.set_marker(lat, lon, text="Selected Location")
    print("[ Sys ] - Function Call : getweathercurrent")
    getweathercurrent(lat, lon)
    print("[ Sys ] - Function Call : getweatherforecast")
    getweatherforecast(lat, lon)

    
    

# - - - - VISUAL - - - -
root_tk = tk.Tk()
root_tk.geometry(f"{800}x{500}")
root_tk.title("Dr.Matvey's Syke Værapp")
root_tk.resizable(False, False)

map_widget = tkmap.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)
map_widget.grid(rowspan = 2, padx = 0, pady = 0)
map_widget.set_position(59.669199, 9.647202)
map_widget.set_zoom(12)
map_widget.add_left_click_map_command(place_marker)


root_tk.mainloop()


#KI BRUKT TIL: 
#Slette gammel map marker slik at det ikke blir laget flere markers
#
