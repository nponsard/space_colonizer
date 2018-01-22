from tkinter import *
import sys
import os

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
        mob = canvas.create_image(x,y,image= iMobs[0][0] ,  anchor="nw")
        Mobs.append([mob,[x,y]])
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
    global shoots
    shoots = []
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

def shoot(Ppos):
    x=Ppos[0]+15
    y=Ppos[1]-10
    s = canvas.create_image(x,y,image=shootImage, anchor = "nw")
    global shoots
    shoots.append([x,y,s])
def delShoot(index):
    global shoots
    canvas.delete(shoots[index][2])
    del shoots[index]



def update():
    global Ppos
    global Pspeed
    global r
    global l
    global ri
    global le
    global step
    global shoots
    global Mdir
    global phase
    if step%50 == 0:
        phase+=1
        if phase%9 == 0:
            for j in range(-1,len(Mobs)-1):
                Mobs[j][1][1]+=5
                canvas.coords(Mobs[j][0],Mobs[j][1][0],Mobs[j][1][1])
            Mdir*=-1
        else:
            for j in range(-1,len(Mobs)-1):
                if j==-1:
                    j=len(Mobs)-1
                Mobs[j][1][0]+=5*Mdir
                canvas.coords(Mobs[j][0],Mobs[j][1][0],Mobs[j][1][1])
    if step%10 == 0 :
        shoot(Ppos)
    i = 0
    for s in shoots:
        shoots[i][1]-=10
        canvas.coords(shoots[i][2],shoots[i][0],shoots[i][1])
        for j in range(-1,len(Mobs)-1):
            if j==-1:
                j=len(Mobs)-1

            if shoots[i][1] >= Mobs[j][1][1] and shoots[i][1] <= Mobs[j][1][1]+40:
                if shoots[i][0] <= Mobs[j][1][0]+40 and shoots[i][0]+10 >= Mobs[j][1][0]:
                    canvas.delete(Mobs[j][0])
                    del Mobs[j]
                    delShoot(i)
        if shoots[i][1]<0:
            delShoot(i)

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
