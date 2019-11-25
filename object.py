from pico2d import *

class object:
    def __init__(self, imageString = None):
        self.image = None
        if imageString is not None:
            self.image = pico2d.load_image(imageString)
            self.imageWidth = self.image.w
            self.imageHeight = self.image.h
        self.x = 0
        self.y = 0
        self.clipWidth = 0
        self.clipHeight = 0
        self.left = 0
        self.bottom = 0

    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y, self.imageWidth, self.imageHeight)
    def clip_draw(self):
        self.image.clip_draw(self.left,self.bottom,
                             self.clipWidth, self.clipHeight,
                             self.x, self.y,
                             self.imageWidth, self.imageHeight)
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def setSize(self, w, h):
        self.imageWidth = w
        self.imageHeight = h
    def setClipSize(self, w, h):
        self.clipWidth = w
        self.clipHeight = h
    def changeClipFrame(self, left, bottom):
        self.left = left
        self.bottom = bottom
    def setImage(self, imageString):
        if self.image is not None:
            del self.image
        self.image = pico2d.load_image(imageString)
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h
    def getPos(self):
        return self.x, self.y


