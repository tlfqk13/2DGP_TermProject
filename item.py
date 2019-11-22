from pico2d import *
import random
import game_world
import game_framework
from boy import Boy

class Item:
    def __init__(self):
        self.image_1 = load_image('item_64.png')
        self.image_2=load_image('item_038.png')
        self.image_3=load_image('item_065.png')
        self.x,self.y=random.randint(200,500),random.randint(200,500)
        self.timer=300
    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def draw(self):
        self.image_2.draw(self.x,self.y)

    def update(self):
      self.timer-=1
      if(self.timer==0):
          game_world.remove_object(self)

      pass
