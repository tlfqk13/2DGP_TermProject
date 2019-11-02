from pico2d import *
import random
import game_world
import game_framework

class Box:
    def __init__(self):
        self.image = load_image('pirate_object_08.png')
        self.x, self.y = 40, 60

    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def update(self):
        pass

    def draw(self):
        self.x =30
        self.y =self.y+30
        self.image.draw(self.x,self.y)

