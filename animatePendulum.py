import pygame
import sys
from DRLib.loadFuncs import loadIndex
from Pendulum import *

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
SIZE = [200, 10, 30]
POS = np.array([WIDTH/2, HEIGHT/2])

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.key.set_repeat(1)

def drawPendulum(pen, size, screen, pos):
    pygame.draw.line(screen, BLACK, pos, pos+size[0]*pen.dir, int(size[1]))
    pygame.draw.circle(screen, BLACK, pos+size[0]*pen.dir, int(size[2]))

FRICTION = [.0000001, .0001]
TORQUE = .000002
GRAVITY = .00001



# player = loadIndex("saved.csv", 3*q)
pen = Pendulum()
pen.dir = np.array([-1, 0])
# create a text suface object,
# on which text is drawn on it.
font = pygame.font.Font('freesansbold.ttf', 32)


for i in range(2500):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pen.applyForces(GRAVITY, (0,0))
    drawPendulum(pen, SIZE, screen, POS)
    pygame.display.update()

while SIZE[0] > 40:
    SIZE[0] *= .999
    SIZE[1] *= .9993
    SIZE[2] *= .9989

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pen.applyForces(GRAVITY, (0,0))

    drawPendulum(pen, SIZE, screen, POS)
    pygame.display.update()
for i in range(1000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pen.applyForces(GRAVITY, (0,0))
    drawPendulum(pen, SIZE, screen, POS)
    pygame.display.update()
for i in range(1000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pen.applyForces(GRAVITY, (0,0))
    for y in range(-250, 251, 100):
        for x in range(-350, 351, 50):
            drawPendulum(pen, SIZE, screen, POS+(i/1000)*np.array([x, y]))

    pygame.display.update()
for i in range(5000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pen.applyForces(GRAVITY, (0,0))
    for y in range(-250, 251, 100):
        for x in range(-350, 351, 50):
            drawPendulum(pen, SIZE, screen, POS+np.array([x, y]))

    pygame.display.update()