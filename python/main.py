from lib.plougame import Interface, Specifications
from lib.simulation import System, Particule

Interface.setup((3200, 1600), "Simulation")

FPS = 60
Specifications.set_fps(FPS)

from gui import ParticuleUI

particules = [
    Particule(10,10,1,1),
    Particule(10,12,-1,1),
]

system = System(particules, dt=0.1/FPS)
system.constants.k = 1

guis = [ParticuleUI(p) for p in particules]


while Interface.running:
    pressed, events = Interface.run()
    
    for i, p in enumerate(system.particules):
        guis[i].sync(p)
        guis[i].display()
    
    system.update()
    system.print()