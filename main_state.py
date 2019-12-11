
from pico2d import *
import game_framework
import game_world
import random
import moster
import objectMgr
import boy
import map
from map import Map
from staticbox import StaticBox,Box
from enemy_bubble import EnemyBubble
from bubble import Bubble
from zombie import Zombie


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
posOffsetX=50

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

    gameObject=boy.CBoy()
    objectMgr.add_gameobject(gameObject,"Player")


    global map
    map=Map()
    game_world.add_gameobject(map,0)

    global staticbox
    staticbox=StaticBox()
    game_world.add_gameobject(staticbox,0)

    global box

    box = [Box(325 + (50 * i), 225) for i in range(4)] + \
          [Box(325 + (50 * i), 425) for i in range(4)] + \
          [Box(275,275+(50*i))for i in range (3)]+\
          [Box(525,275+(50*i))for i in range(3)]

    for i in range(14):
        game_world.add_gameobject(box[i], 5)


def exit():
    global playTime
    global time_CreateMonster

    playTime=0.0
    time_CreateMonster=0.0

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

    objectMgr.handle_events()
    pass

def update():

   global playTime
   playTime=get_time()
   print(playTime)

   objectMgr.update()

   global time_CreateMonster
   global time_UpdateCreateMonster

   global posX
   global posY
   global posOffsetX

   global Monster_Hp
   global Monster_Speed
   global Monster_Exp


   time_CreateMonster+=0.1

   if playTime>=3:
    for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
       print('make_monster')

       PosX = posX + posOffsetX*n
       Monster_Hp = 100
       Monster_Speed = 400
       Monster_Exp = 50
       # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
       GameObject = moster.CMonster(PosX,posY,
                                       114,76,Monster_Hp,Monster_Speed,25,
                                        Monster_Exp,"Enemy01.png")

       objectMgr.add_gameobject(GameObject,"Monster")
       #game_world.remove_object(GameObject)
       pass



def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()
    objectMgr.draw()

    update_canvas()




