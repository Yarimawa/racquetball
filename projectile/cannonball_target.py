from graphics import *
from random import randrange

class Target:

    def __init__(self, win):
        self.win = win
        x = randrange(210)
        self.p = Rectangle(Point(x,-1),Point(x+6,1))
        self.p.setFill('yellow')
        self.p.draw(win)

    def BullsEye(self, value1, value2):
        x = self.p.getCenter()
        x = x.getX()
        return x-6 <= value1 and x+6 >= value2

    def redraw(self):
        self.p.undraw()
        x = randrange(210)
        self.p = Rectangle(Point(x,-1),Point(x+6,1))
        self.p.setFill('yellow')
        self.p.draw(self.win)

    def move(self, dx):
        self.p.move(dx, 0)
        
    def getCenter(self):
        return self.p.getCenter()
