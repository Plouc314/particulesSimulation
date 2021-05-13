from lib.plougame import Interface, Dimension, Form, Page, C, Font
import lib.plougame.components as cmps
from lib.plougame.helper import Delayer
from lib.simulation import System, Particule, MagneticField
from gui import FieldUI, ParticuleUI
from config import Consts
import pygame, time, numpy as np

delayer = Delayer(20)

class App(Page):

    def __init__(self, system: System):

        components = Page.formatter.get_components('ui/app.json')

        super().__init__(['base', 'edit'], components, active_states='none')

        self.set_states_components(['base', 'edit'], [
            'header',
            'label-time',
            'label-particules',
            'button-edit',
            'button-start',
            'button-reset',
            'button-random'
            ]
        )

        self.set_states_components('edit', [
            'button-add-particule',
            'button-add-field',
            ]
        )

        # timer attributes
        self.start_time = None
        self.current_time = 0
        
        # edit modes
        self.mode_p = False # add particule
        self.mode_f = False # add field
        self.mode_p_ui = ParticuleUI(Particule([0,0], 1, 1))
        self.mode_f_ui = FieldUI(MagneticField(0,0,1,1), dynamic=True)

        self.paused = True
        self.system = system

        self.add_button_logic('button-start', self.change_pause_state)
        self.add_button_logic('button-random', self.logic_random)
        self.add_button_logic('button-edit', self.logic_edit)
        self.add_button_logic('button-reset', self.reset)
        self.add_button_logic('button-add-particule', self.logic_add_p)
        self.add_button_logic('button-add-field', self.logic_add_f)
    
    def reset(self):
        self.system.clear_elements()

        if not self.paused:
            self.change_pause_state()
        self.current_time = 0

    def change_pause_state(self):
        '''
        Update `paused` attr, timer & start/stop button
        '''
        self.paused = not self.paused
        
        if self.paused:
            self.current_time += time.time() - self.start_time
            self.start_time = None
        else:
            self.start_time = time.time()
        
        if self.paused:
            self.set_text('button-start', "Start")
        else:
            self.set_text('button-start', "Stop")

    def logic_random(self):
        '''Generate a random situation'''
        if not self.paused:
            self.change_pause_state()
        
        self.reset()
        
        n_particule = np.random.randint(60, 120)

        taken_positions = []

        for i in range(n_particule):
            x = np.random.randint(32)
            y = np.random.randint(2, 16)

            if (x,y) in taken_positions:
                continue
            
            taken_positions.append((x,y))

            q = np.random.uniform(-5, 5)
            m = abs(q)
            p = Particule([x,y], q, m)
            self.system.add_particule(p)

        n_fields = np.random.randint(0, 5)

        for i in range(n_fields):
            x = np.random.randint(32)
            y = np.random.randint(2, 16)

            intensity = np.random.uniform(-5, 5)
            dispersion = np.random.uniform(1, 5)

            field = MagneticField(x, y, intensity, dispersion)
            self.system.add_magnetic_field(field)

    def logic_edit(self):

        if self.get_state() == 'base':
            self.change_state('edit')
            self.set_text('button-edit', 'Done')
        
        elif self.get_state() == 'edit':
            self.change_state('base')
            self.set_text('button-edit', 'Edit')
            self.mode_p = False
            self.mode_f = False
            self.change_option_display_state(False)

    def logic_add_p(self):
        self.mode_f = False
        self.mode_p = not self.mode_p
        self.change_option_display_state(self.mode_p)

        if self.mode_p:
            self.set_option_panel_particule()

    def logic_add_f(self):
        self.mode_p = False
        self.mode_f = not self.mode_f
        self.change_option_display_state(self.mode_f)

        if self.mode_f:
            self.set_option_panel_field()

    @delayer
    def is_pause(self, pressed):
        return pressed[pygame.K_SPACE]
    
    def handeln_pause(self, pressed):
        if self.is_pause(pressed):
            self.change_pause_state()
    
    def update_labels(self):
        
        # time
        if self.start_time is None:
            sec = self.current_time
        else:
            sec = self.current_time + time.time() - self.start_time
        
        decsec = int(10*(sec - int(sec)))

        _time = time.strftime('%M:%S', time.gmtime(sec))
        _time = f"{_time}.{decsec}"

        self.set_text('label-time', f"Time {_time}")

        # particules
        self.set_text('label-particules', f"Paricules {self.system.n_particules}")

    def is_pushed(self, events):
        '''Return if the mouse button has been pushed'''
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                return True
        return False

    def change_option_display_state(self, state: bool):
        self.change_display_state('options-panel', state)
        self.change_display_state('option-title', state)
        self.change_display_state('option-label1', state)
        self.change_display_state('option-label2', state)
        self.change_display_state('option-input1', state)
        self.change_display_state('option-input2', state)

    def set_option_panel_particule(self):
        '''
        Set the option panel for a particule
        '''
        self.set_text('option-label1', 'Charge')
        self.set_text('option-label2', 'Mass')
        self.set_text('option-input1', '+1')
        self.set_text('option-input2', '1')

    def set_option_panel_field(self):
        '''
        Set the option panel for a magnetic field
        '''
        self.set_text('option-label1', 'Intensity')
        self.set_text('option-label2', 'Dispersion')
        self.set_text('option-input1', '+1')
        self.set_text('option-input2', '2')

    def handeln_edit_releases(self, events):
        '''Handeln release of mouse button in edit mode'''

        header = self.get_component('header')
        panel = self.get_component('options-panel')

        if header.on_it() or panel.on_it():
            return

        if not self.is_pushed(events):
            return

        if self.mode_p:
            self.add_particule()
        
        if self.mode_f:
            self.add_field()
            
    def add_particule(self):
        '''Add a particule to the system'''
        pos = self.mode_p_ui.get_center() / Consts.SCALE_FACTOR

        charge = self.get_text('option-input1')
        try:
            charge = float(charge)
        except Exception:
            charge = 1
        
        mass = self.get_text('option-input2')
        try:
            mass = float(mass)
        except Exception:
            mass = 1

        particule = Particule(pos, charge, mass)

        self.system.add_particule(particule)

    def add_field(self):
        '''Add a field to the system'''
        pos = self.mode_f_ui.get_center() / Consts.SCALE_FACTOR

        intensity = self.get_text('option-input1')
        try:
            intensity = float(intensity)
        except Exception:
            intensity = 1
        
        dispersion = self.get_text('option-input2')
        try:
            dispersion = float(dispersion)
        except Exception:
            dispersion = 1

        field = MagneticField(pos[0], pos[1], intensity, dispersion)

        self.system.add_magnetic_field(field)

    def update_system(self):
        '''Update system state'''
        self.system.update()

    def react_events(self, pressed, events):
        
        self.update_labels()
        self.handeln_pause(pressed)
        
        if self.get_state() == 'edit':
            self.handeln_edit_releases(events)

        super().react_events(pressed, events)

    def display_particule_pointer(self):
        '''Display a particule where the mouse is located'''
        pos = pygame.mouse.get_pos()
        self.mode_p_ui.set_pos(pos, center=True, scale=False)
        self.mode_p_ui.display()

    def display_field_pointer(self):
        '''Display a field where the mouse is located'''
        pos = pygame.mouse.get_pos()
        self.mode_f_ui.set_pos(pos, center=True, scale=False)
        self.mode_f_ui.display()

    def display_system(self):
        fields = self.system.magnetic_fields

        field_ui = FieldUI(None)

        for field in fields:
            field_ui.field = field
            field_ui.display()

        particules = self.system.particules

        for particule in particules:
            particule_ui = ParticuleUI(particule)
            particule_ui.display()
    
    def display(self):
        self.display_system()
        
        if self.mode_p:
            self.display_particule_pointer()

        elif self.mode_f:
            self.display_field_pointer()

        super().display()