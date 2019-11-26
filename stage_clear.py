from pico2d import *
import random
import game_world
import game_framework

class Clear:
    def __init__(self,x=0,y=0):
        self.image=load_image('resource/clear.png')
        self.x,self.y=x,y
        self.timer=300

    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
      self.timer-=1
      if(self.timer==0):
          game_world.remove_object(self)


