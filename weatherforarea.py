import json
import requests
from tkinter import *
from PIL import ImageTk
import datetime
import pytz

root = Tk()
root.title('Current Weather')
root.configure(bg='black')
iconphoto = PhotoImage(file='C:\weatherpics\weatherapplogo.png')
root.iconphoto(True, iconphoto)

e = Entry(root, width=70)
e.grid(row=0, column=0, columnspan=2)

api_key = '064168b38869a1444bf3146de4248aa9'

def disable():
    tempslider.config(state=DISABLED)
    tempslider.grid(row=2, column=1)

def checkweather():
    global api_key, data, tempslider
    global weathericon, weatherpic, weatherlabel
    global currenttime
    currenttime = datetime.datetime.now(tz=pytz.timezone('America/New_York'))
    military_hour = currenttime.strftime('%H')
    hour = int(military_hour)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={e.get()}&units=imperial&appid={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    currentweather = data['main']['temp']
    weatherpic = data['weather'][0]['description']
    if 'clouds' in weatherpic:
        if hour < 5:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\scatteredcloudsdayornight.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='purple')
            weatherlabel.grid(row=2, column=0)
        elif hour >= 5:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\scatteredcloudsdayornight.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='#FFAE42')
            weatherlabel.grid(row=2, column=0)
    if 'clear' in weatherpic:
        if hour < 5 or hour > 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\clearskynight.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='purple')
            weatherlabel.grid(row=2, column=0)
        elif hour >= 5 and hour <= 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\clearskyday.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='#FFAE42')
            weatherlabel.grid(row=2, column=0)
    if 'rain' in weatherpic:
        if hour < 5 or hour > 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\\rainnight.png.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='purple')
            weatherlabel.grid(row=2, column=0)
        elif hour >= 5 and hour <= 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\\rainnight.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='#FFAE42')
            weatherlabel.grid(row=2, column=0)
    if weatherpic == 'snow':
        if hour < 5 or hour > 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\snow.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='purple')
            weatherlabel.grid(row=2, column=0)
        elif hour >= 5 and hour <= 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\snow.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='#FFAE42')
            weatherlabel.grid(row=2, column=0)
    if weatherpic == 'thunderstorm':
        if hour < 5 or hour > 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\\thunderstorm.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='purple')
            weatherlabel.grid(row=2, column=0)
        elif hour >= 5 and hour <= 20:
            weathericon = ImageTk.PhotoImage(file='C:\\weatherpics\\thunderstorm.png')
            weatherlabel = Label(root, image=weathericon, height=125, bg='#FFAE42')
            weatherlabel.grid(row=2, column=0)
# finish up all of the weather descriptions and using datetime module, fix up background
    tempslider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
    tempslider.set(currentweather)
    tempslider.grid(row=2, column=1)
    tempslider.after(0, disable)

weatherbtn = Button(root, text='Check Weather', width=50, height=3, borderwidth=3, pady=5, command=checkweather)
weatherbtn.grid(row=3, column=0, columnspan=2)

root.mainloop()
#temperature check
