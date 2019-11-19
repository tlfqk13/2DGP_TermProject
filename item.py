from pico2d import *
import random
import game_world
import game_framework
from boy import Boy

class Item:
    def __init__(self):
        self.image = load_image('item_64.png')

    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10

    def draw(self):
        self.x=320
        self.y=240
        self.image.draw(self.x, self.y)

    def update(self):
        self.x,self.y=320,240
        #self.boy.velocity+=30