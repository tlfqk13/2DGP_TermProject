from pico2d import *

import game_world

class Bubble:

    image=None

    def __init__(self,x=400,y=90,velocity=0):
      self.frame=0
      if Bubble.image==None:
        self.image = load_image('Characbub2.png')
      self.x,self.y,self.velocity=x,y,velocity
    def draw(self):
        #boy.frame=(boy.frame+1)%8
        self.frame=(self.frame+1)%4
        #self.image.cilp_draw(self.frame*60,0,60,45,self.x,self.y)
        self.image.clip_draw(self.frame*60,0,60,65,self.x,self.y)
    def update(self):
        self.x+=self.velocity







