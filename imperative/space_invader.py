import pyxel
from random import randint

# taille de la fenêtre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128)

x = 64                            # x original de gentil
y = 100                           # y original de gentil
l_piou = []
l_mechant = []
collision = 0                     # ==1 si collision gentil avec mechant
mechants_morts = 0                # nb de mechants morts
finale_gentil = [120, 0]          # co de gentil lorsque collision
co_finales_mechant = [0, 0, 0]    # co des mechants morts
radius = 2                        # rayon original de l'explosion de gentil
background = 0                    # augmente de 1 toutes les 15 frames, pour faire briller les étoiles
frequence_mechants = 60
pyxel.load("test.pyxres")

#choses à faire :
#accelerer vitesse piou à 30, 50, 70
#1 fois tous les 10 mechants un special arrive, ou un super pouvoir (cercle)
#mort quand nombre negatif depuis coordonnees gentil

pyxel.sound(3).speed = 12
pyxel.sound(4).speed = 12
pyxel.sound(5).speed = 12
pyxel.sound(6).speed = 12
pyxel.play(0, [3, 4, 5, 6], loop=True)

def update():

    global x, y, l_mechant, collision, mechants_morts, radius, finale_gentil, co_finales_mechant, frequence_mechants

    # deplacer gentil avec flèches
    if (pyxel.btn(pyxel.KEY_RIGHT)) and (x<120):
        x = x + 2
    if (pyxel.btn(pyxel.KEY_LEFT)) and (x>0):
        x = x - 2
    if (pyxel.btn(pyxel.KEY_UP)) and (y>0):
        y = y - 2
    if (pyxel.btn(pyxel.KEY_DOWN)) and (y<120):
        y = y + 2

    # ferme la fenêtre avec la touche q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # piou apparition
    if pyxel.btnp(pyxel.KEY_SPACE):
        l_piou.append([x + 4, y - 4])

    # faire descendre pious
    for i in range(len(l_piou)):
        l_piou[i][1] -= 2

    # mechant apparition
    if pyxel.frame_count % frequence_mechants == 0:
        l_mechant.append([randint(0,120), 0, 4])

    # fonction verifier collision
    def boum(a, b):
        if b[0] > a[0]+8 or b[1] > a[1]+8 or b[0]+8 < a[0] or b[1]+8 < a[1]:
            return False
        else:
            return True

    for i in range(len(l_mechant)):
        # -1 nb méchants morts si vivants quand arrivent en bas
        if l_mechant[i][0] > 0 and l_mechant[i][1] == 128 :
            mechants_morts -= 1
        # faire descendre méchants 
        l_mechant[i][1] += 1
        # si collision : fixer co finales de gentil pour explosion
        if boum(l_mechant[i], [x, y]) == True:
            collision = 1
            finale_gentil[0] = x + 4
            finale_gentil[1] = y + 4
        # enlever piou si touche méchant, enlever 1 vie méchant
        for j in range(len(l_piou)):
            if boum(l_mechant[i], l_piou[j]) == True:
                l_piou[j][1] = -10
                l_mechant[i][2] -=1
        # si méchant n'a plus de vie et qu'il est dans la fenêtre, +1 nb méchants morts
        if l_mechant[i][2] == 0 and l_mechant[i][0] > 0:
            mechants_morts += 1
            # accélérer fréquence d'apparition des méchants
            if mechants_morts < 20 :
                frequence_mechants = 60
            if mechants_morts >= 20 and mechants_morts < 40 :
                frequence_mechants = 50
            if mechants_morts >= 40 and mechants_morts < 60:
                frequence_mechants = 40
            if mechants_morts >= 60 and mechants_morts < 80 :
                frequence_mechants = 30
            if mechants_morts >= 80 :
                frequence_mechants = 20
            # fixer co finales méchants morts pour tête de mort
            co_finales_mechant[0] = l_mechant[i][0]
            co_finales_mechant[1] = l_mechant[i][1]
            # pour temps d'affichage des têtes de mort
            co_finales_mechant[2] = pyxel.frame_count
            # virer méchant de l'écran, éventuellement à remplacer par la suppresion du méchant de l_mechant
            l_mechant[i][0] = -10


def draw():

    global x, y, l_piou, l_mechant, collision, mechants_morts, radius, finale_gentil, background, co_finales_mechant

    # vide la fenêtre et fait alterner 2 backgrounds pour faire briller les étoiles
    if pyxel.frame_count % 15 == 0:
        background += 1
    if background % 2 == 0:
        pyxel.bltm(0, 0, 0, 64, 0, 128, 128)
    else:
        pyxel.bltm(0, 0, 0, 192, 0, 128, 128)

    # si gentil pas entré en collision avec méchant et nb méchants morts pas négatif (c les 2 conditions de vie de gentil)
    if collision == 0 and mechants_morts >= 0:
        # affiche gentil
        pyxel.blt(x, y, 0, 16, 0, 8, 8)
        # affiche pious
        for i in range(len(l_piou)):
            pyxel.blt(l_piou[i][0], l_piou[i][1], 0, 32, 4, 1, 4)
        # affiche mechants
        for i in range(len(l_mechant)):
            if l_mechant[i][2] > 0:
                pyxel.blt(l_mechant[i][0], l_mechant[i][1], 0, 24, 0, 8, 8)
            # si méchants touchés 4x, remplacés par tête de mort pdt 20 frames, elle sera ensuite virée de la fenêtre
            else:
                if pyxel.frame_count - co_finales_mechant[2] == 20:
                    co_finales_mechant[0] = -10
                pyxel.blt(co_finales_mechant[0], co_finales_mechant[1], 0, 56, 0, 8, 8)
    # si gentil mort, explosion et affichage GAME OVER
    else:
        pyxel.circ(finale_gentil[0], finale_gentil[1], radius, 7)
        radius += 2
        if radius > 150:
            pyxel.text(20, 90, "GAME OVER", 0)

    # affiche nb méchants morts
    # pas pour 0, tous les 10 méchants morts, et pas pour GAME OVER : nb affiché de toutes les couleurs qui alternent
    if mechants_morts > 0 and mechants_morts % 10 == 0 and collision == 0:
        pyxel.text(120, 3, str(mechants_morts), pyxel.frame_count % 16)
    else:
        pyxel.text(120, 3, str(mechants_morts), 7)


pyxel.run(update, draw)
