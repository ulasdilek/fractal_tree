from math import copysign, cos, sin, pi

INITIAL_POSITION = (0, -200)
INITIAL_ANGLE = 90
INITIAL_LENGTH = 100

FACTOR = 0.8
ANGLE_DIF = 18


class Node:

    def __init__(self, prev=None, sign=1):
        if prev is None:
            self.angle = INITIAL_ANGLE
            self.length = INITIAL_LENGTH
            self.pos = INITIAL_POSITION
        else:
            sign = copysign(1, sign)
            self.angle = prev.angle + ANGLE_DIF * sign
            self.length = prev.length * FACTOR
            self.pos = (prev.pos[0]+prev.length*cos(pi*(prev.angle/180)), prev.pos[1]+prev.length*sin(pi*(prev.angle/180)))
