# Physics 91SI
# Spring 2017
# Lab 8

import numpy as np
from particle import Particle

class Molecule:

    def __init__(self, pos1, pos2, mass1, mass2, k, L0): 

        self.p1 = Particle(pos1, mass1)
        self.p1.pos = pos1
        self.p1.m = mass1
        self.p2 = Particle(pos2, mass2)
        self.p2.pos = pos2
        self.p2.m = mass2
        self.k = k
        self.L0 = L0

    def get_displ(self):
        return (self.p1.pos - self.p2.pos)

    def get_force(self):
        displacement = self.get_displ()
        displacement_mag  = np.linalg.norm(displacement)
        force_mag = (displacement_mag - self.L0) * self.k
        force = force_mag * (displacement / displacement_mag)
        return force

