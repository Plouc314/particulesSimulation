from lib.plougame import Interface, Specifications

Interface.setup((3200, 1600), "Simulation")
FPS = 60

from lib.simulation import System, Particule, MagneticField
import numpy as np
import pygame, time
from app import App
from gui import ParticuleUI, FieldUI

system = System([], dt=1/FPS)
system.constants.k = 2
system.set_limits(-2, 34, -2, 16)

app = App(system)

while Interface.running:
    
    pressed, events = Interface.run()

    if not app.paused:
        app.update_system()
    
    app.react_events(pressed, events)
    app.display()