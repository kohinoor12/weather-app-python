import json
import tkinter as tk
import requests
import time

def getWeather(root):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=d0de5432e62c40c1e2b4010847473b69"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + '\n' + str(temp) + '°C' 
    final_data  =   '\n' + 'Max Temp: ' + str(max_temp) + '\n' + 'Min Temp: ' + str(min_temp) + '\n' + 'Pressure' + str(pressure) + '\n' + 'Humidity: ' + str(humidity) + '\n' + 'Wind Speed: ' + str(wind) + '\n' + 'Sunrise: ' + sunrise + '\n' + 'Sunset' + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)

root = tk.Tk()
root.geometry("600x500")
root.title("Weather App")

f = ('poppins',15,'bold')
t = ('poppins',35,'bold')

textfield = tk.Entry(root,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(root,font=t)
label1.pack()

label2 = tk.Label(root,font=f)
label2.pack()

root.mainloop()