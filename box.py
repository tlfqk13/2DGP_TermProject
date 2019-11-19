from pico2d import *
import random
import game_world
import game_framework

class Box:
    image=None

    def __init__(self):
     if Box.image==None:
         Box.image = load_image('pirate_object_08.png')
     self.x, self.y =50,60


    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def update(self):
        pass

    def draw(self):
        self.x+=self.x
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def stop(self):
        pass