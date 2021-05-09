'''
Physical simulation
======
Written in C++
'''
from typing import List, Optional

from .cppSimulation import (
    Particule as _Particule,
    System as _System,
    Constants as _Constants
)

class Constants(_Constants):
    '''
    Physical constants holder
    '''
    masse_proton: float
    masse_neutron: float
    masse_electron: float
    charge_proton: float
    charge_electron: float
    k: float
    e: float

class Particule(_Particule):
    '''
    Particule object
    ===
    Arguments
    ---
    `'pos' list`: position of the particule  
    `'q' float`: charge of the particule (see `Constants`)  
    `'m' float`: masse of the particule (see `Constants`)  
    Attributes
    ---
    `'pos'`,`'q'`,`'m'` : see above  
    `'a' list`: acceleration  
    `'v' list`: speed  
    '''
    pos: List[float]
    v: List[float]
    a: List[float]
    q: float
    m: float

    def __init__(self, pos: List[float], q: float, m: float):
        super().__init__(pos[0], pos[1], q, m)

class System(_System):
    '''
    Physical system
    ===
    Arguments
    ---
    `'particules' list[Particule]`: the particules  
    `'dt' float`: time delta used to update the simulation state  
    '''
    particules: List[Particule]
    constants: Constants

    def __init__(self, particules: List[Particule], dt: Optional[float]=None):
        dt = -1 if dt is None else dt
        super().__init__(particules, dt)
    
    def update(self, dt: Optional[float]=None):
        '''
        Update the simulation state  
        Arguments
        ---
        `'dt' float`: time delta used to update the simulation state  
        '''
        dt = -1 if dt is None else dt
        super().update(dt)