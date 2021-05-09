from lib.plougame import Form, C
from lib.simulation import Particule

DIM = (20, 20)
C_POSITIVE = C.RED
C_NEGATIVE = C.BLUE

class ParticuleUI(Form):

    def __init__(self, p: Particule):

        if p.q >= 0:
            color = C_POSITIVE
        else:
            color = C_NEGATIVE

        super().__init__(DIM, p.pos, color, center=True)
    
    def sync(self, p: Particule):
        
        self.set_pos((p.x*100, p.y*100), center=True, scale=True)