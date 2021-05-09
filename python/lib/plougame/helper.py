import pygame

def mean(array):
    total = 0
    for v in array:
        total += v
    return total/len(array)

def center_text(dim_box, font, text, *, ignore_exception=True):
    
    width, height = font.size(text)
    if width > dim_box[0] or height > dim_box[1]:
        if not ignore_exception:
            raise ValueError("Dimension too small for text.")
        
    x_marge = int((dim_box[0] - width)/2)
    y_marge = int((dim_box[1] - height)/2)
    return x_marge, y_marge

def get_pressed_key(pressed):
    '''Return the keyboard input as str'''
    # get letters
    for i in range(97, 123):
        if pressed[i]:
            if pressed[pygame.K_LSHIFT]:
                return chr(i).upper()
            else:
                return chr(i)
    
    # get numbers
    for i in range(48, 58):
        if pressed[i]:
            return chr(i)
    
    if pressed[pygame.K_SPACE]:
        return ' '
    elif pressed[pygame.K_MINUS] and pressed[pygame.K_LSHIFT]:
        return '_'
    elif pressed[pygame.K_QUOTE] and pressed[pygame.K_LSHIFT]:
        return '?'

def get_dark_color(color):
    dark_color = []
    for i in range(3):
        if color[i] >= 20:
            dark_color.append(color[i] - 20)
        else:
            dark_color.append(0)
    return dark_color

def get_light_color(color):
    light_color = []
    for i in range(3):
        if color[i] <= 235:
            light_color.append(color[i] + 20)
        else:
            light_color.append(255)
    return light_color

class Delayer:
    '''
    Creates decorators,

    The decorated function should return True/False depending on whether or not it has been activated,
    if true, creates a delay in order to not be spammed.
    '''
    wait = 0
    delayed = False
    def __init__(self, delay):
        self.delay = delay
        
    def __call__(self, func):
        def inner(*args, **kwargs):
            if self.delayed:
                self.wait += 1
                if self.wait == self.delay:
                    self.delayed = False
                    self.wait = 0
            else:
                # first argument if a boolean value of if the tested key was pressed
                executed = func(*args, **kwargs)
                if executed:
                    self.delayed = True
                return executed
        return inner