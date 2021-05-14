from lib.plougame import Interface, Specifications

Interface.setup((3200, 1600), "Simulation")
FPS = 60

from lib.simulation import System, Particule, MagneticField
import numpy as np
import pygame, time
from app import App
from gui import ParticuleUI, FieldUI
from config import Consts

system = System([], dt=1/FPS, flag=System.FLAG_SUM_ONESIDE)
system.constants.k = 2
system.set_limits(
    Consts.MIN_X,
    Consts.MAX_X,
    Consts.MIN_Y,
    Consts.MAX_Y
)

app = App(system)

while Interface.running:
    
    pressed, events = Interface.run()

    if not app.paused:
        app.update_system()
    
    app.react_events(pressed, events)
    app.display()