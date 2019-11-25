from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('resource/b0s2w-n8tki.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400,300)
