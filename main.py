from tkinter import *
import tkinter.font as tkFont
from services.light import *

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0', flush=True)
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Tk()

font = tkFont.Font(family="Tahoma", size=18, weight=tkFont.BOLD, slant=tkFont.ITALIC)

window.attributes('-fullscreen', True)
window.config(cursor="none")
window.title("Home UI")
window.geometry("480x320")
window.maxsize(480, 320)

states = {
  "light.living_room": "off", 
  "light.kitchen": "off", 
  "light.bedroom": "off", 
  "light.hallway": "off"
}

local_states = {}

def clear_local(entity_id):
  local_states[entity_id] = None

def resolve_state(entity_id):
  if entity_id in local_states.keys() and local_states[entity_id] != None:
    return local_states[entity_id]
  return states[entity_id]

def get_opposite_state(state):
  return "on" if state == "off" else "off"

def get_bg(entity_id):
  state = resolve_state(entity_id)
  return "green" if state == "on" else "gray"

def get_activebg(entity_id):
  state = resolve_state(entity_id)
  return "green" if state == "on" else "gray"

def switch(area_id):
  new_state = get_opposite_state(states["light.{area_id}".format(area_id=area_id)])
  switch_area(area_id, "{new_state}".format(new_state=new_state))
  local_states["light.{area_id}".format(area_id=area_id)] = new_state
  window.after(5000, lambda: clear_local("light.{area_id}".format(area_id=area_id)))

main_frame = Frame(window)
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

left_frame = Frame(main_frame)
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)
right_frame = Frame(main_frame)
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

buttons = {}

def make_button(frame, rely, text, area_id):
  buttons["light.{area_id}".format(area_id=area_id)] = Button(
    frame, 
    text=text, 
    command=lambda: switch(area_id), 
    bg=get_bg("light.{area_id}".format(area_id=area_id)), 
    activebackground=get_activebg("light.{area_id}".format(area_id=area_id)), 
    font=font)
  buttons["light.{area_id}".format(area_id=area_id)].place(
    relx=0.5, 
    rely=rely, 
    relwidth=1,
    relheight=0.5,
    anchor="n")

make_button(left_frame, 0, "Living room", "living_room")
make_button(left_frame, 0.5, "Hallway", "hallway")
make_button(right_frame, 0, "Bedroom", "bedroom")
make_button(right_frame, 0.5, "Kitchen", "kitchen")

def update_colors():
  for entity_id in states.keys():
    buttons[entity_id].configure(bg=get_bg(entity_id), activebackground=get_activebg(entity_id))
  window.after(50, update_colors)

update_colors()

def update_states():
  global states
  states = get_states(states.keys())
  print(states, flush=True)
  window.after(1000, update_states)

update_states()

window.mainloop()
