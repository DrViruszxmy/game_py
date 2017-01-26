import tkinter
#
#Lyout
# set center

def __center(platform):
    platform.update_idletasks()
    w = platform.winfo_screenwidth()
    h = platform.winfo_screenheight()
    size = tuple(int(_) for _ in platform.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    platform.geometry("%dx%d+%d+%d" % (size + (x, y)))
# set fullscreen
def __fullscreen(platform):
    return platform.attributes('-fullscreen',True)
# set minimize
def __minimize(platform):
    return platform.attributes('-fullscreen',False)
#close
def __close(platform):
    return platform.destroy()
#destroy
def __destroy(platform):
    return platform.destroy()
#init
def __initGameScene(platform):
    return platform.mainloop()
