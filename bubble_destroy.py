from pico2d import *
from bubble import Bubble

import game_world

class Bubble_destroy:
    image=None
    b_image=None
    def __init__(self,x=400,y=90,velocity=0,start_timer=400,timer=400):
      self.frame=0
      if Bubble_destroy.image==None:
        self.b_image = load_image('padoexLeft.png')
      self.x,self.y,self.velocity,self.start_timer,self.timer\
          =x,y,velocity,start_timer,timer
    def draw(self):
         self.frame=(self.frame+1)%4

         self.b_image.draw(self.x,self.y)
    def update(self):
        pass





