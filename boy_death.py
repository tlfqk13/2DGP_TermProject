
from pico2d import *

class Death:
    image=None
    b_image=None
    def __init__(self):
      self.frame=0
      self.image = load_image('Characbub0.png')
      self.timer=200
      self.x,self.y=400,300
    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30
    def draw(self):
        self.frame=(self.frame+1)%4
        self.image.clip_draw(self.frame*60,0,60,65,self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
       pass
















