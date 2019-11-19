from pico2d import *
import random
import game_world
import game_framework

class Box:
    def __init__(self):
        self.image = load_image('pirate_object_08.png')
        self.x, self.y = 500, 260

    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)
        #print(self.x,self.y)
        draw_rectangle(*self.get_bb())