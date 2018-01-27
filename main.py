from tkinter import *
from game import *
import os






init(800,600,"space colonizer")
create_player(400,500)
i = PhotoImage(file = os.path.join("imgs","e.png"))
create_Mob(i)





start()
