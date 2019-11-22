from pico2d import *
import random
import game_world
import game_framework

class Box:
    image=None
    def __init__(self,x,y):
     if Box.image==None:
         Box.image = load_image('pirate_object_08.png')
     self.x,self.y=x,y

    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def stop(self):
        pass