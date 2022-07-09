import pyxel
pyxel.init(128, 128)
pyxel.load("test.pyxres")

tete = [64, 64, [48, 8]] # x y [u, v]
options_tete = [[48, 8], [56, 8], [40, 16], [48, 16]] # R L D U


def update():

    global tete

    # ferme la fenêtre avec la touche q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # fait avancer tete
    if tete[2] == options_tete[0] and (tete[0]<112) :
        tete[0] += 1
    if tete[2] == options_tete[1] and (tete[0]>8) :
        tete[0] -= 1
    if tete[2] == options_tete[2] and (tete[1]<112) :
        tete[1] += 1
    if tete[2] == options_tete[3] and (tete[1]>8) :
        tete[1] -= 1

    # changer direction tete
    if pyxel.btnp(pyxel.KEY_RIGHT) and not tete[2] == options_tete[1]:
        while tete[1] % 8 != 0:
            if tete[2] == options_tete[3]:
                tete[1] -= 1
            else:
                tete[1] += 1
        tete[2] = options_tete[0]
    if pyxel.btnp(pyxel.KEY_LEFT) and not tete[2] == options_tete[0]:
        while tete[1] % 8 != 0:
            if tete[2] == options_tete[3]:
                tete[1] -= 1
            elif tete[2] == options_tete[2]:
                tete[1] += 1
        tete[2] = options_tete[1]
    if pyxel.btnp(pyxel.KEY_UP) and not tete[2] == options_tete[2]:
        while tete[0] % 8 != 0:
            if tete[2] == options_tete[0]:
                tete[0] += 1
            else:
                tete[0] -= 1
        tete[2] = options_tete[3]
    if pyxel.btnp(pyxel.KEY_DOWN) and not tete[2] == options_tete[3]:
        while tete[0] % 8 != 0:
            if tete[2] == options_tete[0]:
                tete[0] += 1
            else:
                tete[0] -= 1
        tete[2] = options_tete[2]

def draw():

    global tete

    #background
    pyxel.bltm(0, 0, 0, 128, 128, 128, 128)

    #snake base
    pyxel.blt(tete[0], tete[1], 0, tete[2][0], tete[2][1], 8, 8, False)

pyxel.run(update, draw)
