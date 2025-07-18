import requests
from tkinter import *
import tkinter.messagebox as tmsg

def get_weather():
    city=city_entry.get()
    city=city.capitalize()
    if not city:
        tmsg.showwarning("Input Error", "Please enter a city name")
        return
    api_key="dc5e41e36d730b5a6c5205d65deeadba"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            condition = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result=(
                      f"City: {data['name']}\n"
                      f"Temperature: {temperature} °C\n"
                      f"Condition: {condition}\n"
                      f"Humidity: {humidity} %\n"
                      f"Wind speed: {wind_speed} m/s\n"
                   )
            result_label.config(text=result)
        else:
            result_label.config(text="")
            tmsg.showerror("Error","City Not Found")

    except Exception as e:
        tmsg.showerror("Error",f"Something went wrong:\n{e}")


# --- GUI Setup ---

root = Tk()
root.title("Weather App")
root.geometry("400x350")
root.iconbitmap("logo.ico")
root.resizable(False, False)
root.configure(bg="#f0f8ff")

# Heading Label
heading_label = Label(root, text="Check your City's Weather ",font=("Helvetica",15,"bold"),bg="#f0f8ff",fg="#333")
heading_label.grid(row=0, column=0, columnspan=2, pady=15)

# City Label
city_label = Label(root, text="Enter City Name:",font=("Calibri",12))
city_label.grid(row=1, column=0, padx=15, pady=10, sticky="e")

# City Entry
city_entry = Entry(root, width=25, font=("Calibri", 12))
city_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Search Button
search_button = Button(root, text="Get Weather", width=15,command=get_weather)
search_button.grid(row=2, column=1, columnspan=2, pady=10)

# Result Display Area
result_label = Label(root, text="", font=("Calibri", 12),fg="blue", justify="left")
result_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

# Run the app
root.mainloop()



