import pygame
import sys
#from DRLib.loadFuncs import loadIndex
from Pendulum import *

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
SIZE = [200, 10]
POS = np.array([WIDTH/2, HEIGHT/2])

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.key.set_repeat(1)



FRICTION = [.0000001, .0001]
TORQUE = .000003
GRAVITY = .00001
MOTOR = .0005

if True:

    #player = loadIndex("saved.csv", q)
    pen = Pendulum()

    while True:
        power = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    power = 1
                if event.key == pygame.K_RIGHT:
                    power = -1
        pen.motor(MOTOR, TORQUE, power)

        screen.fill(WHITE)

        pen.applyForces(GRAVITY, FRICTION, MOTOR, TORQUE)
        pygame.draw.line(screen, BLACK, POS, POS+SIZE[0]*pen.dir, SIZE[1])
        pygame.draw.circle(screen, BLACK, POS+SIZE[0]*pen.dir, 30)
        pygame.draw.line(screen, BLACK, (400, 550), (600, 550), SIZE[1])
        pygame.draw.line(screen, BLACK, (500+100*pen.spool, 560), (500+100*pen.spool, 540), 5)
        pygame.display.update()