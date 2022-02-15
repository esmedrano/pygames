import pygame as pg
from math import pi, sin, cos

pg.init()
DISPLAY_W = 500
DISPLAY_H = 500
window = pg.display.set_mode((DISPLAY_W, DISPLAY_H))
pg.display.flip()

CENTER = (DISPLAY_W // 2, DISPLAY_H // 2)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SQRT_2 = 1.4142
SQRT_3 = 1.7321


class Regular_Polygon:
  def __init__(self, surface, color, side_num, pos, side_len):
    self.color = color
    self.surface = surface
    self.side_num = side_num
    self.pos = pos
    self.side_len = side_len
    
  def draw(self):
    rotation_ang =  2 * pi / self.side_num
    endpoint = [0, 0]
    for _ in [*range(0, self.side_num)]:
      endpoint[0] += self.side_len * cos(rotation_ang)
      endpoint[1] += self.side_len * sin(rotation_ang)
      pg.draw.line(self.surface, self.color, self.pos, endpoint)
  

def stone_of_philosophers(center_radius):
  triangle = Regular_Polygon(window, RED, 3, (CENTER[0] + 2 * center_radius, CENTER[1] + 2 * center_radius), 
                             2 * center_radius + 2 * center_radius / SQRT_3 * 2)
  pg.draw.circle(window, BLUE, CENTER, center_radius, 1)
  pg.draw.rect(window, GREEN, (CENTER[0] - center_radius, CENTER[1] - center_radius, 
                               center_radius * 2, center_radius * 2), 1)
  triangle.draw()
  pg.draw.circle(window, WHITE, CENTER, 2 * center_radius, 1)


def main():
  radius = 100
  isStoned = False
  while 1:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        quit()
    if not isStoned:
      stone_of_philosophers(radius)
      pg.display.update()
      isStoned = True
        

if __name__ == '__main__':
  main()
