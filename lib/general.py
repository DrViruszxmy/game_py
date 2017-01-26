from lib import layout
import tkinter
import sys


gamescene = tkinter.Tk()
layout.__fullscreen(gamescene)
layout.__center(gamescene)
gamescene.title('Game')

def close(event):
    gamescene.destroy()


# Code to add widgets will go here...
photo = tkinter.PhotoImage(file="../img/grass-pattern.gif")

label = tkinter.Label(image=photo)
label.image = photo # keep a reference!
label.pack()
c = tkinter.Canvas(gamescene, bg="white", height=gamescene.winfo_screenheight(), width=gamescene.winfo_screenwidth())
c.create_image(0,0,image=photo)
#coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start=0, extent=150, fill="red")

c.pack()

gamescene.bind('<Escape>',close)
layout.__initGameScene(gamescene)






