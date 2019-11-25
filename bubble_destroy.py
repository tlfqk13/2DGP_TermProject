from pico2d import *

import game_world

class Bubble_destroy:
    image=None

    def __init__(self, x=400, y=300):
        self.frame = 0
        self.image = load_image('resource/padoexLeft.png')
        self.x, self.y = x, y
        self.timer = 200



    def get_bb(self):
        return self.x - 65, self.y - 10, self.x + 65, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer -= 1
        if (self.timer == 0):
            game_world.remove_object(self)





