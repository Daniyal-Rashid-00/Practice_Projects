import requests
import tkinter as tk
from tkinter import messagebox

# Function to get the weather
def get_weather():
    city = city_get.get()
    api_key = "fa861ae77e724cef99c51659241411"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"