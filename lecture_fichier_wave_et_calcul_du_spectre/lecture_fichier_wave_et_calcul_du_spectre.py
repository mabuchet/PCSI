"""
Auteur : Marc-Antoine BUCHET
Date : 22/03/2022

BUT :
Ouvrir un fichier wav et tracer le graphe, puis calculer le spectre.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile

## Paramétrage des graphes :
plt.rc('font', weight="bold",size=12)

## Lecture des données :
fichier='triangle.wav'
rate,data=scipy.io.wavfile.read(fichier)
facteur_de_normalisation=10000. # le choix semble arbitraire
s1=data[:,0]/facteur_de_normalisation
s2=data[:,1]/facteur_de_normalisation

## Calcul des abscisses :
N=len(s1)
dt=1./rate
T=(N-1)*dt
t=np.linspace(0,T,N)

## Graphe :
figname='triangle_temporel'
fig=plt.figure(figname)
plt.plot(t,s1)
plt.xlabel('t en s')
plt.ylabel('signal en u.a.')
plt.draw()
plt.tight_layout()
plt.show()

## Spectre :
spectre=np.fft.rfft(s1)
f=np.fft.rfftfreq(N,1./rate)
figname='triangle_spectre'
fig=plt.figure(figname)
plt.plot(f,abs(spectre))
plt.xscale('log')
plt.yscale('log')
plt.xlabel('f (Hz)')
plt.ylabel('Spectre')
plt.grid()
plt.draw()
plt.tight_layout()
plt.show()
