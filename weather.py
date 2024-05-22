import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import font

def get_weather(city):
    api_key = 'efcd04d7813a14e6a78eab0cd1a738ae'  # Replace with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]
        return {
            'city': city,
            'temperature': main['temp'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'description': weather['description'],
        }
    else:
        return None

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        result = f"City: {weather['city']}\nTemperature: {weather['temperature']}°C\n"
        result += f"Pressure: {weather['pressure']} hPa\nHumidity: {weather['humidity']}%\n"
        result += f"Description: {weather['description']}"
    else:
        result = "City not found."
    
    messagebox.showinfo("Weather Information", result)

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")  # Set window size with correct format

# Create a custom font
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create and place the widgets with padding
city_label = tk.Label(root, text="Enter city name:", font=custom_font)
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=custom_font)
city_entry.pack(pady=10)

get_weather_btn = tk.Button(root, text="Get Weather", command=show_weather, font=custom_font)
get_weather_btn.pack(pady=20)

# Run the application
root.mainloop()