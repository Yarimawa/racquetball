# Launcher.py
from math import radians, sin, cos, degrees
from shottracker import ShotTracker
from graphics import *

class Launcher:

    def __init__(self, win):
        # draw the base shot of the launcher
        base = Circle(Point(0,0),3)
        base.setFill("red")
        base.setOutline("red")
        base.draw(win)

        # save the window and create initial angle and velocity
        self.win = win
        self.angle = radians(45.0)
        self.vel = 40.0

        # create initial "dummy" arrow (needed by redraw)
        self.arrow = Line(Point(0,0),Point(0,0)).draw(win)
        # replace it with the correct arrow
        self.redraw()

    def adjAngle(self, amt):
        """Change launch angle by amt degrees"""

        self.angle = self.angle + radians(amt)
        self.redraw()

    def adjVel(self, amt):
        """Change launch velocity by amt"""

        self.vel = self.vel + amt
        self.redraw()

    def redraw(self):
        """redraw the arrow to show current angle and velocity"""

        self.arrow.undraw()
        pt2 = Point(self.vel*cos(self.angle),
                    self.vel*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)

    
