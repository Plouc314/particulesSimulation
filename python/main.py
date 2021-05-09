from lib.plougame import Interface, Specifications
from lib.simulation import System, Particule

Interface.setup((1600, 1200), "Simulation")

FPS = 60
Specifications.set_fps(FPS)

from gui import ParticuleUI

particules = [
    Particule(( 9, 8), 1, 1),
    Particule(( 9, 9), -1, 1),
    Particule(( 9,10), 1, 1),
    Particule(( 9,11), -1, 1),
    Particule(( 9,12), 1, 1),
    Particule((11,10), -3, 1),
    Particule((13, 8), 1, 1),
    Particule((13, 9), -1, 1),
    Particule((13,10), 1, 1),
    Particule((13,11), -1, 1),
    Particule((13,12), 1, 1),
]

particules[5].v = [2, 0.6]

system = System(particules, dt=1/FPS)
system.constants.k = 1

guis = [ParticuleUI(p) for p in system.particules]


while Interface.running:
    pressed, events = Interface.run()
    
    for particule in guis:
        particule.update()
        particule.display()
    
    system.update()