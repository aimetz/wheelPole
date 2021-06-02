import pygame
import sys
from DRLib.loadFuncs import loadIndex
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
TORQUE = .0000025
GRAVITY = .00001
MOTOR = .0005


# player = NN(3, [2, 4, 4, 1])
# player.layers[0].weights = [[ 1.04105281,  1.41965268,  0.24164059, -1.08015808],
#                             [ 1.02373352, -0.3299172,  -0.49380182,  1.14940579]]
# player.layers[0].bias =    [[-0.05863339, -0.00181791,  0.02863135,  0.06348731]]
# player.layers[1].weights = [[-2.11933215,  1.41457551, -1.30119171, -0.98632311],
#                             [-1.03620955,  0.65200167, -1.56971423,  1.28854099],
#                             [-1.08301761,  1.60073122,  0.29844105, -1.006978  ],
#                             [-0.43283162, -1.01874074,  1.60636639,  1.12808766]]
# player.layers[1].bias =    [[-0.08026357, -0.06809398, -0.1405554,  -0.01807309]]
# player.layers[2].weights = [[-1.59771158],
#                             [ 0.24303081],
#                             [-0.20603571],
#                             [-1.3503754 ]]
# player.layers[2].bias =    [[0.11509012]]
its = [9000, 12000, 13000, 14000, 14000, 15000]
for q in range(5, 6):

    player = loadIndex("saved.csv", 116)
    pen = Pendulum()
    # create a text suface object,
    # on which text is drawn on it.
    font = pygame.font.Font('freesansbold.ttf', 32)


    for i in range(500000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         pen.angular_vel -= 10*TORQUE
            #     if event.key == pygame.K_RIGHT:
            #         pen.angular_vel += 10*TORQUE

        screen.fill(WHITE)

        pen.applyForces(GRAVITY, FRICTION, MOTOR, TORQUE)

        data= (pen.dir[1]/2+.5, 500*(2*(1*(pen.dir[0]<0))-1)*(pen.angular_vel))
        plays = player.f_pass(data)
        power = 0
        if plays[0][0] < -.05:
            power = max(-1, plays[0][0])
        elif plays[0][0] > .05:
            power = min(1, plays[0][0])
        pen.motor(MOTOR, TORQUE, power)
        # if plays < 0:
        #     pen.angular_vel -= (2*(1*(pen.dir[0]<0))-1)*TORQUE
        # elif plays > 0:
        #     pen.angular_vel += (2*(1*(pen.dir[0]<0))-1)*TORQUE

        pygame.draw.line(screen, BLACK, POS, POS+SIZE[0]*pen.dir, SIZE[1])
        pygame.draw.circle(screen, BLACK, POS+SIZE[0]*pen.dir, 30)
        pygame.draw.line(screen, BLACK, (400, 550), (600, 550), SIZE[1])
        pygame.draw.line(screen, BLACK, (500+100*pen.spool, 560), (500+100*pen.spool, 540), 5)
        text = font.render("Generation "+str(q)+" Best", True, (0, 0, 0), (255, 255, 255))

        textRect = text.get_rect()

        textRect.center = (150, 150)

        screen.blit(text, textRect)
        pygame.display.update()
        # if (i%2==0):
        #     pygame.image.save(screen, "images2/screenshot"+str(q)+"-"+str(i)+".jpeg")