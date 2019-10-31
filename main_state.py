import random
import json
import os

from pico2d import *

import game_framework
#import title_state
#import pause_state
import game_world

from boy import Boy
from map import Map

from bubble import Bubble

name = "MainState"

boy = None
map=None

def collide(a,b):

    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global boy
    boy=Boy()
    game_world.add_object(boy, 1)

    global map
    map=Map()
    game_world.add_object(map,0)

    global bubbles
    bubbles= [Bubble() for i in range(10)]
    game_world.add_object(bubbles,1)

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
       # elif (event.type, event.key) ==(SDL_KEYDOWN ,SDLK_SPACE):
            #game_framework.change_state(title_state)
        #elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
            #game_framework.push_state(pause_state)

        else:
            boy.handle_event(event)
def update():

    for game_object in game_world.all_objects():
        game_object.update()
    for bubble in bubbles:
        if collide(boy,bubbles):
            print("Collision")
    pass

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




