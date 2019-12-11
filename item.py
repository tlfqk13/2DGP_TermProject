import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import moster

import main_state
from zombie import Zombie


boy = None
zombies=[]
GameObject=None

name = "WorldBuildState"

menu = None

# Monster1 생성시간
time_CreateMonster=10.0
time_UpdateCreateMonster=10.0

# Monster 생성 인자.
Monster_Hp = 100
Monster_Speed = 1
Monster_Exp = 50

#Monster 생성 위치
posX=random.randint(75,750)
posY=random.randint(75,550)
posOffsetX=100

#Game Play Time
playTime=0.0

def enter():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    global playTime
    playTime = 0.0

    del menu

def pause():
    pass

def resume():
    pass

def get_boy():
    return boy

def create_new_world():

    global playTime
    playTime = get_time()
    print(playTime)

    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    with open('zombie_data.json','r') as f:
        zombie_data_list=json.load(f)

    for data in zombie_data_list:
        zombie=Zombie(data['name'],data['x'],data['y'],data['size'])
        zombies.append(zombie)
        game_world.add_object(zombie,6)

    global time_CreateMonster
    global time_UpdateCreateMonster

    global posX
    global posY
    global posOffsetX

    global Monster_Hp
    global Monster_Speed
    global Monster_Exp

    time_CreateMonster += 0.1

    if playTime>=5:
        print('make_monster')
        for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
            PosX = posX + posOffsetX * n
            Monster_Hp = 100
            Monster_Speed = 400
            Monster_Exp = 50
            # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
            GameObject = moster.CMonster(PosX, posY,
                                         114, 76, Monster_Hp, Monster_Speed, 25,
                                         Monster_Exp, "Enemy01.png")

            game_world.add_object(GameObject, 8)
            # game_world.remove_object(GameObject)
            pass

def load_saved_world():
    global boy

    # fill here
def get_monsters():
    return GameObject

def get_zombies():
    return zombies

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load_saved_world()
            game_framework.change_state(main_state)

def update():
    pass


def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()


def load_saved_world():
    global boy

    game_world.load()
    for o in game_world.all_objects():
        if isinstance(o,Boy):
            boy=o
            break
