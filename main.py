import requests
import json
import tkinter as tk
from tkinter import messagebox
import time as t
import os
from dotenv import load_dotenv

#Hente API key fra .env fila
load_dotenv(".env")
YOUR_API_KEY = os.getenv('apikey')

print("<<-- Weather App Console -->>     Version: 0.0.2")

