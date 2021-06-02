import pygame
import sys
from DRLib.Gen import Generation
from DRLib.loadFuncs import loadIndex
from Pendulum import *

""" CONSTANTS ONLY NEEDED FOR GRAPHICS
"""
WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
SIZE = [200, 10]
POS = np.array([WIDTH/2, HEIGHT/2])

""" More various graphics setup
"""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


""" CONSTANTS FOR REAL WORLD FORCES
"""
FRICTION = [.0000001, .0001] #index 0 is constant, index 1 is proportion of angular momentum
TORQUE = .0000025
GRAVITY = .00001
MOTOR = .0005

""" MAKE INITIAL 100 Random neural networks and 100 pendulum objects
"""
pop = 100
pen = [None]*pop
for i in range(pop):
    pen[i] = Pendulum()
g = Generation(pop, [2, 4, 4, 1], True)
g.pop[0] = loadIndex("saved.csv", 75)

for q in range(50): # Go for 5 generations
    print("generation: " + str(q+1))
    for i in range(10000): # Go for 10000 gameloops per generation
        if i%1000==0:
            print(i) # Let me know how long is left in generation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # Makes close button work for graphics window

        data = np.array([None]*len(pen)) # will be a list of inputs for each player based on their own data

        for j in range(len(pen)):
            pen[j].applyForces(GRAVITY, FRICTION, MOTOR, TORQUE) # First apply gravity and friction
            """ Input is 1x2 index 0: y component of direction vector, 0 is straight up and 1 is straight down
                index 1 is angular velocity made to be between -1 and 1
                It doesnt know what its x component is so it doesnt know what side of the y axis it is on. I made the
                observation that it should treat both sides with the exact same strategy except inverted so I multiply 
                all of the necesary values by -1 if it is on one side and and have it think that it is always on the 
                same side.
            """
            data[j] = (pen[j].dir[1]/2+.5, 500*(2*(1*(pen[j].dir[0]<0))-1)*(pen[j].angular_vel))#, pen[j].spool)

        plays = g.f_pass_sep_inputs(data) #Pass list of all inputs to generation object, return output

        """ Parse numerical output into game output
        """

        for j in range(len(pen)):
            # power = 0
            # if np.argmax(np.abs(plays[j][0])) == 0:
            # power = max(min(plays[j][0][0], 1), -1)
            power = 0
            if plays[j][0][0] < -.05:
                power = max(-1, plays[j][0][0])
            elif plays[j][0][0] > .05:
                power = min(1, plays[j][0][0])
            pen[j].motor(MOTOR, TORQUE, power)

            #
            # elif np.argmax(plays[j]) == 1:
            #   if (pen[j].dir[0]>= 0 and pen[j].spool > -1) or (pen[j].dir[0]<= 0 and pen[j].spool < 1):
            #     pen[j].angular_vel += (2*(1*(pen[j].dir[0]<0))-1)*TORQUE*plays[j][0][1]
            #     pen[j].spool += (2*(1*(pen[j].dir[0]<0))-1)*.005*plays[j][0][1]

            g.scores[j] += pen[j].dir[1]+.5*abs(pen[j].spool)

        """ Print graphics for player at index 0 only, It is slow because around 600 other neural networks are also
        playing simaltaniously so overall training time is relatively fast
        who is unchanged best from previous generation
        """
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, POS, POS+SIZE[0]*pen[0].dir, SIZE[1])
        pygame.draw.line(screen, BLACK, (400, 550), (600, 550), SIZE[1])
        pygame.draw.line(screen, BLACK, (500+100*pen[0].spool, 560), (500+100*pen[0].spool, 540), 5)
        pygame.display.update()

    """ Update generation and create new pendulum objects
    """
    g = g.next_gen()
    pop = len(g.pop)
    pen = [None]*pop
    for i in range(pop):
        pen[i] = Pendulum()
