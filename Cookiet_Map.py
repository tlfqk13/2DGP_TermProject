from pico2d import *


class Stage:
    def __init__(self):
        self.image = load_image('cookie_tile_01.png')
        self.x, self.y = 50, 25
    def update(self):
        self.x += 100
        if(self.x>=800):
            self.y += 50
            self.x = 50
    def draw(self):
        self.image.draw(self.x, self.y, 100, 50)
