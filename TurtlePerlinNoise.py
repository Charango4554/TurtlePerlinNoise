#Code written by Charango4554 (https://github.com/Charango4554)

import turtle
import numpy as np

width = int(input("insert the desired width:"))
height = int(input("insert the desired height:"))
octaves = 4

perlin_noise = np.random.rand(width, height)# génération d'une matrice aléatoire de valeurs de bruit de Perlin
t = turtle.Turtle()
t.speed(0)
t.penup()

#coin supérieur gauche:
t.setx(-width/2)
t.sety(height/2)

for x in range(width):
    for y in range(height):
         # utilisation de la valeur de la matrice pour définir la couleur de remplissage
        t.fillcolor(perlin_noise[x][y], perlin_noise[x][y], perlin_noise[x][y])
        t.begin_fill()
        for i in range(4):# boucle pour dessiner un carré de 1x1
            t.forward(1)
            t.right(90)
        t.end_fill()# fin de remplissage
        t.forward(1)
    t.setx(-width/2)# retour à la position de départ
    t.sety(t.ycor() - 1)# descente d'une ligne
turtle.exitonclick()
