from pico2d import *

import game_world
import bubble

class Bubble_destroy:
    def __init__(self):
      self.frame=0
      self.b_image = load_image('padoexLeft.png')
      self.timer=300
    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30
    def draw(self):
        self.x=500
        self.y=300
        self.frame=(self.frame+1)%4
        self.b_image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer-=1
        if self.timer==0 :
         game_world.remove_object(self)

        pass





