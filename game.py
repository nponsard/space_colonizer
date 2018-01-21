from tkinter import *
import sys

def start():
    global iMobs
    global Mobs
    x=2
    y=2
    for i in range(20):
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
    shootImage = PhotoImage(file = "imgs\\s.png")
    window.bind_all("<Left>", left)
    window.bind_all("<Right>", right)

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




def right(arg):
    global r
    r = 1
#    global Ppos
#    Pmove(Ppos[0]+10,Ppos[1])
def left(arg):
    global l
    l = 1
#    global Ppos
#    Pmove(Ppos[0]-10,Ppos[1])


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
    if step%10 == 0 :
        shoot(Ppos)
    i = 0
    for s in shoots:
        shoots[i][1]-=10
        canvas.coords(shoots[i][2],shoots[i][0],shoots[i][1])
        for j in range(1,len(Mobs)):
            print(len(Mobs))
            if len(Mobs)==1 :
                print(Mobs)

            if shoots[i][0] <= Mobs[j-1][1][0]+40 and shoots[i][0]+10 >= Mobs[j-1][1][0] and shoots[i][1] >= Mobs[j-1][1][1] and shoots[i][1] <= Mobs[j-1][1][1]+40:
                canvas.delete(Mobs[j-1][0])
                del Mobs[j-1]
                delShoot(i)
        if shoots[i][1]<0:
            delShoot(i)

        i+=1
    if r ==1 :
        if ri < 10:
            ri += 2
        r = 0
    else:
        if ri > 0 and step%5 == 0:
            ri -=2

    if l==1:
        if le < 10:
            le += 2
        l=0
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
