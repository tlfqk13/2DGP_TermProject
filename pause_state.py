
from pico2d import *

import game_framework
import main_state

name="Pause_state"
image=None
pause=None

class Pause:
    def __init__(self):
        self.image=load_image('ui_mainexit.png')

    def draw(self):
         self.image.draw(400,400)


def enter():
    global pause
    pause=Pause()
    pass

def exit():
    global pause
    del(pause)
    pass

def pause():

    pass


def resume():
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) ==(SDL_KEYDOWN,SDLK_p):
            game_framework.pop_state()
            #game_framework.pop_state()

    pass


def update():
    pass

def draw():
    clear_canvas()
    main_state.draw()
    pause.draw()
    update_canvas()
    pass





