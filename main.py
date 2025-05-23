import requests
import tkinter as tk
from tkinter import messagebox
import tkintermapview as tkmap
import os # You dont need this if you hardcode your API key
from dotenv import load_dotenv # You also dont need this if you hardcode your API key
from datetime import datetime

v="0.2.2" # version number
print("")
print("<<-- Repository: https://github.com/JahBoiMat/Weather-App -->>")
print(f"<<-- Dr.Matvey's Wicked Weather App Console Log-->>     Version: {v}")
print("""
Log Acro List: 
[ Ack ] (Acknowledge) = Api acknowledge message.
[ Sys ] (System) = Process related message / Process Status.
[ Err ] (Error) = Error/Exeption - Related to current process.
[ Idl ] (Idle) = Idle/Waiting for input.
[=STR=] (Start) = Marks start of a function - The following prints are related to this process until [=END=].
[=END=] (End) = Marks end of a function.
This console is used for debugging, please look to the Python Window for a readable application and Weather data.
""")
print("<<===== LOG =====>>")
print("[=STR=] - Main Start")
load_dotenv(".env") # You also ALSO dont need this if you hardcode your API key
YOUR_API_KEY = os.getenv('apikey') #testkey = test key (t) apikey = main key # You also ALSO ALSOOO dont need this if you hardcode your API key
set_marker = None
set_location = None 

#-----------------------#
# - - - - LOGIC - - - - #
#-----------------------#
def getweathercurrent(lat, lon): # get current weather
    print("[=STR=] - Get Current Weather Data")
    print("[ Sys ] - Current Function: getweathercurrent")
    print("[ Sys ] - Api call Start")
    api_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={YOUR_API_KEY}&units=metric") #replace YOUR_API_KEY with your key to get weather data
    data = api_response.json()
    if api_response.status_code==200:
        print("[ Ack ] - Api Status: ", api_response.status_code)
        print("[ Ack ] - Api Returned Data: ", data)
        print("[ Sys ] - Assigning Variables")

        if "sys" in data and "country" in data["sys"]:
            country = data["sys"]["country"]
        else:
            print("[ Sys ] - Invalid location (e.g. ocean)")
            country = "N/A"
        city = data["name"]
        condition = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        temp_feels = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind_speed =data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]

        print(f"[ Sys ] - Readable Format: City: {city} | Country: {country} | Conditions: {condition} | Temperature: {temp}°C | Feels like: {temp_feels}°C | Pressure: {pressure}Pa | Humidity: {humidity}% | Wind Speed {wind_speed}m/s | Wind Deg: {wind_deg}°")
        weather_location.set(f"Conditions in {city}, {country}")
        weather_current.set(f"Current condition(s): {condition.capitalize()}. Temperature is {temp}°C (Feels like: {temp_feels}°C) Winds at {wind_speed}m/s from {wind_deg}°. Pressure: {pressure}Pa Humidity: {humidity}%")

        print("[=END=] - Get Current Weather Data")

    elif api_response.status_code==404: 
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - Server could not find the client-requested webpage")
        print("[ Err ] Denied - Text: ", api_response.text)
        print("[ Err ] Denied - Data: ", data)
        print("[=END=] - Get Current Weather Data")
        messagebox.showerror("Failed to contact server", "Error 404 - could not contact server. Check your internet connection and try again.")

    else:
        print("[ Err ] Request Failed: Other - Status: ", api_response.status_code)
        print("[ Err ] Request Failed: Other - Text: ", api_response.text)
        print("[=END=] - Get Current Weather Data")
        messagebox.showerror("Unexpected Error", "An unexpected error occurred - Check terminal or close program")


def getweatherforecast(lat, lon): # get 7 day forecast
    print("[=STR=] - Get Weather Forecast Data")
    print("[ Sys ] - Current Function: getweatherforecast")
    print("[ Sys ] - Api call Start")
    api_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=8&appid={YOUR_API_KEY}&units=metric") #replace YOUR_API_KEY with your key to get weather data
    data = api_response.json()
    if api_response.status_code==200:
        print("[ Ack ] - Api Status: ", api_response.status_code)
        print("[ Ack ] - Api Returned Data: ", data)
        
        forecast_list = []
        print("[ Sys ] - Adding Forecast Data to List")
        for day in data["list"][1:]: 
            weekday = datetime.fromtimestamp(day["dt"]).strftime("%A")

            condition = day["weather"][0]["description"]
            temp_min = day["temp"]["min"]
            temp_max = day["temp"]["max"]

            forecast_list.append(f"{weekday}: {condition.capitalize()}. Temp - Hi:{temp_max}°C Lo:{temp_min}°C")
            print(f"[ Sys ] - Added {weekday} data to list")
        
        print("[ Sys ] - Forecast List Updated")
        weather_forecast.set("\n".join(forecast_list))
        print("[=END=] - Get Weather Forecast Data")

    elif api_response.status_code==404:
        print("[ Err ] Denied - Status: ", api_response.status_code)
        print("[ Err ] Denied - Server could not find the client-requested webpage")
        print("[ Err ] Denied - Text: ", api_response.text)
        print("[ Err ] Denied - Data: ", data)
        print("[=END=] - Get Weather Forecast Data")
        messagebox.showerror("Failed to contact server", "Error 404 - could not contact server. Check your internet connection and try again.")
        
    else:
        print("[ Err ] Request Failed: Other - Status: ", api_response.status_code)
        print("[ Err ] Request Failed: Other - Text: ", api_response.text)
        print("[=END=] - Get Weather Forecast Data")
        messagebox.showerror("Unexpected Error", "An unexpected error occurred - Check terminal or close program")
    


def place_marker(coords): #User map interaction
    lat, lon = coords
    global set_marker
    print("[=STR=] - Click Map Data")
    print("[ Sys ] - Current Function: place_marker")
    print(f"[ Sys ] - User Interaction : Lat-{lat} Lon-{lon}")
    if set_marker is not None:
        set_marker.delete()
        print("[ Sys ] - Deleted Previous Marker")
    print("[ Sys ] - Create Marker")
    set_marker = map_widget.set_marker(lat, lon, text="Selected Location")
    print("[ Sys ] - Function Call : getweathercurrent")
    getweathercurrent(lat, lon)
    print("[ Sys ] - Function Call : getweatherforecast")
    getweatherforecast(lat, lon)
    print("[=END=] - Click Map Data")
    
#------------------------#
# - - - - VISUAL - - - - #
#------------------------#
root_tk = tk.Tk()
root_tk.geometry(f"{800}x{500}")
root_tk.title("Dr. Matvey's Wicked Weather App")
root_tk.iconbitmap("logo.ico") #uncomment to add logo
root_tk.resizable(False, False)
root_tk.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
root_tk.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

map_widget = tkmap.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)
map_widget.grid(row=0, column=0, rowspan=5, padx=0, pady=0)
map_widget.set_position(59.669199, 9.647202)
map_widget.set_zoom(12)
map_widget.add_left_click_map_command(place_marker)

#Labels
title_static = tk.StringVar()
title_static.set("Dr. Matvey's Wicked Weather App")

description_static = tk.StringVar()
description_static.set("Welcome! Click on the map to see weather data.")

version = tk.StringVar()
version.set(f"Version: {v} - ©Matvey Golovtsov 2025 All rights reserved")

weather_location = tk.StringVar()
weather_current = tk.StringVar()
weather_forecast = tk.StringVar()

if set_location is None:
    weather_location.set("No location Selected")
    weather_current.set("No weather data to display. Please select a location.")
    weather_forecast.set("No forecast data available. Please select a location")
    print("[ Sys ] - No location selected")
    print("[ Idl ] - Idle, awaiting user interaction")
else:
    pass

#Label Design / Layout
title_static_label = tk.Label(root_tk, textvariable=title_static, anchor=tk.CENTER, font=("Arial", 14, "bold"), fg="black",padx=25, justify=tk.CENTER)
title_static_label.grid(row=0, column=1, columnspan=2, rowspan=1)

description_static_label = tk.Label(root_tk, textvariable=description_static, anchor=tk.CENTER, font=("Arial", 10), fg="black", padx=25, justify=tk.CENTER)
description_static_label.grid(row=0, column=1, columnspan=2, rowspan=2)
 
version_label = tk.Label(root_tk, textvariable=version, anchor=tk.CENTER, font=("Arial", 6, "bold"), fg="grey", padx=10, justify=tk.CENTER)
version_label.grid(row=4, column=1, columnspan=2, rowspan=2)

weather_location_label = tk.Label(root_tk, textvariable=weather_location, anchor=tk.CENTER, font=("Arial", 14, "bold"), fg="black", padx=10, justify=tk.CENTER)
weather_location_label.grid(row=1, column=1, columnspan=2, rowspan=1)

weather_current_label = tk.Label(root_tk, textvariable=weather_current, anchor=tk.CENTER, font=("Arial", 9), fg="black", padx=10, pady=10, justify=tk.CENTER, wraplength=310)
weather_current_label.grid(row=1, column=1, columnspan=2, rowspan=2)

weather_forecast_label = tk.Label(root_tk, textvariable=weather_forecast, anchor=tk.CENTER, font=("Arial", 8), fg="black", padx=10, pady=10, justify=tk.CENTER, wraplength=320)
weather_forecast_label.grid(row=1, column=1, columnspan=2, rowspan=4)



root_tk.mainloop()

#KI BRUKT TIL: 
#Forklare feilmeldinger <- 
#Forklare hvordan grid fungerer i tkinter
#Hvordan jeg kan hente ut 1 og 1 dag fra forecast lista og legge den til i en felles liste for å bli vist i den label tingen
