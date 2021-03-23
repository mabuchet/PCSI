"""
Auteur : Marc-Antoine BUCHET
Date : 01/03/2021

BUT :
Tracer les trajectoires dans le cas d'une chute libre pour différents angles
de lancer.

Ici on ne se pose pas de questions : on trace tous les graphes avec les
mêmes abscisses en faisant en sorte d'avoir dépassé l'instant pour lequel le
mobile est passé en dessous du sol.
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
N = 1000 # nombre de points

## Calcul des abscisses :
x_min = 0. # m
x_max = 10 # m
x = np.linspace(x_min,x_max,N) # abscisses

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
    y = ordonnees(x,a,v0) # calcul des ordonnées correspondantes aux abscisses
    plt.plot(x,y,label='alpha = {0}'.format(l)) # Graphe pour l'angle étudié

plt.xlabel('x en m')
plt.ylabel('y en m')
plt.grid()
plt.legend()
