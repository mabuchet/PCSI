"""
Auteur : Marc-Antoine BUCHET
Date : 01/03/2021

BUT :
Tracer les trajectoires dans le cas d'une chute libre pour différents angles
de lancer.

Seconde version pour n'avoir que les parties de trajectoires au-dessus du sol.
Pour cela, on construit pas à pas les listes d'abscisses et d'ordonnées et
on s'arrète dès que l'ordonnée est négative => boucle while
"""

import numpy as np
import matplotlib.pyplot as plt

plt.ion() # activation du mode interactif de pyplot

## Paramètres physiques :
g = 9.8 # m.s^-2, accélération de la pesanteur
v0 = 10 # m.s^-1, vitesse initiale
angles_de_lancer = [ np.pi/10 , np.pi/6 , np.pi/5 , np.pi/4 , 3*np.pi/10 ,
                     np.pi/3 , 2*np.pi/5]
labels = ['pi/10' , 'pi/6' , 'pi/5' , 'pi/4', '3pi/10' , 'pi/3'  , '2pi/5' ]

## Paramètres numériques :
""" On s'attend à ce que la portée soit d'un ordre de grandeur compris entre
le mètre et la dizaine de mètres au plus. Choisir un pas en abscisse de l'ordre
du centimètre semble donc pertinent (on aura au moins une centaine de points et
au plus quelques miliers, valeurs raisonnables dans les deux cas pour avoir des
graphes suffisamment lisses mais sans trop de points)."""
dx = 1.e-2 # m, pas en abscisse

## Équation de la trajectoire :
def ordonnees(x,a,v0) :
    """
    Calcule l'ordonnée de la trajectoire en fonction de :
    - l'abscisse 'x' (flottant ou tableau numpy)
    - l'angle de lancé 'a' (flottant, compris entre 0 et pi/2)
    - la norme de la vitesse initiale v0 (flottant, positif).
    """
    return np.tan(a)*x-0.5*g*x**2/(v0*np.cos(a))**2

## Représentations graphiques :
fig = plt.figure() # Génération de la figure

for a,l in zip(angles_de_lancer,labels) : # on fait une boucle sur les angles
    # Initialisation des listes x et y avec les conditions initiales :
    x = [0]
    y = [ordonnees(0,a,v0)]
    while y[-1]>=0 :
        # Remplissage des listes x et y
        nouveau_x = x[-1]+dx
        nouveau_y = ordonnees(nouveau_x,a,v0)
        x.append(nouveau_x)
        y.append(nouveau_y)
    # Vérification du nombre de points pour chaque graphe (au cas où) :
    print("alpha = {0}, nombre de points = {1}".format(l,len(x)))
    # Graphique pour l'angle étudié :
    plt.plot(x,y,label='alpha = {0}'.format(l))

plt.xlabel('x en m')
plt.ylabel('y en m')
plt.legend()
plt.grid()