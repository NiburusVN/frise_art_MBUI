import random

"""
Frise Minecraft - NSI 1Ã¨re SpÃ©

Membres du groupe:
    -Pheakdey
    -Michel
    -Amine
"""

size(600, 400)

#Background de la premiÃ¨re ligne de la frise:
noStroke()
fill(0, 255, 255)
rect(0, 0, 300, 89)

'''
Nether 1ère frise à droite
'''

#Backround rouge nether
for i in range (0, 3):
    fill(198, 40, 40)
    rect(300, 0, 300, 89)

#Carrés aléatoire au fond du nether
for i in range(0, 15):
    for a in range(0, 10):
        Fondx = random.randint(310, 600)
        Fondy = random.randint(0, 100)
        couleurr = random.randint(150, 255)
        couleurg = random.randint(0, 25)
        couleurb = random.randint(0, 25)
        fill(couleurr, couleurg, couleurb)
        square(Fondx, Fondy, 10)

#Plateforme du nether
stroke(0, 0, 0)
for i in range (0, 3):
    fill(105, 5, 5)
    rect(425, 35, 150, 40)
    fill(135, 22, 22)
    rect(400, 55, 150, 20)
    fill(135, 22, 22)
    rect(315, 55, 150, 20)
    fill(189, 11, 11)
    rect(375, 45, 105, 30)

#Bedrock
fill(126, 126, 143)
rect(0, 89, 600, 11)

#Lave
z = 330
Z = 90
y = 322
Y = 90
for i in range (0,3):
    fill(255, 86, 34)
    rect(z, 9, 5, 39)
    fill(255, 86, 34)
    rect(y, 0, 20, 9)
    z = z + Z
    y = y + Y

#Rails 
line(300, 75, 600, 75)
fill(62, 39, 35)
rect(300, 76, 600, 2)
#Wagon
fill(97, 97, 97)
rect(305, 69, 15, 5) 
fill(0, 230, 119)
rect(310, 66, 5, 5)
fill(255, 139, 128)
rect(310, 64, 5, 3)

a = 340
b = 90
c = 345
d = 370
e = 355
F = 325
for i in range (0, 3):
    #Ghasts
    fill(255, 255, 255)
    rect(a, 6, 40, 40)
    #Visage ghasts
    fill(0, 0, 0)
    rect(c, 15, 7, 1)
    fill(0, 0, 0)
    rect(d, 15, 10, 1)
    fill(0, 0, 0)
    rect(e, 30, 15, 1)
    #Tentacules ghasts
    fill(255, 255, 255)
    quad(a, 18, F, 20, F, 26, a, 24)
    fill(255, 255, 255)
    quad(a, 23, F, 25, F, 29, a, 29)
    fill(255, 255, 255)
    quad(a, 28, F, 30, F, 36, a, 34)
    fill(255, 255, 255)
    quad(a, 33, F, 35, F, 41, a, 39)
    a = a + b
    c = c + b
    d = d + b
    e = e + b
    F = F + b

'''
Transition entre la partie gauche de la frise et la partie droite
'''

#Particules de l'entrée du nether
for i in range (0, 40):
    for a in range (0, 20):
        particulesx = random.randint(288, 312)
        particulesy = random.randint(6, 66)
        stroke(237, 80, 241)
        point(particulesx, particulesy)

stroke(0, 0, 0)            
#Portail du nether
fill(0, 0, 0)
rect(295, 0, 10, 75)

#EntrÃ©e du portail du nether
fill(104, 58, 183)
rect(292, 8, 3, 60)
fill(104, 58, 183)
rect(305, 8, 3, 60)

'''
Overworld 1ère frise à gauche
'''

#Pelouse de blocs d'herbe
fill(109, 76, 65)
rect(0, 75, 20, 18)

fill(109, 76, 65)
rect(20, 89, 50, 4)

fill(56, 142, 61)
rect(0, 75, 20, 6)

fill(109, 76, 65)
rect(70, 75, 230, 18)

fill(56, 142, 61)
rect(70, 75, 230, 6)

#pont
fill(146, 109, 39)
rect(20, 75, 50, 6)

#riviÃ¨re
"""
TracÃ© des courbes:

    bezier(x1,y1,x2,y2,x3,y3,x4,y4)

"""
x1 = 20
x2 = 30
x3 = 20
x4 = 40
for i in range(0, 3):
    fill(47, 47, 145)
    bezier(x1,89,x2,80,x3,80,x4,89)
    x1 = x1+15
    x2 = x2+15
    x3 = x3+15
    x4 = x4+15

#maisons + villageois
s = 40
h = 90
L = 50
m = 60
M = 25
for i in range (0, 3):
    #base des maisons (bois)
    fill(91, 60, 17)
    rect(s, 25, 50, 50)

    #pierre des maisons
    fill(130,130,130)
    rect(L,25,30,50)

    #porte
    fill(170,140,80)
    rect(m, 40, 10, 34)
    
    
    #villageois
    fill(60,40,40)
    rect(M, 49, 10, 20)
    
    #pied
    fill(65,45,45)
    rect(M+2, 69, 6, 5)
    
    #bras
    fill(30,10,10)
    rect(M-3,54, 16, 7)
    
    #tete
    fill(110,80,60)
    rect(M, 44, 10, 7)
    
    #yeux
    fill(255,255,255)
    rect(M+2,46, 2, 2)
    fill(255,255,255)
    rect(M+6,46, 2, 2)
    
    #nez
    fill(0,0,0)
    rect(M+4,47, 2, 5)

    #toit
    
    #triangle(x1, y1, x2, y2, x3, y3)
    
    triangle(s-8, 25, s+25, 4, s+58, 25)
    
    s = s + h
    L = L + h
    m = m + h
    M = M + h
    
#Soleil
S = 0
for y in range(25):
    line(0, y, 25, y)
    S= S+7
    stroke(255, 255, S)

'''
End deuxième frise
'''

#Ciel de l'end
stroke(26, 23, 23)
fill(26, 23, 23)
rect(0, 100, 600, 100)

#Etoiles
strokeWeight(2)
stroke(219, 218, 192)
for i in range(1, 20):
    
    for r in range(1, 10):
        etoilesx= random.randint(0,600)
        etoilesy= random.randint(100, 200)
        point(etoilesx, etoilesy)

#Sol de l'end
strokeWeight(1)
stroke(255, 235, 59)
fill(255, 235, 59)
rect(0, 190, 600, 10)

#Tour de l'end
stroke(0, 0, 0)
T = 50
Y = 100
for i in range (0, 6):
    fill(0, 0, 0)
    rect(T, 140, 20, 50)
    fill(126, 126, 143)
    rect(T, 148, 20, 2)
    T = T + Y
#Boule de crystal de l'end
B = 60
C1 = 55
C2 = 65
C3 = 60
for i in range(0, 6):
    stroke(255, 255, 255)
    fill(156, 39, 176)
    circle(B, 130, 10)
    line(C1, 130, C2, 130)
    line(C3, 125, C3, 135)
    line(C1, 125, C2, 125)
    line(C1, 135, C2, 135)
    line(C2, 125, C2, 135)
    line(C1, 125, C1, 135)
    line(C1, 125, C2, 135)
    line(C2, 125, C1, 135)
    B = B + Y
    C1 = C1 + Y
    C2 = C2 + Y
    C3 = C3 + Y

#Enderman
E = 25
E1 = 75
E2 = 100
stroke(0, 0, 0)
for i in range (0, 12):
    fill(0, 0, 0)
    rect(E, 180, 2, 10)
    fill(123, 31, 62)
    rect(E, 180, 2, 2)
    fill(0, 0, 0)
    rect(E1, 180, 2, 10)
    fill(123, 31, 62)
    rect(E1, 180, 2, 2)
    fill(0, 0, 0)
    rect(E2, 180, 2, 10)
    fill(123, 31, 62)
    rect(E2, 180, 2, 2)
    E = E + Y
    E1 = E1 + Y
    E2 = E2 + Y

#Enderdragon
stroke(33, 33, 33) 
#corps
fill(0, 0, 0)
rect(185, 115, 60, 20)
#tÃªte
fill(0, 0, 0)
rect(240, 110, 20, 15)
#bouche
fill(0, 0, 0)
rect(260, 118, 15, 7)
#oreille
fill(0, 0, 0)
triangle(245, 110, 250, 105, 255, 110)
#oeil
fill(63, 0, 113)
rect(245, 112, 10, 3)
#aile
fill(0, 0, 0)
triangle(195, 123, 225, 160, 230, 123)     
#patte
fill(0, 0, 0)
rect(193, 142, 10, 3)
fill(0, 0, 0)
rect(193, 135, 5, 10)
fill(0, 0, 0)
rect(235, 142, 10, 3)
fill(0, 0, 0)
rect(235, 135, 5, 10)
#queue
fill(0, 0, 0)
rect(160, 115, 25, 5)

'''
Biome cave quatrième frise
'''

#grotte
fill(200,200,200)
#( on ecrit "-1" et "601" pour ne pas afficher les bordures
rect(-1, 300, 601, 400)

#decor de la grotte
fill(170,170,170)
rect(20,330,560,50)
fill(110,110,100)
rect(70,340,500,35)
fill(60,60,60)
rect(260,355, 270, 20)

#torche
torX = 40
for i in range(0,6):
    fill(91, 60, 17)
    rect(torX, 315, 5, 10)
    fill(255,255,0)
    rect(torX, 310, 5, 5)
    torX = torX + 100

#torche arriere plan
fill(150,150,150)
rect(290,355,23,20)
fill(91, 60, 17)
rect(300,365,3,6)
fill(255,255,0)
rect(300, 362, 3, 3)

fill(170,170,170)
rect(175,340,35,35)
fill(91, 60, 17)
rect(190,355,4,8)
fill(265,255,0)
rect(190, 351, 4, 4)


#chute d'eau
fill(37, 53, 233)
rect(100,340,30,35)
fill(37, 53, 233)
rect(120,375,100,5)

#chute de lave
fill(198, 40, 40)
rect(490,355,10,20)
fill(198, 40, 40)
rect(400,355,10,20)

#rails
fill(100,100,100)
rect(-1, 390, 601, 400)

#planches de bois sur les rails
BO = 5
for i in range (0,30):
    fill(91, 60, 17)
    rect(BO, 385, 10, 10)
    BO = BO+ 20

#wagon
wag = 15
xr = 20
xrr = 60
for i in range (0,6):
    fill(30,30,20)
    rect(wag, 350, 50, 30)
    #coffre dans le wagon
    fill(237, 127, 16)
    rect(wag+4, 337,42,13)
    fill(0,0,0)
    line(wag+ 4, 347, wag+ 46, 347)
    fill(200,200,200)
    rect(wag+24,343,4,7)

    #roue
    fill(0,0,0)
    circle(xr, 385, 9)
    circle(xrr, 385, 9)
    wag = wag + 100
    xr = xr + 100
    xrr = xrr + 100

'''
Temple aquatique 3ème frise
'''

fill(61, 178, 255)
rect(0, 200, 600, 100)

def test():
#Profondeur
    y6 = 220

#d1 : dégradé pour montrer le niveau de profondeur de l'océan 
    d1 = 0

    SurfaceEau = 300
    for lvl in range(80+1):
        line(0, SurfaceEau - lvl , 600, SurfaceEau - lvl)
        stroke(20, 39, d1)
        d1 = d1 + 5
test()



for i in range(1, 20):

    for r in range(1, 10):
        posXx = random.randint(0,600)
        posYy= random.randint(240, 270)
        ellipse(posXx, posYy, 5, 2)
        fill(255, 0, 0)


    for y in range(1, 10):
        posx = random.randint(0,600)
        posy = random.randint(280, 290)
        ellipse(posx, posy, 3, 10)
        fill(50, 80, 46)
        noStroke()

#Vagues
x1 = 0
x2 = 4
x3 = 0
x4 = 20
for i in range(0, 40):
    fill(20, 39, 155)
    bezier(x1, 220 ,x2,216,x3,219,x4,220)
    x1 = x1 + 15
    x2 = x2+15
    x3 = x3+15
    x4 = x4+15

#Motifs des gardiens en cours... 


T1 = 50
T2 = 30
T3 = 66
T4 = 68
T5 = 64
T6 = 23
T7 = 55
T8 = 60
Y = 100
for i in range (0, 6):
    stroke(0, 0, 0)
    fill(127, 139, 82)
    rect(T1, 240, 20, 20)
    fill(127, 139, 82)
    rect(T2, 245, 21, 10)
    fill(255, 255, 255)
    rect(T3, 243, 5, 10)
    fill(59, 0, 0)
    rect(T4, 248, 3, 4)
    fill(28, 121, 71)
    rect(T5, 243, 6, 2)
    fill(242, 161, 84)
    arc(T6,250, 20, 20, radians(-120), radians(150))
    rect(T1, 242, 2, -5)
    rect(T7, 242, 2, -5)
    rect(T8, 242, 2, -5)
    T1 = T1 + Y
    T2 = T2 + Y 
    T3 = T3 + Y
    T4 = T4 + Y
    T5= T5 + Y
    T6 = T6 + Y
    T7 = T7 + Y
    T8 = T8 + Y