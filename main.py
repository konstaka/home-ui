from tkinter import *
import tkinter.font as tkFont
import os
from requests import post
from dotenv import load_dotenv

load_dotenv()

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Tk()

font = tkFont.Font(family="Tahoma", size=18, weight=tkFont.BOLD, slant=tkFont.ITALIC)

host = "http://homeassistant.local:8123/api"
token = os.environ.get("HASS_TOKEN")
headers = {
    "Authorization": "Bearer {token}".format(token=token),
    "Content-Type": "application/json",
}

area_ids = ["living_room", "kitchen", "bedroom", "hallway"]

def lights_on():
  print("Lights on")
  res = post("{host}/services/light/turn_on".format(host=host), headers=headers, json={"area_id": area_ids})
  print(res.text)

def lights_off():
  print("Lights off")
  res = post("{host}/services/light/turn_off".format(host=host), headers=headers, json={"area_id": area_ids})
  print(res.text)

window.attributes('-fullscreen', True)
window.title("Home UI")
window.geometry("480x320")

Button(window, text="Lights on", command=lights_on, font=font, padx=30, pady=30).pack()
Button(window, text="Lights off", command=lights_off, font=font, padx=30, pady=30).pack()

window.mainloop()
