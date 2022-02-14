# metatron's cube

import pygame as pg
import time
from math import sin, cos, pi

pg.init()
display_w = 500
display_h = display_w
window = pg.display.set_mode((display_w, display_h))
pg.display.flip

white = (255, 255, 255)


class Circle:
  def __init__(self):
    self.radius = display_w / 10
    self.theta = pi / 6
    self.hypotenuse = 2 * self.radius
    self.display_center = [display_w / 2, display_h / 2]
    self.center = [self.display_center[0], self.display_center[1]]
    self.centers = []
    self.drawn = False

  def draw(self):
    i = 0
    for _ in [*range(0, 14)]:
      if i > 12:  # draw outer circle
        self.center = self.display_center
        self.radius = display_w / 2
      pg.draw.circle(window, white, (int(self.center[0]), int(self.center[1])), int(self.radius), 1)
      self.center[0] = self.display_center[0] + self.hypotenuse * cos(self.theta)  # update circle center
      self.center[1] = self.display_center[1] - self.hypotenuse * sin(self.theta)
      if i < 13:  # don't append the last center bc it's the large outer circle 
        center = self.center[:]  # create a copy so that they are not the same object
        self.centers.append(center)  # append current center to list of centers
      self.theta += pi / 3  # increment theta to adjust position of next circle
      i += 1  # increment iteration counter
      if i == 6:  # if done drawing inner layer of circles, double the hypotenuse to draw outer layer
        self.hypotenuse += self.hypotenuse
      time.sleep(.2)  # pause for effect
      pg.display.update()  # this update displays one circle at a time
    for i in self.centers:
      for j in self.centers:
        pg.draw.line(window, white, i, j)
        time.sleep(.2)
        pg.display.update()  # this update displays one line at a time
    self.drawn = True  # use bool to only draw once (see main loop)


def main():
  metatrons_cube = Circle()
  while 1:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        quit()
    if not metatrons_cube.drawn:  # the function only runs once
      metatrons_cube.draw()  # draw the cube
        

if __name__ == '__main__':
  main()
