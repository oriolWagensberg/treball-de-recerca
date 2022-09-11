"""
Diccionari per entendre els comentaris:

    -Objecte: Un manera abstracta de relacionar variables i funcións. En el context d'objectes les funcions es diuen metodes, i les variables atributs
    -Classe: Es la plantilla que dissenyem per crear els nostres objectes.
    -Array: Una llista de qualsevol tipus de variable.
    -pygame: La llibraria que májuda a crear a tot el joc, amb ella creo la pantalla, objectes que hi apareixen, em facilita molt la part grafica
    -random:

"""
import time
import pygame
import random
import numpy
            
pygame.init()

# Inicio algunes constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
X = 800
Y = 500
screen = pygame.display.set_mode((X, Y)) # aquí és on inicialitzo la pantalla principal.
SPEED = 50
FPS = 30


# La classe principal de tots el sprites que apareixen en pantalla.

class Simbol:
    def __init__(self, color, posX, posY, text, size,display):
        self.color = color
        self.pos = {
            'x': posX ,
            'y': posY - size/2
            }
        
        self.size = size
        font = pygame.font.Font("FreeSans.ttf", size)
        self.text = font.render(text, True, self.color)
        self.canISpin = False
        self.display = display

    def spin(self, speed): # Aquest metode l'utilitzo per poder canviar la possisió dels meus Simbols.

        if self.pos['y'] < 650:
            self.pos['y'] += speed
        else:
            self.pos['y'] = 0

    def correct(self, hMuch):
        self.pos['y'] -= hMuch

def objList(num, x):
    objArray = []
    for i in range(0, num):
        newObj = Simbol(BLACK, x, i* 100, f"{i}", 100, screen)
        objArray.append(newObj) 
    return objArray


def drawWindow(win, wheels):

    win.fill(WHITE)
    for objs in wheels:
        for obj in objs:
            win.blit(obj.text, (obj.pos['x'], obj.pos['y']))
    pygame.display.update()

def randomTimes(s, e, num):

    random_times = []
    time_seconds = time.time() + random.randint(s, e)
    for i in range(0, num):
        random_times.append(
            time_seconds + random.random()/2
            )

    return random_times

def isAllEqual(array):
    for i in array:
        for k in array:
            if i == k:
                return i
            else:
                continue


def howMuch(wheel):
    lowest = wheel[1].pos['y'] - 250
    for i in wheel:
        temporay = i.pos['y'] - 250
        if temporay < lowest and temporay > 0:
            lowest = temporay
        else: 
            continue
    return temporay


def correctPos(correct_pos, WHEELS):
    for i, v in enumerate(WHEELS):
        if correct_pos[i]:
            for s in v:
                s.correct(howMuch(WHEELS[i]))
        correct_pos[i] = False    

# Aquí tenim la funció principal
# Aquesta funció fa dues coses, inisialitzar els tambors i crear el game loop. --> un bucle infinit en el que passa tot el joc


def main():
    RUN  = True # Aquesta funció es True fins que s'intenta sortir del joc, així tornantse False i trencant el game Loop

    clock = pygame.time.Clock() #creo una insancia del obj per tenim uns FPS constants´.

    wheel_1 = objList(7, 167) # Utilizo la funció objList, per automatitzar la creació de tots els objecctes de la calasse Simbol, que formaran el meu tambor
    wheel_2 = objList(7, 333)
    wheel_3 = objList(7, 500)

    new_wheel_1 = random.sample(wheel_1, len(wheel_1))
    new_wheel_2 = random.sample(wheel_2, len(wheel_1))
    new_wheel_3 = random.sample(wheel_3, len(wheel_1))



    WHEELS = [new_wheel_1, new_wheel_2, new_wheel_3] # Creao una llista amb

    
    mWheels = [False, False, False]
    endTime = [0, 0, 0]

    while RUN:
        
        clock.tick(FPS)

        for events in pygame.event.get():

            if events.type == pygame.QUIT:
                RUN = False
    
        keys_down = pygame.key.get_pressed()
        
        if keys_down[pygame.K_SPACE] and mWheels[0] == False:

            mWheels = [True, True, True]

            endTime = randomTimes(5, 7, 3)


        for indx, val in enumerate(WHEELS):
            if mWheels[indx]:
                for i in val:
                    i.spin(SPEED)


        for indx, val in enumerate(endTime):

            if time.time() > endTime[indx]:
                mWheels[indx] = False

        drawWindow(screen, WHEELS)

if __name__ == "__main__":
    main()




    """
        Mira quin es el simbol que esta més aprop de les cordenades del mig
        i calcula quan s'ha de moure perque hi quedin i li suma aquest numero a les y de tota la 
    """

    """
        Corretgeix qu el centre del numero sigui a la punta

    """