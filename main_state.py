
from pico2d import *
import game_framework
import game_world

from boy import Boy
from map import Map
from staticbox import StaticBox,Box
from enemy_bubble import EnemyBubble
from zombie import Zombie

import world_build_state

boy = None
map=None
staticbox=None
zombies=[]

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
    boy=world_build_state.get_boy()
    game_world.add_object(boy, 1)

    global zombies
    zombies=world_build_state.get_zombies()

    global map
    map=Map()
    game_world.add_object(map,0)

    global staticbox
    staticbox=StaticBox()
    game_world.add_object(staticbox,0)

    global box

    box = [Box(325 + (50 * i), 225) for i in range(4)] + \
          [Box(325 + (50 * i), 425) for i in range(4)] + \
          [Box(275,275+(50*i))for i in range (3)]+\
          [Box(525,275+(50*i))for i in range(3)]

    for i in range(14):
        game_world.add_object(box[i], 5)

    global enemy_bubbles
    enemy_bubbles=[EnemyBubble()for i in range (10)]

    for i in range(10) :
        game_world.add_object(enemy_bubbles[i],8)



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
        else:
            boy.handle_event(event)

def update():

   for game_object in game_world.all_objects():
        game_object.update()

   boxList=game_world.get_layer(5)

   for i in range(len(boxList)):
       if collide(boy,boxList[i]):
           print("box_collide")

   for zombie in zombies:
       if collide(boy,zombie):
           print("zombie_collide")

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




