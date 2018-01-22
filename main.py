from tkinter import *
from game import *
import os






init(800,600,"space colonizer")

image = PhotoImage(file = os.path.join("imgs","p.png"))
create_player(400,500,image)
i = PhotoImage(file = os.path.join("imgs","e.png"))
create_Mob(i)





start()
