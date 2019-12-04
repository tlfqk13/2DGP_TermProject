
from pico2d import *

import game_framework
import title_state
import pause_state
import game_world

from boy import Boy
from girl import Girl
from map import Map
from box import Box
from game_start import Start
from item import Item
from boss import Boss
from enemy_bubble import Enemy_bubble

playtime=0.0
name = "MainState"

boy = None
map=None

#game play time
Playtime=0.0

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():

    global Playtime
    Playtime=get_time()

    global boy
    boy=Boy()
    game_world.add_object(boy, 1)

    global enemy_bubbles
    enemy_bubbles=[Enemy_bubble()for i in range (10)]
    for i in range(10) :
        game_world.add_object(enemy_bubbles[i],8)

    global map
    map=Map()
    game_world.add_object(map,0)

    ## bulid box !!##
    global box_x,box_y,box_center_x,box_center_y
    box_x=[Box(40*(i+1),55) for i in range(15)]\
          +[Box(40*(i+1),540) for i in range(15)]
    for i in range(30):
        game_world.add_object(box_x[i],5)
    box_y = [Box(40,42*(i+2)) for i in range(11)]+[Box(600,42*(i+2))for i in range(10)]
    for i in range(21):
        game_world.add_object(box_y[i], 5)
    box_center_x=[Box(40*(i+3),275)for i in range(5)]+[Box(40*(i+3),125)for i in range(5)]
    box_center_y=[Box(120,42*(i+3)) for i in range(4)]+[Box(280,42*(i+3))for i in range(4)]
    for i in range(10):
        game_world.add_object(box_center_x[i],5)
    for i in range(8):
        game_world.add_object(box_center_y[i],5)

    global boss
    boss=Boss()
    game_world.add_object(boss,1)

    global start
    start = Start()
    game_world.add_object(start, 3)


def exit():

    game_world.clear()

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
        #elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_e):
            #game_framework.change_state()
        else:
            boy.handle_event(event)

def update():

   for game_object in game_world.all_objects():
        game_object.update()

   boxList=game_world.get_layer(5)
   itemList=game_world.get_layer(3)
   enemyList=game_world.get_layer(8)

   #for i in range(len(enemyList)):
       #game_world.remove_object(enemyList[i])

   global Playtime
   Playtime=get_time()
   #print(Playtime)
   #if (Playtime>=7):
    #global items
    #items=Item()
    #game_world.add_object(items,3)

   for i in range(len(itemList)):
       if collide(boy,itemList[i]):
        print("item")
        boy.boy_speed()
        game_world.remove_object(itemList[i])
        break

   for i in range(len(boxList)):
       if collide(boy,boxList[i]):
        print("box_collide")
        boy.stop()
        break


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




