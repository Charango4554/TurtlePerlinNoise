# TurtlePerlinNoise
Ce code utilise les bibliothèques Python "turtle" et "numpy" pour créer un dessin de bruit de Perlin (Perlin noise) dans une fenêtre Turtle. Il débute par définir la largeur et la hauteur de la fenêtre, ainsi que le nombre d'octaves à utiliser pour le bruit de Perlin.

Ensuite, il utilise la bibliothèque numpy pour générer une matrice aléatoire de valeurs de bruit de Perlin de la largeur et de la hauteur spécifiées. Cette matrice contiendra des valeurs aléatoires qui seront utilisées pour définir les couleurs de remplissage des carrés qui seront dessinés.

Il crée ensuite un objet turtle (appelé t) et règle sa vitesse à 0 (ce qui signifie qu'il dessine aussi rapidement que possible). Il soulève ensuite le crayon pour éviter de dessiner des lignes en se déplaçant. Il déplace ensuite le turtle à la position (-largeur / 2, hauteur / 2) pour commencer à dessiner dans le coin supérieur gauche de la fenêtre.

Il utilise ensuite deux boucles "for" imbriquées pour parcourir tous les pixels de la matrice de bruit de Perlin. À chaque pixel, il utilise la valeur de la matrice pour définir la couleur de remplissage du turtle (en utilisant la même valeur pour les composantes rouge, verte et bleue) et remplit un carré de 1x1 à l'aide de la boucle "for" interne. Il avance ensuite d'un pixel avant de continuer à dessiner le prochain carré. À la fin de chaque ligne, il ramène le turtle à sa position de départ pour la ligne suivante.

Enfin, Il utilise turtle.exitonclick() pour permettre à l'utilisateur de fermer la fenêtre en cliquant dessus.

_____________________________________________________________

This code uses the Python libraries "turtle" and "numpy" to create a Perlin noise drawing in a Turtle window. It starts by defining the width and height of the window, as well as the number of octaves to use for the Perlin noise.

Then it uses the numpy library to generate a random matrix of Perlin noise values of the specified width and height. This matrix will contain random values that will be used to define the fill colors of the squares that will be drawn.

It then creates a turtle object (called t) and sets its speed to 0 (meaning it draws as fast as possible). He then lifts the pencil to avoid drawing lines while moving. He then moves the turtle to the position (-width / 2, height / 2) to start drawing in the upper left corner of the window.

It then uses two nested "for" loops to traverse all the pixels in the Perlin noise matrix. At each pixel, he uses the value of the matrix to define the fill color of the turtle (using the same value for the red, green and blue components) and fills a 1x1 square using the internal "for" loop. It then moves forward one pixel before continuing to draw the next square. At the end of each line, he returns the turtle to its starting position for the next line.

Finally, it uses turtle.exitonclick() to allow the user to close the window by clicking on it.

Translated with www.DeepL.com/Translator (free version)
