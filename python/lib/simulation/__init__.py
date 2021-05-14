'''
Physical simulation
======
Written in C++
'''
from typing import List, Optional

from ._simulation import (
    Particule as _Particule,
    MagneticField as _MagneticField,
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

class MagneticField(_MagneticField):
    '''
    Magnetic field
    ===
    Arguments
    ---
    `'x', 'y' float`: Origin of the field  
    `'intensity' float`: Inensity of the field  
    `'dispersion' float`: Dispersion -> how much the field expand
    '''
    origin: List[float]
    intensity: float
    dispersion: float

    def __init__(self, x: float, y: float, intensity: float, dispersion: float=None):
        dispersion = -1 if dispersion is None else dispersion
        super().__init__(x, y, intensity, dispersion)


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
    magnetic_fields: List[MagneticField]
    constants: Constants
    n_particules: int
    FLAG_SUM: int = 0
    FLAG_SUM_ONESIDE: int = 1

    def __init__(self, particules: List[Particule], dt: Optional[float]=None, flag: Optional[int]=None):
        dt = -1 if dt is None else dt
        flag = 0 if flag is None else flag
        super().__init__(particules, dt, flag)
    
    def update(self, dt: Optional[float]=None):
        '''
        Update the simulation state  
        Arguments
        ---
        `'dt' float`: time delta used to update the simulation state  
        '''
        dt = -1 if dt is None else dt
        super().update(dt)
    
    def clear_elements(self):
        '''
        Clear all elements from the system (particules & magnetic fields).  
        Keep all other settings.
        '''
        super().clear_elements()

    def add_particule(self, particule: Particule):
        '''
        Add a particule to the system
        '''
        super().add_particule(particule)

    def add_magnetic_field(self, field: MagneticField):
        '''
        Add a magnetic field to the system
        '''
        super().add_magnetic_field(field)
    
    def set_limits(self, min_x: float, max_x: float, min_y: float, max_y: float):
        '''
        Set the limits of the simulation
        '''
        super().set_limits(min_x, max_x, min_y, max_y)