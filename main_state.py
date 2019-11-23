import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import game_world

from boy import Boy
from girl import Girl
from map import Map
from box import Box
from bubble import Bubble
from item import Item
from boss import Boss
from boy_death import Death

from Cookiet_Map import Stage

from bubble_destroy import Bubble_destroy

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

    global girl
    girl=Girl()
    #game_world.add_object(girl,2)

    #global stage
    #stage=Stage()
    #game_world.add_object(stage,0)

    global boss
    boss=Boss()
    #game_world.add_object(boss,1)

    global map
    map=Map()
    game_world.add_object(map,0)

    global bubbles
    #bubbles=Bubble()
    #game_world.add_object(bubbles,1)
    bubbles= [Bubble() for i in range(10)]
    for i in range(10):
     game_world.add_object(bubbles[i],1)

    global deaths
    deaths=Death()
    game_world.add_object(deaths,1)

    ## bulid box !!##
    global box_x,box_y,box_center_x,box_center_y
    box_x=[Box(40*(i+1),55) for i in range(15)]+[Box(40*(i+1),540) for i in range(15)]
    for i in range(30):
        game_world.add_object(box_x[i],1)
    box_y = [Box(40,42*(i+2)) for i in range(11)]+[Box(600,42*(i+2))for i in range(10)]
    for i in range(21):
        game_world.add_object(box_y[i], 1)
    box_center_x=[Box(40*(i+3),275)for i in range(5)]+[Box(40*(i+3),125)for i in range(5)]
    box_center_y=[Box(120,42*(i+3)) for i in range(4)]+[Box(280,42*(i+3))for i in range(4)]
    for i in range(10):
        game_world.add_object(box_center_x[i],1)
    for i in range(8):
        game_world.add_object(box_center_y[i],1)

    global bubble_destroy
    bubble_destroy=Bubble_destroy()
    game_world.add_object(bubble_destroy,1)

    global item
    item=[Item() for i in range(10)]
    game_world.add_objects(item,1)


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
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            game_framework.change_state(title_state)
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
            game_framework.push_state(pause_state)
        else:
            boy.handle_event(event)

def update():
   for game_object in game_world.all_objects():
        game_object.update()

   if collide(boy,bubble_destroy):
      game_world.remove_object(boy)

   for i in range(30):
    if collide(boy,box_x[i]):
      game_world.remove_object(box_x)
      print("Collision")
   for i in range(21):
       if collide(boy,box_y[i]):
           game_world.remove_object(box_y)
           print("collision")

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




