from pico2d import *

import game_world
import game_framework

class Bubble:

    image=None
    b_image=None
    def __init__(self,x=400,y=90,timer=400):
      self.frame=0
      if Bubble.image==None:
        self.image = load_image('bubble_116.png')
      self.x,self.y,self.timer=x,y,timer

    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def draw(self):
        self.frame=(self.frame+1)%4
        self.image.clip_draw(self.frame*40,0,40,68,self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        #self.timer-=1
        #if (self.timer==0):
         #game_world.remove_object(self)
        pass










