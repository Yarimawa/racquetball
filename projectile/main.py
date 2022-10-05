# ProjectileApp.py
from graphics import *
from launcher import Launcher
from cannonball_target import Target

######
##        AND 21
######

class ProjectileApp:

    def __init__(self):
        # create graphics window with a scale line at the bottom
        self.win = GraphWin("Projectile Animation", 640, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10,0),Point(210,0)).draw(self.win)
        for x in range(0,210,50):
            Text(Point(x,-7), str(x)).draw(self.win)
            Line(Point(x,0),Point(x,2)).draw(self.win)

        # add the launcher to the window
        self.launcher = Launcher(self.win)

        # start with an empty list of "live" shots
        self.shots = []

        # create target rectangle
        self.target = Target(self.win)

    def updateShots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and -10 < shot.getX() < 210:
                alive.append(shot)
            else:
                if self.target.BullsEye(shot.getX(), shot.getX()):
                    self.win.getMouse()
                    self.target.redraw()                    
                shot.undraw()
        self.shots = alive
    
    def run(self):

        # main event/animation loop
        while True:    
            self.updateShots(1/30)
            
            key = self.win.checkKey()
            if key in ["Q", "q"]:
                break            

            if key == "Up":
                self.launcher.adjAngle(5)
            elif key == "Down":
                self.launcher.adjAngle(-5)
            elif key == "Right":
                self.launcher.adjVel(5)
            elif key == "Left":
                self.launcher.adjVel(-5)
            elif key in ["w", "W"]:
                self.launcher.adjHeight(5)
            elif key in ["s", "S"]:
                self.launcher.adjHeight(-5)
            elif key in ["f", "F"]:
                self.shots.append(self.launcher.fire())

            update(30)

        self.win.close()

if __name__ == '__main__':
    ProjectileApp().run()
