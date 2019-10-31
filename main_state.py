import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import game_world

from boy import Boy
from map import Map
from bubble import Bubble

name = "MainState"

boy = None
grass = None
font = None
bubble=None
map=None


def enter():
    global boy
    boy=Boy()
    map=Map()
    game_world.add_object(map,0)
    game_world.add_object(boy,1)


def exit():
    game_world.clear()

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
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





