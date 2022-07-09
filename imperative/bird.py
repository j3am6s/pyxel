import pyxel
from random import randint
pyxel.init(128, 128)
pyxel.load("test.pyxres")

x = 8
y = 112
u = 40
direction = 0
ailes = 0
tour = 0
pieces = []
b = 0

def update():

    global x, y, u, direction, ailes, tour, pieces, b

    # ferme la fenêtre avec la touche q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    #change direction + droite gauche
    if pyxel.btn(pyxel.KEY_RIGHT):
        direction = 0
        if x<112:
            x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        direction = 1
        if x>8:
            x -= 1

    #monter espace
    if pyxel.btnp(pyxel.KEY_SPACE):
        b = 0
        if y>=16:
            b = 8
    if b > 0:
        y -= 2
        b -= 1

    #descendre constamment
    if y<112:
        y += 1

    #battent des ailes
    if pyxel.frame_count % 10 == 0 :
        if ailes == 0:
            ailes = 1
        else:
            ailes = 0
    if direction == 0:
        if ailes == 0:
            u = 40
        else:
            u = 48
    else:
        if ailes == 0:
            u = 16
        else:
            u = 24

    if pieces == [] :
        tour += 1
        for i in range(tour):
            pieces.append([randint(8, 112), randint(8, 112)])

    # fonction verifier collision
    def boum(a1, a2, b):
        if b[0] > a1+8 or b[1] > a2+8 or b[0]+6 < a1 or b[1]+6 < a2:
            return False
        else:
            return True

    for i in range(len(pieces)):
         if boum(x, y, pieces[i]):
            pieces[i][0] = -20

    c = 0
    for j in range(len(pieces)):
        if pieces[j][0] == -20:
            c += 1
    if c == tour :
        pieces = []


def draw():

    global x, y, u, tour, pieces

    #background
    pyxel.bltm(0, 0, 0, 128, 128, 128, 128)

    #pieces
    if pyxel.frame_count % 15 != 0:
        if pieces != []:
            for i in range(len(pieces)):
                pyxel.blt(pieces[i][0], pieces[i][1], 0, 32, 32, 6, 6, False)

    #perso
    pyxel.blt(x, y, 0, u, 32, 8, 8, False)

    pyxel.text(110, 10, str(tour), 7)


pyxel.run(update, draw)
