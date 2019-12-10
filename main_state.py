
from pico2d import *
import game_framework
import game_world
import random
import moster

from boy import Boy
from map import Map
from staticbox import StaticBox,Box
from enemy_bubble import EnemyBubble
from bubble import Bubble
from zombie import Zombie


import world_build_state

boy = None
map=None
staticbox=None
zombies=[]

# Monster1 생성시간
time_CreateMonster=10.0
time_UpdateCreateMonster=10.0

# Monster 생성 인자.
Monster_Hp = 100
Monster_Speed = 3
Monster_Exp = 50

#Monster 생성 위치
posX=random.randint(75,750)
posY=random.randint(75,550)
posOffsetX=114

#Game Play Time
playTime=0.0

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

def exit():
    global playTime
    global time_CreateMonster

    playTime=0.0
    time_CreateMonster=0.0
    game_world.clear()

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            boy.handle_event(event)

def update():

   global playTime
   playTime=get_time()
   print(playTime)

   for game_object in game_world.all_objects():
        game_object.update()

   boxList=game_world.get_layer(5)
   zombieList=game_world.get_layer(6)

   for i in range(len(boxList)):
       if collide(boy,boxList[i]):
           print("box_collide")


   for i in range(len(zombieList)):
       if collide(boy,zombieList[i]):
           print("zombie_collide")

   global time_CreateMonster
   global time_UpdateCreateMonster

   global posX
   global posY
   global posOffsetX

   global Monster_Hp
   global Monster_Speed
   global Monster_Exp

   time_CreateMonster+=0.1

   if time_CreateMonster>=time_UpdateCreateMonster:
       print('make_monster')
       for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
           PosX = posX + posOffsetX * n
           Monster_Hp = 100
           Monster_Speed = 400
           Monster_Exp = 50
           # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
           GameObject = moster.CMonster(PosX,posY,
                                        114,76,Monster_Hp,Monster_Speed,25,
                                        Monster_Exp,"Enemy01.png")

           game_world.add_object(GameObject,8)
           pass


       pass

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




