from pico2d import *

import game_world

class Bubble:

    image=None

    def __init__(self,x=400,y=90,velocity=0,timer=100):
      self.frame=0
      if Bubble.image==None:
        self.image = load_image('bubble_116.png')
      self.x,self.y,self.velocity,self.timer=x,y,velocity,timer
    def draw(self):
        #boy.frame=(boy.frame+1)%8
        self.frame=(self.frame+1)%4
        #self.image.cilp_draw(self.frame*60,0,60,45,self.x,self.y)
        self.image.clip_draw(self.frame*40,0,40,68,self.x,self.y)
    def update(self):
        self.timer-=1
        if (self.timer==0):
         game_world.remove_object(self)







