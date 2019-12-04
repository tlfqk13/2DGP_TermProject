from pico2d import *

class StaticBox:
    def __init__(self):
        self.image = load_image('resource/cookie_object_04.png')

    def draw(self):
      for i in range (17) :
        self.image.draw(25+(50*i),25)

      for i in range (15) :
        self.image.draw(25,25+(50*i))

      for i in range(15):
        self.image.draw(775,25+(50*i))

      for i in range(17):
        self.image.draw(25+(50*i),575)

    def update(self):
        pass


class Box:
    image = None

    def __init__(self,x,y):
        Box.image = load_image('resource/cookie_block_03.png')
        self.x=x
        self.y=y

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def update(self):
        pass

    def draw(self):
       self.image.draw(self.x,self.y)
       draw_rectangle(*self.get_bb())
       pass



    def stop(self):
        pass