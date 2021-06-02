import numpy as np

class Pendulum:
    def __init__(self):
        self.score = 0
        self.dir = np.array([0, 1])
        self.angular_vel = 0
        self.spool = 0
        self.braking = False
        self.stopping = False

    def applyForces(self, gravity, friction, spool_amt, TORQUE):
        if self.dir[0] < 0:
            self.angular_vel -= gravity*np.abs(self.dir[0])
        else:
            self.angular_vel += gravity*np.abs(self.dir[0])
        if self.angular_vel > 0:
            self.angular_vel -= (friction[0] + friction[1]*(np.abs(self.angular_vel) + TORQUE/spool_amt))
        elif self.angular_vel < 0:
            self.angular_vel += (friction[0] + friction[1]*(np.abs(self.angular_vel) + TORQUE/spool_amt))
        self.spool -= (2*(self.spool>0)-1)*friction[1]
        self.dir = rot(self.dir, self.angular_vel)
        self.score += self.dir[1]

    def motor(self, spool_amt, TORQUE, power):
        if self.spool > 0+.1 and power < 0-.1:
            self.braking = True
            self.stopping = True
        if power >= 0:
            self.braking = False
        if self.spool < 0:
            self.stopping = False
        if ((power>0 and self.spool>-1) or (power<0 and self.spool<1)) and (not self.braking or self.stopping):
            self.angular_vel += (2*(1*(self.dir[0]<0))-1)*power*TORQUE
            self.spool += (2*(1*(self.dir[0]<0))-1)*power*spool_amt



def rot(vector, theta):
    return np.dot(np.array([[np.cos(theta), -1*np.sin(theta)], [np.sin(theta), np.cos(theta)]]), vector)
