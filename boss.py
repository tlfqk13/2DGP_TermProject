from pico2d import *

class Boss:

    def __init__(self):
        self.frame = 0
        self.image = load_image('resource/boss_fire.png')
        self.x, self.y = 400,300

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw(self):
        self.frame = (self.frame + 1) % 3
        self.image.clip_draw(self.frame * 230, 0, 230,500, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        pass
