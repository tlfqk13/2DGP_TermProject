from pico2d import *
from bubble import Bubble

import game_world

class Bubble_destroy:
    def __init__(self):
      self.frame=0
      self.b_image = load_image('padoexLeft.png')
      self.timer=300
    def draw(self):
        self.x=400
        self.y=300
        self.frame=(self.frame+1)%4
        self.b_image.draw(self.x,self.y)
    def update(self):
        self.timer-=1
        if self.timer==0 :
            game_world.remove_object(self)

        pass





