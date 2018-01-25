from tkinter import *
import sys
import os
from random import *
from math import *

def start():
    global iMobs
    global Mobs
    global Mdir
    global phase
    phase = 0
    Mdir = 1
    x=2
    y=2
    for i in range(19):
        for j in range(3):
            mob = canvas.create_image(x,y,image= iMobs[0][0] ,  anchor="nw")
            Mobs.append([mob,[x,y]])
            y+=40
        y=2
        x+=40
    update()
    window.mainloop()

def init(width , height , title):
    global players
    global started
    global window
    global canvas
    global Mobs
    global iMobs
    global step
    global shootImage
    global Mshoots
    global Pshoots
    global MshootImage
    Mshoots = [[[800,100],[0,0],1]]
    Pshoots = []

    step =0
    Mobs = []
    iMobs =[]
    started =1
    players =0
    window = Tk()
    window.title(title)
    canvas= Canvas(window,width=width,height=height,bg="black")
    canvas.grid(column=0,row=0)
    shootImage = PhotoImage(file = os.path.join("imgs","s.png"))
    MshootImage = PhotoImage(file = os.path.join("imgs","Ms.png"))
    window.bind_all("<KeyPress>", keypressed)
    window.bind_all("<KeyRelease>", keyreleased)

def create_Mob(image, spawnRate = 1):
    iMobs.append([image, spawnRate])

def create_player(x,y,image,movments="xy", physics=0):
    global players
    global Ppos
    global player
    global Pmovments
    global r
    global l
    global Pspeed
    global ri
    global le
    ri = 0
    le = 0
    l =0
    r=0
    Pspeed = 0
    player = canvas.create_image(x,y,image=image, anchor = "nw")
    if players >0 :
        sys.exit("one player supported at this moment !")
    print("creating player")
    players +=1
    Pmovments = movments
    Ppos = [x,y]

def Pmove(x,y):
    global Ppos
    if x<760 and x>0:
        Ppos = [x,y]
        canvas.coords(player,Ppos[0],Ppos[1])


def keypressed(arg):
	global r
	global l

	if arg.keysym == 'Left':
		l = 1
	elif arg.keysym == 'Right':
		r = 1

def keyreleased(arg):
	global r
	global l

	if arg.keysym == 'Left':
		l = 0
	elif arg.keysym == 'Right':
		r = 0

def Pshoot(pos ,vector = [0,-10]):
    s = canvas.create_image(pos[0],pos[1],image=shootImage, anchor = "nw")
    global Pshoots
    Pshoots.append([[pos[0],pos[1]],vector,s])

def Mshoot(pos ,vector = [0,10]):
    s = canvas.create_image(pos[0],pos[1],image=MshootImage, anchor = "nw")
    global Mshoots
    Mshoots.append([[pos[0],pos[1]],vector,s])

def delMshoot(index):
    global Mshoots
    canvas.delete(Mshoots[index][2])
    del Mshoots[index]

def delPshoot(index):
    global Pshoots
    canvas.delete(Pshoots[index][2])
    del Pshoots[index]



def update():
    global Ppos
    global Pspeed
    global r
    global l
    global ri
    global le
    global step
    global Mshoots
    global Pshoots
    global Mdir
    global phase
    if len(Mobs)==0 :
        sys.exit("you win !")
    if step%50 == 0:
        phase+=1
        if phase%9 == 0:
            Mdir*=-1

        for j in range(-1,len(Mobs)-1):
            if j==-1:
                j=len(Mobs)-1
            if randrange(10)==1:
                vector = [0,0]
                vector[0] = randrange(-5,5)
                vector[1] = randrange(5,10)
                Mshoot([Mobs[j][1][0]+15,Mobs[j][1][1]+40],vector)
            if phase%9 == 0:
                Mobs[j][1][1]+=5
            else:
                Mobs[j][1][0]+=5*Mdir
            canvas.coords(Mobs[j][0],Mobs[j][1][0],Mobs[j][1][1])
    if step%10 == 0 :
        Pshoot([Ppos[0]+15,Ppos[1]-10])
    i = 0
    for s in Mshoots:
        Mshoots[i][0][0]+=Mshoots[i][1][0]
        Mshoots[i][0][1]+=Mshoots[i][1][1]
        canvas.coords(Mshoots[i][2],Mshoots[i][0][0],Mshoots[i][0][1])
        if Mshoots[i][0][1]> Ppos[1] and Mshoots[i][0][1]<Ppos[1]+40 :
            if Mshoots[i][0][0]> Ppos[0] and Mshoots[i][0][0]<Ppos[0]+40 :
                sys.exit("you loose !")
        if Mshoots[i][0][1]> 800:
            delMshoot(i)
        i+=1

    i=0
    for s in Pshoots:
        Pshoots[i][0][0]+=Pshoots[i][1][0]
        Pshoots[i][0][1]+=Pshoots[i][1][1]
        canvas.coords(Pshoots[i][2],Pshoots[i][0][0],Pshoots[i][0][1])
        for j in range(-1,len(Mobs)-1):
            if j==-1:
                j=len(Mobs)-1

            if Pshoots[i][0][1] >= Mobs[j][1][1] and Pshoots[i][0][1] <= Mobs[j][1][1]+40:
                if Pshoots[i][0][0] <= Mobs[j][1][0]+40 and Pshoots[i][0][0]+10 >= Mobs[j][1][0]:
                    canvas.delete(Mobs[j][0])
                    del Mobs[j]
                    delPshoot(i)
        if Pshoots[i][0][1]<0:
            delPshoot(i)

        i+=1
    if r ==1 :
        if ri < 10:
            ri += 2
    else:
        if ri > 0 and step%5 == 0:
            ri -=2

    if l==1:
        if le < 10:
            le += 2
    else :
        if le > 0 and step%5 == 0:
            le -=2
    Pspeed = ri-le
    Pmove(Ppos[0]+Pspeed,Ppos[1])
    window.after(16,update)
    step +=1




























#
#
#
# class personnage():
#     """docstring forpersonnage."""
#     personnages = 0
#     def __init__(self, canvas,x, y, image):
#         if personnage.personnages == 0:
#             personnage.positionx = x
#             personnage.positiony = y
#             personnage.personnage = canvas.create_image(x,y,image = image)
#         personnage.personnages+=1
#     def move(self,canvas,x,y):
#         personnage.positionx = x
#         personnage.positiony = y
#         canvas.coords(self,x,y)
#
#
#
#
#
# class game():
#     """docstring for """
#
#     def update():
#         game.window.after(16,game.update)
#     def right(evt):
#         personnage.move(personnage,game.canvas,personnage.positionx+10,personnage.positiony)
#     def left(evt):
#         personnage.move(personnage,game.canvas,personnage.positionx-10,personnage.positiony)
#     def start(arg):
#         game.window.bind_all("<Left>", game.left)
#         game.window.bind_all("<Right>", game.right)
#         game.update()
#         game.window.mainloop()
#
#     def __init__(self, width=800, height=600):
#         game.window = Tk()
#         game.window.title("space colonizer")
#
#         game.canvas= Canvas(game.window,width=800,height=600,bg="black")
#         game.canvas.grid(column=0,row=0)
