from tkinter import *
from game import *







init(800,600,"space colonizer")

image = PhotoImage(file = "imgs\\p.png")
create_player(400,500,image)
i = PhotoImage(file = "imgs\\e.png")
create_Mob(i)





start()
