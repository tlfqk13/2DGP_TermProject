from pico2d import *

class Bubble:
    def __init__(self,x=400,y=90,velocity=1):

        self.x,self.y=400,90
        self.frame=0
        self.image = load_image('Characbub0.png')
        self.timer=100
    def update(self):
        self.frame = (self.frame + 1) % 4
        self.timer-=10
    def draw(self):
        if timer!=0:
         self.image.clip_draw(self.frame*60,0,60,65,self.x,self.y)




