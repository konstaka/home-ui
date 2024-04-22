from tkinter import *
import tkinter.font as tkFont
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Tk()

font = tkFont.Font(family="Tahoma", size=18, weight=tkFont.BOLD, slant=tkFont.ITALIC)

def exit():
  print("Exiting")
  window.quit()

window.attributes('-fullscreen', True)
window.title("Home UI")
window.geometry("480x320")

exitButton = Button(window, text="Exit", command=exit, font=font, padx=30, pady=30)
exitButton.pack()

window.mainloop()
