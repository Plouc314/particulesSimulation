from lib.plougame import C
import numpy as np

class Consts:
    ### PARTICULE ###
    DIM_PARTICULE = np.array([15, 15])
    C_POSITIVE = (255, 0, 0)
    C_NEGATIVE = (0, 0, 255)
    COLOR_MAX_CHARGE = 10
    COLOR_LIGHTEST = 200
    SCALE_FACTOR = 100

    ### DIMENSION ###
    MIN_X = -2
    MAX_X = 34
    MIN_Y = 0
    MAX_Y = 18

    ### RANDOM GENERATION ###
    MIN_PARTICULES = 60
    MAX_PARTICULES = 120
    MIN_FIELDS = 0
    MAX_FIELDS = 5