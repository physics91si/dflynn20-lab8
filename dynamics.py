#!/usr/bin/python

# Physics 91SI
# molecule 2017
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
from particle import Particle
from molecule import Molecule



# TODO: Implement this function
def init_molecule():
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them"""
    
    pos1 = np.array([[0.2],[0.2]])
    pos2 = np.array([[0.8],[0.8]])
    mol = Molecule(pos1, pos2, 10, 20, 1, 0.5)
    
    return mol


# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""
    f = mol.get_force()   
    a1 = f / mol.p1.m
    a2 = -f / mol.p2.m
    v_prev1 = mol.p1.vel - dt * a1 / 2
    v_prev2 = mol.p2.vel - dt * a2 / 2
    v_next1 = v_prev1 + a1 * dt
    v_next2 = v_prev2 + a2 * dt
    mol.p1.vel = v_next1
    mol.p2.vel = v_next2
    mol.p1.pos = mol.p1.pos + v_next1 * dt
    mol.p2.pos = mol.p2.pos + v_next2 * dt    



#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    ax.clear()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
