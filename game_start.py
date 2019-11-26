from pico2d import *
import random
import game_world
import game_framework
from boy import Boy

class Start:
    def __init__(self):
        self.image=load_image('resource/start.png')
        self.x,self.y=400,300
        self.timer=300
    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def draw(self):
         self.image.draw(self.x,self.y)

    def update(self):
      self.timer-=1
      if(self.timer==0):
          game_world.remove_object(self)

      pass
