from pico2d import *

import game_world
import bubble

class Bubble_destroy:
    image=None
    def __init__(self):
      if Bubble_destroy.image==None:
       Bubble_destroy.image = load_image('padoexLeft.png')
       self.timer=300
       self.x,self.y=200,300
    def get_bb(self):
        return self.x-60,self.y-25,self.x+60,self.y+25
    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer-=1
        if self.timer==0 :
         game_world.remove_object(self)
        pass





