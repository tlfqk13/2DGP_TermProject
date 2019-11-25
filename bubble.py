from pico2d import *

import game_world
import game_framework
from bubble_destroy import Bubble_destroy
#from boy import Boy

class Bubble:
    image=None
    b_image=None

    def __init__(self,x=0,y=0):
      self.frame=0
      self.image = load_image('bubble_116.png')
      self.x,self.y=x,y
      self.timer=200

    def collide(self,a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30
    def draw(self):
        self.frame=(self.frame+1)%4
        self.image.clip_draw(self.frame*40,0,40,68,self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer-=1
        if (self.timer==0):
          game_world.remove_object(self)
          global bubble_destroys
          bubble_destroys=Bubble_destroy(self.x,self.y)
          game_world.add_object(bubble_destroys,4)
          bubble_destroysList=game_world.get_layer(4)
          boyList=game_world.get_layer(1)
          length=len(bubble_destroysList)
          print(length)
          for i in range(length):
           if self.collide(boyList[1],bubble_destroysList[i]):
               print("collision")
               game_world.remove_object(bubble_destroysList[i])











