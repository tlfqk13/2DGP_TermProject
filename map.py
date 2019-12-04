from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('resource/cookie_tile_01.png')

    def update(self):
        pass
    def draw(self):
        #for i in range (17) :
         #   self.image.draw(25+(50*i),25)

        #for i in range (15) :
         #   self.image.draw(25,25+(50*i))

        #for i in range(15):
         #   self.image.draw(75,25+(50*i))

        for j in range(17):
            for i in range(15):
                self.image.draw(25+(50*j),25+(50*i))