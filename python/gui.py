from lib.plougame import Form, C
from lib.simulation import Particule
import numpy as np

### PARTICULE ###
DIM_PARTICULE = np.array([15, 15])
C_POSITIVE = C.RED
C_NEGATIVE = C.BLUE
SCALE_FACTOR = 50

### MARK ###
LIFETIME = 1200

class ParticuleUI(Form):

    def __init__(self, particule: Particule):
        self._p = particule
        if self._p.q >= 0:
            color = C_POSITIVE
        else:
            color = C_NEGATIVE

        # change dimension according to charge
        dim = DIM_PARTICULE * abs(self._p.q)**0.5

        pos = np.array(self._p.pos) * SCALE_FACTOR

        super().__init__(dim, pos, color, center=True)

        self.delay = 0
        self.marks = []

    def update(self):
        
        # update marks
        old_pos = self.get_center()
        self._add_mark(old_pos)

        pos = np.array(self._p.pos) * SCALE_FACTOR

        self.set_pos(pos, center=True, scale=True)

    def _add_mark(self, pos):
        if len(self.marks) != 0:
            last_pos = self.marks[-1].get_center()
            
            if (last_pos == pos).all(): # only add mark if position has changed
                return

        self.delay += 1
        if self.delay != 10:
            return
        self.delay = 0

        dim = np.array(self.get_dim()) * 0.7

        self.marks.append(Mark(dim, pos, self.get_color()))

    def _update_marks(self):
        for mark in self.marks[:-1]:
            if mark.age == LIFETIME:
                self.marks.remove(mark)
            else:
                mark.update()

    def display(self):
        self._update_marks()

        for mark in self.marks:
            mark.display()
        
        super().display()


class Mark(Form):

    def __init__(self, dim, pos, color):
        super().__init__(dim, pos, color, center=True)

        self.age = 0

    def update(self):
        self.age += 1
        dim = self.get_dim() * (1 - self.age / LIFETIME)**2
        self.set_dim(dim, scale=True)