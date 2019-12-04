from pico2d import *

import game_world

class Bubble_destroy:
    image=None

    def __init__(self, x=400, y=300):
        self.frame = 0
        self.image = load_image('resource/bombwater_center.png')
        self.x, self.y = x, y
        self.timer = 200


    def collide(self,a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb(self):
        return self.x - 65, self.y - 10, self.x + 65, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            game_world.remove_object(self)

class enemyBubbleDestroy:

    def __init__(self, x=400, y=300):
        self.frame = 0
        self.image = load_image('resource/bombwater_center.png')
        self.x, self.y = x, y
        self.timer = 200


    def collide(self,a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb(self):
        return self.x - 65, self.y - 10, self.x + 65, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            game_world.remove_object(self)





