# Square the circle
# by Elijah Medrano
# 1/27/22
# This program squares a circle with only TWO user inputs!!  (display width and shrink rate)

import pygame as pg
from math import pi, sqrt

pg.init()
display_w = 500  
display_h = display_w
window = pg.display.set_mode((display_w, display_h))
pg.display.flip()

white = (255, 255, 255)


def main():
  shrink_rate = 5  # only need to change the value of this variable; set shrink_rate = display_w / 2 to square one circle
  drawn = False    
  radius = int(display_w / 2)  # radius of circle
  iterations = int(radius / shrink_rate)  # number of circles squared
  center = (int(display_w / 2), int(display_h / 2))  # center of the display
  while 1:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        quit()
    if not drawn:  # only draw the image once
      for _ in [*range(0, iterations)]:  # square _ many circles
        area = pi * radius ** 2  # area of the circle and the square
        square_len = sqrt(area)  # square dimensions
        pg.draw.circle(window, white, center, radius, 1)
        pg.draw.rect(window, white, (center[0] - square_len / 2, center[1] - square_len / 2, 
                                     square_len, square_len), 1)
        radius -= shrink_rate
        pg.display.update()
        drawn = True
    
    
if __name__ == '__main__':
  main()
