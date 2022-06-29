"""
THE CRAZY ADVENTURES OF PINK CANDY

Le joueur contrôle un bonbon rose à travers diverses aventures.

Dans le menu des niveaux :
avec la touche V on arrive dans les vestiaires, où on peut choisir avec les flèches un costume pour le bonbon, qui sera sélectionné en pressant sur ENTER
avec la touche L on accède au mode libre, où tous les niveaux sont déjà accessibles
avec la touche N on joue dans le mode normal, c'est-à-dire qu’il faut réussir un niveau pour débloquer le suivant. La progression est enregistrée.
En cliquant sur les numéros des niveaux disponibles on lance le jeu auquel correspond le chiffre.

À tout moment, vous pouvez revenir au menu en cliquant sur la touche M.
La touche Q vous permet de quitter le jeu.

Nous vous proposons également une petite mélodie de qualité :)

Cordialement, team XIAOLONGBAO

"""

import pyxel
import random
pyxel.init(128, 128)
pyxel.load("xiaolongbao.pyxres")

s = 0
bg = [[0, 0], [128, 0], [256, 0], [384, 0], [512, 0], [640, 0], [128, 128], [128, 256], [128, 384], [128, 512], [128, 640],
#      start     1      2         3        4        V        1exp     1, 1       1, 2,      1, 3     1, niv+
#       0        1        2       3       4         5         6        7          8          9        10
[256, 128], [256, 256], [256, 384], [256, 512],
# 2, exp      2, 1   2, niv+      2, 2
#  11         12       13        14
[384, 128], [384, 256], [384, 384], [384, 512], [384, 640],
# 3, exp      3, 1     3, 2      3, 3     3, niv+
#   15       16        17        18       19
[512, 128], [512, 256], [512, 384], [512, 512], [512, 640]]
# 4, exp      4, 1     4, 2      4, 3     4, niv+
#  20       21        22        23        24

x = 57
y = 100
play = "normal"
xchoix = 16
ychoix = 56
bonbon = 0
costumes = [[16, 56], 0, [32, 56], 8, [48, 56], 16, [64, 56], 24, [80, 56], 32, [96, 56], 40,
[16, 80], 48, [32, 80], 56, [48, 80], 64, [64, 80], 72, [80, 80], 80, [96, 80], 88,
[16, 104], 96, [32, 104], 104, [48, 104], 112, [64, 104], 120, [80, 104], 128, [96, 104], 136]
mechant = []
time = 60
pistolet = 64
piou = []
remember = 1
att = 0
hs = 0
liste = [[4, -1],[4, -2],[4, -3],[4, -4],[3, -4],[2, -4],[1, -4],[0, -4],[-1, -4],[-2, -4],[-3, -4],[-4, -4],[-4, -3],[-4, -2],[-4, -1],[-4, 0],[-4, 1],[-4, 2],[-4, 3],[-4, 4],[-3, 4],[-2, 4],[-1, 4],[0, 4],[1, 4],[2, 4],[3, 4],[4, 4],[4, 3],[4, 2],[4, 1],[4, 0]]
cercle = 0
carre = []
xcarre = 0
ycarre = 0

def update():

    global s, x, y, play, remember, xchoix, ychoix, bonbon, mechant, time, pistolet, piou, carre, xcarre, ycarre, remember, att, hs, cercle

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if s==0:
        x+=2
        if x>130:
            x=-10
        if pyxel.btnp(pyxel.KEY_S):
            s = 1

    if s>0 and pyxel.btnp(pyxel.KEY_M):
        if play == "normal":
            s = remember
        elif play == "libre":
            s = 4

    if s<4 and pyxel.btnp(pyxel.KEY_L):
        play = "libre"
        remember = s
        s = 4
    if s<=4 and pyxel.btnp(pyxel.KEY_N):
        s = remember
        play = "normal"

    if s>0 and s<5 and pyxel.btnp(pyxel.KEY_1):
        s = 6
    if s>1 and s<5 and pyxel.btnp(pyxel.KEY_2):
        s = 11
    if s>2 and s<5 and pyxel.btnp(pyxel.KEY_3):
        s = 15
    if s==4 and pyxel.btnp(pyxel.KEY_4):
        s = 20

    if s>0 and s<5 and pyxel.btnp(pyxel.KEY_V):
        s = 5

    if s==5:
        if xchoix < 96 and pyxel.btnp(pyxel.KEY_RIGHT):
            xchoix += 16
        if xchoix > 16 and pyxel.btnp(pyxel.KEY_LEFT):
            xchoix -= 16
        if ychoix < 104 and pyxel.btnp(pyxel.KEY_DOWN):
            ychoix += 24
        if ychoix > 56 and pyxel.btnp(pyxel.KEY_UP):
            ychoix -= 24
        if pyxel.btnp(pyxel.KEY_RETURN):
            bonbon = costumes[costumes.index([xchoix, ychoix])+1]
            if play == "normal":
                s = remember
            elif play == "libre":
                s = 4

    def collision_droite(couleur, x, y):
        for i in range(8):
            if pyxel.pget(x+8, y+i) == couleur:
                return True
        return False
    def collision_gauche(couleur, x, y):
        for i in range(8):
            if pyxel.pget(x-1, y+i) == couleur:
                return True
        return False
    def collision_haut(couleur, x, y):
        for i in range(8):
            if pyxel.pget(x+i, y-1) == couleur:
                return True
        return False
    def collision_bas(couleur, x, y):
        for i in range(8):
            if pyxel.pget(x+i, y+8) == couleur:
                return True
        return False

    def create_mechant(param):
        b = random.choice([0, 8, 16, 24, 32, 40])
        if param == 1:
            a = random.randint(1, 4)
            if a == 1:
                 mechant.append([random.randint(14, 120), -10, a, b])
            if a == 2:
                 mechant.append([random.randint(14, 120), 130, a, b])
            if a == 3:
                 mechant.append([-10, random.randint(-10, 120), a, b])
            if a == 4:
                 mechant.append([130, random.randint(14, 120), a, b])
        if param==2:
            mechant.append([128, random.choice([16, 40, 64, 88, 112]), b])

#labyrinthe

    if s==6 and pyxel.btnp(pyxel.KEY_P):
        s = 7
        x = 0
        y = 0
        mechant = []

    if s==7 or s==8 or s==9:
        carre = []
        for i in range(32):
            for j in range(32):
                xcarre = i*4
                ycarre = j*4
                if abs(xcarre-x)>10 and abs(ycarre-y)>10:
                    carre.append([xcarre, ycarre])
        if pyxel.frame_count%4 == 0:
            for i in mechant:
                if i[2] == 1:
                    i[1]+=1
                if i[2] == 2:
                    i[1]-=1
                if i[2] == 3:
                    i[0]+=1
                if i[2] == 4 :
                    i[0]-=1
        if pyxel.frame_count%65==0:
            create_mechant(1)
        if pyxel.btn(pyxel.KEY_RIGHT) and not collision_droite(7, x, y) and x<120:
            x+=1
        if pyxel.btn(pyxel.KEY_LEFT) and not collision_gauche(7, x, y) and x>0:
            x-=1
        if pyxel.btn(pyxel.KEY_UP) and not collision_haut(7, x, y) and y>0:
            y-=1
        if pyxel.btn(pyxel.KEY_DOWN) and not collision_bas(7, x, y) and y<120:
            y+=1
        if collision_droite(10, x, y) or collision_gauche(10, x, y) or collision_haut(10, x, y) or collision_bas(10, x, y) or collision_droite(2, x, y) or collision_gauche(2, x, y) or collision_haut(2, x, y) or collision_bas(2, x, y) or collision_droite(3, x, y) or collision_gauche(3, x, y) or collision_haut(3, x, y) or collision_bas(3, x, y):
            x=0
            y=0
            mechant=[]
        if pyxel.pget(x, y) == 11:
            x=0
            y=0
            s+=1
            mechant = []

    if s==10 and play=="normal":
        remember = 2

#gameboy

    if s == 11 and pyxel.btnp(pyxel.KEY_P):
        mechant = []
        s = 12
        x = 0
        y = 56
        time = 60
        pistolet = 64
        hs = 0
    if s==12 or s==14:
        if pyxel.frame_count%30 == 0 and s==12:
            time -=1
        if pyxel.frame_count%30 == 0 and s==14:
            time +=1
            if time>hs:
                hs = time
        if pyxel.frame_count%2 == 0:
            for i in mechant:
                i[0] -= 1
                if i[0] == 39:
                    mechant = []
                    if s==12:
                        time = 60
                    elif s==14:
                        time = 0
        if pyxel.frame_count%25==0:
            create_mechant(2)
        if pyxel.frame_count%25 == 0:
            create_mechant(2)
        if pistolet==40 and pyxel.btnp(pyxel.KEY_UP):
            pistolet = 16
        if pistolet==64 and pyxel.btnp(pyxel.KEY_UP):
            pistolet = 40
        if pistolet==88 and pyxel.btnp(pyxel.KEY_UP):
            pistolet = 64
        if pistolet==112 and pyxel.btnp(pyxel.KEY_UP):
            pistolet = 88
        if pistolet==88 and pyxel.btnp(pyxel.KEY_DOWN):
            pistolet = 112
        if pistolet==64 and pyxel.btnp(pyxel.KEY_DOWN):
            pistolet = 88
        if pistolet==40 and pyxel.btnp(pyxel.KEY_DOWN):
            pistolet = 64
        if pistolet==16 and pyxel.btnp(pyxel.KEY_DOWN):
            pistolet = 40
        if time == 0 and s==12:
            s=13
            if play == "normal":
                remember = 3
            time = 0
            mechant = []
            pistolet = 64
        if pyxel.btnp(pyxel.KEY_SPACE):
            piou.append([40, pistolet])
        for i in piou:
            i[0]+=1
            for j in mechant:
                if (i[0]+7 == j[0] or i[0]+8 == j[0] or i[0]+6 == j[0]) and i[1] == j[1]:
                    i[1] = -20
                    j[0] = -20

    if s==13 and pyxel.btnp(pyxel.KEY_C):
        s=14
        pistolet = 64

#tenet

    if s==15 and pyxel.btnp(pyxel.KEY_P):
        s=16
        x=[48, 120]
        y=[120, 120]
    if s==16 and x==[0, 72] and y==[0, 0]:
        s=17
        x=[0, 120]
        y=[120, 0]
    if s==17 and x==[32, 88] and y==[8, 112]:
        s=18
        x=[24, 72]
        y=[104, 56]
    if s==18 and x==[8, 120] and y==[8, 64]:
        s=19

    if s==16 or s==17 or s==18:
        if pyxel.btn(pyxel.KEY_RIGHT):
            if s==18 and not collision_gauche(7, x[1], y[1]):
                x[1] -= 1
            elif not s == 18 and x[1]<120 and not collision_droite(7, x[1], y[1]):
                x[1] += 1
            if not collision_droite(7, x[0], y[0]):
                x[0] += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            if s==18 and not collision_droite(7, x[1], y[1]) and x[1]<120:
                x[1] += 1
            elif not s == 18 and not collision_gauche(7, x[1], y[1]):
                x[1] -= 1
            if not collision_gauche(7, x[0], y[0]) and x[0]>0:
                x[0] -= 1
        if pyxel.btn(pyxel.KEY_UP):
            if s==18 and not collision_bas(7, x[1], y[1]) and y[1]<120:
                y[1] += 1
            elif not s == 18 and y[1]>0 and not collision_haut(7, x[1], y[1]):
                y[1] -= 1
            if not collision_haut(7, x[0], y[0]) and y[0]>0:
                y[0] -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            if s==18 and not collision_haut(7, x[1], y[1]) and y[1]>0:
                y[1] -= 1
            elif not s == 18 and y[1]<120 and not collision_bas(7, x[1], y[1]):
                y[1] += 1
            if not collision_bas(7, x[0], y[0]) and y[0]<120:
                y[0] += 1

    if s==19 and play == "normal":
        remember = 4

#bounce

    if s==20:
        x=60
        y=120
        if pyxel.btnp(pyxel.KEY_P):
            s=21
        mechant = []
    if s==21 or s==22 or s==23:
        if y<=-8:
            if s==22:
                mechant = [[60, 100], [35, 56], [100, 56]]
                cercle = 0
            else:
                mechant = []
            s+=1
            x = 60
            y = 120
        if pyxel.btnp(pyxel.KEY_SPACE):
            att = 8
        if att>0:
            y-=2
            att -=1
        if y<120:
            y+=1
        if collision_droite(11, x, y) or collision_gauche(11, x, y) or collision_haut(11, x, y) or collision_bas(11, x, y):
            y = 120

    if s==21:
        if pyxel.frame_count%30==0:
            mechant.append([128, random.randint(0, 105), [24, 24]])
        for i in mechant:
            i[0]-=1
    if s==22:
        if pyxel.frame_count%60==0:
            mechant.append([-8, 70, [32, 0]])
            mechant.append([-8, 40, [32, 0]])
            mechant.append([-8, 10, [32, 0]])
        for i in mechant:
            i[0]+=4
            i[1]+=1
    if s==23:
        if pyxel.frame_count%2==0:
            for i in mechant:
                i[0]+=liste[cercle][0]
                i[1]+=liste[cercle][1]
            cercle +=1
            if cercle > 31:
                cercle = 0

def draw():

    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, bg[s][0], bg[s][1], 128, 128)

    if s==0:
        pyxel.blt(x, y, 0, 8, 0, 8, 8, False)
        pyxel.text(33, 55, "S pour COMMENCER", 0)
    if s<=4 and s>0:
        pyxel.text(5, 5, "N : NORMAL", 8)
        pyxel.text(87, 5, "L : LIBRE", 3)
        pyxel.text(40, 122, "V : vestiaires", 7)
    if s==5:
        pyxel.text(42, 18, "VESTIAIRES", 0)
        pyxel.blt(xchoix, ychoix, 0, 24, 16, 8, 8, False)
    if s == 6:
        pyxel.text(45, 30, "LABYRINTHE", 0)
        pyxel.text(20, 50, "arrivez au carre vert", 0)
        pyxel.text(18, 70, "sans vous faire toucher", 0)
        pyxel.text(42, 90, "P : commencer", 0)
    if s==7 or s==8 or s==9 :
        pyxel.blt(x, y, 0, 8, bonbon, 8, 8, False)
        for i in mechant:
            pyxel.blt(i[0], i[1], 0, 16, i[3], 8, 8, False)
        for i in carre:
            pyxel.blt(i[0], i[1], 0, 0, 0, 4, 4)
    if s==10:
        pyxel.text(30, 40, "NIV 2 DISPONIBLE", 0)
        pyxel.text(48, 60, "M : menu", 0)
    if s==11:
        pyxel.text(49, 30, "GAMEBOY", 0)
        pyxel.text(7, 50, "HAUT BAS : bouger le pistolet", 0)
        pyxel.text(37, 70, "ESPACE : tirer ", 0)
        pyxel.text(39, 90, "P : commencer", 0)
    if s==12 or s==14:
        pyxel.text(115, 5, str(time), 7)
        pyxel.blt(x, y+8, 0, 8, bonbon, 8, 8, False)
        pyxel.blt(24, pistolet, 0, 24, 0, 8, 8, False)
        for i in mechant:
            pyxel.blt(i[0], i[1], 0, 16, i[2], 8, 8, False)
        for i in piou:
            pyxel.blt(i[0], i[1], 0, 24, 8, 8, 8, False)
    if s==13:
        pyxel.text(30, 40, "NIV 3 DISPONIBLE", 0)
        pyxel.text(48, 60, "M : menu", 0)
        pyxel.text(38, 80, "C : continuer", 0)
    if s==15:
        pyxel.text(49, 30, "MIROIR", 0)
        pyxel.text(23, 60, "dirigez les bonbons", 0)
        pyxel.text(39, 90, "P : commencer", 0)
    if s==16 or s==17 or s==18:
        pyxel.blt(x[0], y[0], 0, 8, bonbon, 8, 8, False)
        pyxel.blt(x[1], y[1], 0, 8, bonbon, 8, 8, False)
    if s==19:
        pyxel.text(30, 40, "NIV 4 DISPONIBLE", 0)
        pyxel.text(48, 60, "M : menu", 0)
    if s==20:
        pyxel.text(49, 30, "BOUNCE", 0)
        pyxel.text(34, 60, "ESPACE : monter", 0)
        pyxel.text(39, 90, "P : commencer", 0)
    if s==21 or s==22 or s==23:
        pyxel.blt(x, y, 0, 8, bonbon, 8, 8, False)
    if s==24:
        pyxel.text(33, 65, "TOUT DISPONIBLE", 0)
        pyxel.text(48, 90, "M : menu", 0)
    if s==21:
        for i in mechant:
            pyxel.blt(i[0], i[1], 0, i[2][0], i[2][1], 32, 8)
    if s==22:
        for i in mechant:
            pyxel.blt(i[0], i[1], 0, i[2][0], i[2][1], 8, 8, False)
    if s==23:
        for i in mechant:
            pyxel.blt(i[0], i[1], 0, 32, 0, 8, 8, False)

pyxel.playm(2, loop = True)
pyxel.run(update, draw)
