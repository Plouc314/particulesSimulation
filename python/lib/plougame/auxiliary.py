import pygame
import numpy as np

class Dimension:
    _f = 1

    @classmethod
    def set_factor(cls, factor):
        '''
        Set the scale factor, used to change the dimension of the window 
        (based on the dimension given in `Interface.setup`).
        '''
        cls._f = factor

        # update scaled sizes
        cls._rx = cls._f * cls._x
        cls._ry = cls._f * cls._y

    @classmethod
    def get_factor(cls):
        ''' Return the scale factor. '''
        return cls._f

    @classmethod
    def set_dim(cls, dim):
        '''
        Set the window dimension.
        '''
        cls.WINDOW = dim 
        
        # unscaled
        cls.center_x = int(dim[0]/2)
        cls.center_y = int(dim[1]/2)
        cls.center = (cls.center_x, cls.center_y)
        cls._x = dim[0]
        cls._y = dim[1]
        cls._rx = cls._f * cls._x
        cls._ry = cls._f * cls._y

    @classmethod
    def get_x(cls, scaled=False):
        '''
        Return the x dimension of the window,
        if `scaled=True` the dimension will be scaled to the current window's dimension.
        '''
        if scaled:
            return cls._rx
        else:
            return cls._x

    @classmethod
    def get_y(cls, scaled=False):
        '''
        Return the y dimension of the window,
        if `scaled=True` the dimension will be scaled to the current window's dimension.
        '''
        if scaled:
            return cls._ry
        else:
            return cls._y

    @classmethod
    def get_window_dim(cls):
        '''Return the scaled dimension of the window'''
        return cls.scale(cls.WINDOW)

    @classmethod
    def scale(cls, x, factor=None):
        
        if factor:
            f = factor
        else:
            f = cls._f

        if type(x) in [int, float]:
            return x * f

        return np.array(x, dtype='float64') * f

    @classmethod
    def inv_scale(cls, x):
        '''
        Inverse the scale of the number: scale -> unscale ( note: unscale -> ?!@#@ )
        '''
        f = 1/cls._f
        
        if type(x) in [int, float]:
            return x * f

        return np.array(x, dtype='float64') * f

    @classmethod
    def E(cls, x, *, fp=None):
        return round(x*cls._f, fp)

class C:
    '''Container of predefined colors'''
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    
    NEO_BLUE = (95, 245, 255)
    XLIGHT_BLUE = (204,230,255)
    LIGHT_BLUE = (135,206,250)
    BLUE = (65,105,225)
    DARK_BLUE = (7, 19, 134)
    
    GREY = (150,150,150)
    LIGHT_GREY = (200,200,200)
    XLIGHT_GREY = (245,245,245)
    
    LIGHT_RED = (255, 80, 80)
    RED = (225, 50, 50)
    DARK_RED = (195, 20, 20)

    LIGHT_GREEN = (124,252,100)
    GREEN = (94,222,70)
    DARK_GREEN = (17, 159, 26)
    
    LIGHT_BROWN = (225, 167, 69)
    
    DARK_PURPLE = (140, 17, 159)
    PURPLE = (180, 57, 199)
    LIGHT_PURPLE = (210, 87, 229)
    
    DARK_YELLOW = (219, 207, 40)
    YELLOW = (253, 240, 49)

class Font:
    '''
    Static object  
    Create pygame fonts  
    Use `f` method to generate a font.  
    The `fontname` attribute can be modified, it is the default fontname.
    '''
    fontname = 'Arial'
    @classmethod
    def f(cls, size, fontname: str=None):
        '''
        Create a font of the given size,  
        if `fontname` is specified, generate the specified font,
        else use the default font (`fontname` attribute).  
        In the format: `{'size':size,'font':pygame.font}`
        '''
        if fontname is None:
            fontname = cls.fontname

        return {'size':size , 'font':pygame.font.SysFont(cls.fontname, Dimension.E(size))}

