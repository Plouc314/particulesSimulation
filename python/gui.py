from lib.plougame import Interface, Dimension, Form, Page, C, Font
import lib.plougame.components as cmps
from lib.plougame.helper import Delayer
from lib.simulation import Particule, MagneticField
from config import Consts
import numpy as np
import pygame, time

class ParticuleUI(Form):

    def __init__(self, particule: Particule):
        self.particule = particule
        if self.particule.q >= 0:
            color = Consts.C_POSITIVE
        else:
            color = Consts.C_NEGATIVE

        # change dimension according to charge
        dim = Consts.DIM_PARTICULE * abs(self.particule.q)**0.5

        pos = np.array(self.particule.pos) * Consts.SCALE_FACTOR

        super().__init__(dim, pos, color, center=True)

class FieldUI(Form):

    def __init__(self, field: MagneticField, dynamic=False):
        self.field = field
        self.dynamic = dynamic
        
        if self.dynamic:
            super().__init__([10,10], self.field.origin, color=C.GREY, center=True)
    
    def display(self):

        center = Dimension.scale(self.field.origin) * Consts.SCALE_FACTOR
        radius = Dimension.scale(self.field.dispersion) * Consts.SCALE_FACTOR

        pygame.draw.circle(
            Interface.screen,
            C.LIGHT_GREY,
            center,
            radius,
        )

        if self.dynamic:
            super().display()