import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

from boy import Boy
from map import Map
from bubble import Bubble

name = "MainState"

boy = None
grass = None
font = None
bubble=None


def enter():
    global boy,map,bubble
    boy=Boy()
    map=Map()
    bubble=Bubble()
    pass

def exit():
    global boy,map,bubble
    del(boy)
    del(map)
    del(bubble)

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
        elif (event.type, event.key) ==(SDL_KEYDOWN ,SDLK_SPACE):
            game_framework.change_state(title_state)
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
            game_framework.push_state(pause_state)
        else:
            boy.handle_event(event)


def update():
    boy.update()
    bubble.update()
    pass


def draw():
    clear_canvas()
    map.draw()
    boy.draw()
    bubble.draw()
    update_canvas()
    pass





