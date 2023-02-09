import tkinter as tk
import requests
from bs4 import BeautifulSoup


def get_weather():
    city = city_entry.get()
    page = requests.get(f"https://www.google.com/search?q={city}+weather")
    soup = BeautifulSoup(page.content, "html.parser")
    temperature = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    weather_label["text"] = f"Temperature in {city}: {temperature}"


root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

city_label = tk.Label(root, text="City:", font=("Helvetica", 16), fg="black")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="", font=("Helvetica", 16), fg="black")
weather_label.pack()

root.mainloop()
