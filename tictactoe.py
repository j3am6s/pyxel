import pyxel
pyxel.init(104, 104)
pyxel.load("test.pyxres")

tour = 1
cercles = []
croix = []
remplissage = [[17, 17], [49, 17], [81, 17],
               [17, 49], [49, 49], [81, 49],
               [17, 81], [49, 81], [81, 81]]
a = 0

def update():

    global tour, cercles, croix, a

    # ferme la fenêtre avec la touche q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def position(x, y):
        if x<32:
            if y<32:
                return [16, 16]
            elif y>68:
                return [16, 80]
            else:
                return [16, 48]
        elif x>68:
            if y<32:
                return [80, 16]
            elif y>68:
                return [80, 80]
            else:
                return [80, 48]
        else:
            if y<32:
                return [48, 16]
            elif y>68:
                return [48, 80]
            else:
                return [48, 48]

    def remplir(r):
        # cercle horizontal
        if pyxel.pget(r[0][0], r[0][1]) == 3 and pyxel.pget(r[1][0], r[1][1]) == 3 and pyxel.pget(r[2][0], r[2][1]) == 3:
            return 1
        if pyxel.pget(r[3][0], r[3][1]) == 3 and pyxel.pget(r[4][0], r[4][1]) == 3 and pyxel.pget(r[5][0], r[5][1]) == 3:
            return 1
        if pyxel.pget(r[6][0], r[6][1]) == 3 and pyxel.pget(r[7][0], r[7][1]) == 3 and pyxel.pget(r[8][0], r[8][1]) == 3:
            return 1
        # croix horizontale
        if pyxel.pget(r[0][0], r[0][1]) == 8 and pyxel.pget(r[1][0], r[1][1]) == 8 and pyxel.pget(r[2][0], r[2][1]) == 8:
            return 2
        if pyxel.pget(r[3][0], r[3][1]) == 8 and pyxel.pget(r[4][0], r[4][1]) == 8 and pyxel.pget(r[5][0], r[5][1]) == 8:
            return 2
        if pyxel.pget(r[6][0], r[6][1]) == 8 and pyxel.pget(r[7][0], r[7][1]) == 8 and pyxel.pget(r[8][0], r[8][1]) == 8:
            return 2
        # cercle vertical
        if pyxel.pget(r[0][0], r[0][1]) == 3 and pyxel.pget(r[3][0], r[3][1]) == 3 and pyxel.pget(r[6][0], r[6][1]) == 3:
            return 1
        if pyxel.pget(r[1][0], r[1][1]) == 3 and pyxel.pget(r[4][0], r[4][1]) == 3 and pyxel.pget(r[7][0], r[7][1]) == 3:
            return 1
        if pyxel.pget(r[2][0], r[2][1]) == 3 and pyxel.pget(r[5][0], r[5][1]) == 3 and pyxel.pget(r[8][0], r[8][1]) == 3:
            return 1
        # croix verticale
        if pyxel.pget(r[0][0], r[0][1]) == 8 and pyxel.pget(r[3][0], r[3][1]) == 8 and pyxel.pget(r[6][0], r[6][1]) == 8:
            return 2
        if pyxel.pget(r[1][0], r[1][1]) == 8 and pyxel.pget(r[4][0], r[4][1]) == 8 and pyxel.pget(r[7][0], r[7][1]) == 8:
            return 2
        if pyxel.pget(r[2][0], r[2][1]) == 8 and pyxel.pget(r[5][0], r[5][1]) == 8 and pyxel.pget(r[8][0], r[8][1]) == 8:
            return 2
        # cercle diagonale
        if pyxel.pget(r[0][0], r[0][1]) == 3 and pyxel.pget(r[4][0], r[4][1]) == 3 and pyxel.pget(r[8][0], r[8][1]) == 3:
            return 1
        if pyxel.pget(r[2][0], r[2][1]) == 3 and pyxel.pget(r[4][0], r[4][1]) == 3 and pyxel.pget(r[6][0], r[6][1]) == 3:
            return 1
        # croix diagonale
        if pyxel.pget(r[0][0], r[0][1]) == 8 and pyxel.pget(r[4][0], r[4][1]) == 8 and pyxel.pget(r[8][0], r[8][1]) == 8:
            return 2
        if pyxel.pget(r[2][0], r[2][1]) == 8 and pyxel.pget(r[4][0], r[4][1]) == 8 and pyxel.pget(r[6][0], r[6][1]) == 8:
            return 2

    #vérifier victoire
    if remplir(remplissage) == 1 and tour<=10:
        tour = 11
        a = pyxel.frame_count
    elif remplir(remplissage) == 2 and tour<=10:
        tour = 12
        a = pyxel.frame_count

    #poser cercle
    if tour % 2 == 1 and pyxel.btnp(pyxel.KEY_A):
        if pyxel.pget(position(pyxel.mouse_x, pyxel.mouse_y)[0], position(pyxel.mouse_x, pyxel.mouse_y)[1]) == 6:
            cercles.append(position(pyxel.mouse_x, pyxel.mouse_y))
            tour += 1
            if tour == 10:
                a = pyxel.frame_count

    #poser croix
    if tour % 2 == 0 and pyxel.btnp(pyxel.KEY_B):
        if pyxel.pget(position(pyxel.mouse_x, pyxel.mouse_y)[0], position(pyxel.mouse_x, pyxel.mouse_y)[1]) == 6:
            croix.append(position(pyxel.mouse_x, pyxel.mouse_y))
            tour += 1
            if tour == 10:
                a = pyxel.frame_count

    if a>0 and pyxel.frame_count - a == 50:
        tour += 3


def draw():

    global tour, cercles, croix

    #background
    pyxel.bltm(0, 0, 0, 32, 32, 13, 13)

    #cercles présents
    for i in range(len(cercles)):
        pyxel.blt(cercles[i][0], cercles[i][1], 0, 16, 24, 8, 8, False)

    #croix présentes
    for i in range(len(croix)):
        pyxel.blt(croix[i][0], croix[i][1], 0, 24, 24, 8, 8, False)

    #cercle en attente
    if tour % 2 == 1 and pyxel.frame_count % 10 != 0 and tour < 10:
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 88, 24, 8, 8, False)

    #croix en attente
    if tour % 2 == 0 and pyxel.frame_count % 10 != 0 and tour < 10:
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 96, 24, 8, 8, False)

    if tour >= 13:
        # changer background
        pyxel.bltm(0, 0, 0, 48, 32, 13, 13)
        # égalité
        if tour == 13:
            pyxel.blt(40, 48, 0, 16, 24, 8, 8, False)
            pyxel.blt(57, 48, 0, 24, 24, 8, 8, False)
        # cercle gagne
        if tour == 14:
            pyxel.blt(48, 48, 0, 16, 24, 8, 8, False)
            pyxel.blt(48, 36, 0, 104, 24, 8, 8, False)
        # croix gagne
        if tour == 15:
            pyxel.blt(48, 48, 0, 24, 24, 8, 8, False)
            pyxel.blt(48, 36, 0, 104, 24, 8, 8, False)

pyxel.run(update, draw)
