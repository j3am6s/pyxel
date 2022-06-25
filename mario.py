import pyxel
pyxel.init(128, 128)
pyxel.load("test.pyxres")

mario = [8, -20, [88, 48]]
menu = 0
fond = [32, 64]
xfond = 0
monter = 0
piece = []
nbpieces = 0
couleur = 0
instant = 0
unlocked = 1
moment = 0
mechant = [0]
contact = 0

def update():

    global mario, fond, xfond, monter, piece, nbpieces, couleur, instant, menu, unlocked, contact,  moment, mechant

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_M):
        menu = 0

    if xfond > -358 and menu == 1:

        moment += 1

        descendre = 1
        for i in range(12):
            if pyxel.pget(mario[0]+i, mario[1]+16) == 3 or pyxel.pget(mario[0]+i, mario[1]+16) == 4:
                descendre = 0
        if descendre == 1:
            mario[1] += 1
            if moment > 116:
                mario[1] += 1

        if moment >= 116:
            if (pyxel.btn(pyxel.KEY_RIGHT)) and (mario[0]<116):
                droite = 0
                for i in range(16):
                    if pyxel.pget(mario[0]+12, mario[1]+i) == 4 or pyxel.pget(mario[0]+12, mario[1]+i) == 3:
                        droite = 1
                if droite == 0:
                    mario[0] += 1
                if monter <= 0:
                    mario[2] = [88, 48]
                else:
                    mario[2] = [124, 48]
                if mechant[0] != 0 and mario[0] > 84:
                    for i in range(mechant[0]):
                        mechant[i+1][0] -= 0.5
            if (pyxel.btn(pyxel.KEY_LEFT)) and (mario[0]>0):
                gauche = 0
                for i in range(16):
                    if pyxel.pget(mario[0]-1, mario[1]+i) == 4 or pyxel.pget(mario[0]-1, mario[1]+i) == 3:
                        gauche = 1
                if gauche == 0:
                    mario[0] -= 1
                if monter <= 0:
                    mario[2] = [108, 48]
                else:
                    mario[2] = [137, 48]
                if mechant[0] != 0 and mario[0] < 42:
                    for i in range(mechant[0]):
                        mechant[i+1][0] += 0.8
            if monter > 0:
                if mario[2] == [108, 48]:
                    mario[2] = [137, 48]
                elif mario[2] == [88, 48]:
                    mario[2] = [124, 48]

        if mario[0] > 84 and xfond > -380:
            xfond -= 1
            mario[0] -= 1
        if mario[0] < 42 and xfond < 0 :
            xfond += 1
            mario[0] += 1

        if pyxel.btnp(pyxel.KEY_SPACE) and descendre == 0:
            monter = 20
        oui = 0
        for i in range(12):
            if pyxel.pget(mario[0]+i, mario[1]-1) == 4:
                monter = 0
                oui = 1
        if oui == 1:
            nbpieces += 1
            piece = [mario[0]+1, mario[1]-16, 10]
        if monter > 0:
            mario[1] -= 4
            monter -= 1

        if piece != []:
            if piece[2] >= 5:
                piece[1] -= 1
            elif piece[2] > 0:
                piece[1] += 1
            else:
                piece[0] = -10
            piece[2] -= 1

        if fond == [16, 80] and xfond == -145 and mechant[0] == 0:
            mechant.append([140, 104])
            mechant[0] = 1
        if fond == [16, 96] and xfond == -75 and mechant[0] == 0:
            mechant.append([140, 104])
            mechant[0] = 1
        if fond == [16, 96] and xfond == -150 and mechant[0] == 1:
            mechant.append([140, 104])
            mechant[0] = 2
        if fond == [16, 112] and xfond == -140 and mechant[0] == 0:
            mechant.append([140, 104])
            mechant[0] = 1
        if fond == [16, 112] and xfond == -230 and mechant[0] == 1:
            mechant.append([140, 104])
            mechant[0] = 2
        if fond == [16, 128] and xfond == -88 and mechant[0] == 0:
            mechant.append([140, 104])
            mechant[0] = 1
        if fond == [16, 128] and xfond == -180 and mechant[0] == 1:
            mechant.append([140, 104])
            mechant[0] = 2
        if mechant[0] != 0:
            for i in range(mechant[0]):
                mechant[i+1][0] -= 0.5
                mtn = 0
                touche = 0
                for j in range(8):
                    if pyxel.pget(mechant[i+1][0]+j, mechant[i+1][1]-1) == 8:
                        touche = 1
                if touche == 1:
                    mechant[i+1][0] = -100
                    monter = 10
                contact = 0
                for k in range(8):
                    if pyxel.pget(mechant[i+1][0]-1, mechant[i+1][1]+j) == 8 or pyxel.pget(mechant[i+1][0]+8, mechant[i+1][1]+j) == 8:
                        contact = 1
                if contact == 1:
                    menu = 0

    elif xfond == -358 and menu == 1:
        instant = moment
        xfond = -359
        moment += 1
    elif xfond <= -359 and menu == 1:
        moment += 1
        if moment - instant > 30 and moment - instant < 90:
            if xfond > -382:
                xfond -= 1
            if pyxel.pget(mario[0], mario[1]+16) != 3:
                mario[0] += 0.5
                mario[1] += 2
            elif pyxel.pget(mario[0]+10, mario[1]) != 0 and mario[0] < 110:
                mario[0] += 1
        if moment - instant == 90:
            mario[2] = [108, 48]
        if moment - instant == 100:
            menu = 0
            if unlocked == 1 and fond == [16, 80]:
                unlocked = 2
            elif unlocked == 2 and fond == [16, 96]:
                unlocked = 3
            elif unlocked == 3 and fond == [16, 112]:
                unlocked = 4

    if menu == 0:
        xfond = 0
        mario[1] = -20
        mario[0] = 8
        mario[2] = [88, 48]
        couleur = 0
        mechant = [0]
        fond[0] = 32
        fond[1] = 64
        contact = 0
        if pyxel.btnp(pyxel.KEY_1):
            menu = 1
            moment = 0
            fond = [16, 80]
            couleur = 7
        if pyxel.btnp(pyxel.KEY_2) and unlocked >= 2:
            menu = 1
            moment = 0
            fond = [16, 96]
            couleur = 7
        if pyxel.btnp(pyxel.KEY_3) and unlocked >= 3:
            menu = 1
            moment = 0
            fond = [16, 112]
            couleur = 0
        if pyxel.btnp(pyxel.KEY_4) and unlocked >= 4:
            menu = 1
            moment = 0
            fond = [16, 128]
            couleur = 7

def draw():

    pyxel.bltm(xfond, 0, 0, fond[0], fond[1], 64, 16)

    pyxel.blt(mario[0], mario[1], 0, mario[2][0], mario[2][1], 12, 16, False)

    if menu == 0 and unlocked == 1:
        pyxel.blt(17, 74, 0, 88, 64, 13, 13)
        pyxel.blt(39, 95, 0, 152, 64, 13, 13)
        pyxel.blt(67, 68, 0, 152, 64, 13, 13)
        pyxel.blt(95, 101, 0, 152, 64, 13, 13)
    if menu == 0 and unlocked == 2:
        pyxel.blt(17, 74, 0, 88, 64, 13, 13)
        pyxel.blt(39, 95, 0, 104, 64, 13, 13)
        pyxel.blt(67, 68, 0, 152, 64, 13, 13)
        pyxel.blt(95, 101, 0, 152, 64, 13, 13)
    if menu == 0 and unlocked == 3:
        pyxel.blt(17, 74, 0, 88, 64, 13, 13)
        pyxel.blt(39, 95, 0, 104, 64, 13, 13)
        pyxel.blt(67, 68, 0, 120, 64, 13, 13)
        pyxel.blt(95, 101, 0, 152, 64, 13, 13)
    if menu == 0 and unlocked >= 4:
        pyxel.blt(17, 74, 0, 88, 64, 13, 13)
        pyxel.blt(39, 95, 0, 104, 64, 13, 13)
        pyxel.blt(67, 68, 0, 120, 64, 13, 13)
        pyxel.blt(95, 101, 0, 136, 64, 13, 13)

    if mechant[0] != 0:
        for i in range(mechant[0]):
            pyxel.blt(mechant[i+1][0], mechant[i+1][1], 0, 64, 96, 8, 8, False)

    if piece != []:
        pyxel.blt(piece[0], piece[1], 0, 32, 32, 6, 6, False)

    pyxel.text(116, 8, str(nbpieces), couleur)

    if moment < 45 and menu == 1:
        pyxel.text(100, 80, "3", 0)
    if moment >= 45 and moment < 80 and menu == 1:
        pyxel.text(100, 80, "2", 0)
    if moment >= 80 and moment < 116 and menu == 1:
        pyxel.text(100, 80, "1", 0)
    if moment >= 116 and moment < 125 and menu == 1:
        pyxel.text(95, 80, "GO!", 0)
    if moment >= 130 and moment < 145 and menu == 1:
        pyxel.text(95, 80, "GO!", 0)

pyxel.run(update, draw)
