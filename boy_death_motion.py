
from pico2d import *
import game_world

from stage_clear import Clear

class Death_Motion:
    image=None
    b_image=None
    def __init__(self,x=400,y=300):
      self.frame=0
      self.image = load_image('resource/Die.png')
      self.timer=3000
      self.x,self.y=x,y
    #def get_bb(self):
      #  return self.x-30,self.y-30,self.x+30,self.y+30
    def draw(self):

        if self.frame <=8 :
         self.frame=(self.frame+1)
         self.image.clip_draw(self.frame*70,0,70,110,self.x,self.y)
         delay(0.1)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.timer -= 1
        if (self.timer == 0):
            game_world.remove_object(self)
            global clears
            clears=Clear(self.x,self.y)
            game_world.add_object(clears,3)
















