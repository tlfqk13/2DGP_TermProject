from pico2d import *

import game_world
from bubble_destroy import Bubble_destroy

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4
TIMER=200

class Bubble :
    image=None

    def __init__(self,x=0,y=0):
        self.frame=0
        self.image=load_image('resource/bubble_116.png')
        self.x=x
        self.y=y
        self.timer=200

    def draw(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 68, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def collide(self,a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def update(self):
        self.timer-=1
        if self.timer==0:
            global bubble_destroys
            bubble_destroys=Bubble_destroy(self.x,self.y)
            game_world.add_object(bubble_destroys,4)
            game_world.remove_object(self)

            boxList = game_world.get_layer(5)
            bubble_destroyList = game_world.get_layer(4)
            boyList=game_world.get_layer(1)

            for i in range(len(boxList)):
                if self.collide(bubble_destroyList[0], boxList[i]):
                    print("collsion2")
                    game_world.remove_object(boxList[i])
                    break

            for i in range(len(bubble_destroyList)):
                if self.collide(boyList[0],bubble_destroyList[i]):
                    print("collsion1")


