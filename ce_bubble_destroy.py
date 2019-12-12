from pico2d import *
import boy
import game_world
import boy


class Ce_Bubble_destroy:
    image=None
    boy = None

    def __init__(self, x=400, y=300):
        self.frame = 0
        self.center_image = load_image('resource/bombwater_start.png')
        self.x, self.y = x, y
        self.timer =100


    def collide(self,a,b):

        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb(self):
        return self.x -25, self.y -25, self.x + 25, self.y + 25

    def collide1(self,a,b):

        left_a, bottom_a, right_a, top_a = a.get_bb2()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb2(self):
        return self.x-0,self.y-0,self.x+0,self.y+0

    def draw(self):
         self.center_image.draw(self.x, self.y)
         draw_rectangle(*self.get_bb())



    def update(self):
        self.timer -= 1
        if self.timer == 0:
            game_world.remove_object(self)






