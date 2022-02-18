# Phiolopher's Stone
# by Elijah Medrano
# 2/17/22
# This program draws the philosopher's stone using a regular polygon class to draw the triangle

import pygame as pg
import operator
from math import pi, sqrt, sin, cos

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
    self.vertices = []

  def draw(self):
    ops = {0: operator.add, 1: operator.sub, 3: 0}
    rotation_ang =  360 / self.side_num
    inner_angle = (self.side_num - 2) * pi / self.side_num
    angle_count = 0
    endpoint = self.pos[:]
    pos = self.pos[:]
    for i in [*range(0, self.side_num)]:
      angle_count += rotation_ang 
      if angle_count < 90:
        op_x = 0
        op_y = 1
      elif angle_count == 90:
        op_x = 3
        op_y = 1
      elif 90 < angle_count < 180:
        op_x = 1
        op_y = 1
      elif angle_count == 180:
        op_x = 1
        op_y = 3
      elif 180 < angle_count < 270:
        op_x = 1
        op_y = 0
      elif angle_count == 270:
        op_x = 3
        op_y = 0
      elif 270 < angle_count < 360:
        op_x = 0
        op_y = 0
      elif angle_count == 360:
        op_x = 0
        op_y = 3
      # angle_count = angle_count - i * 90
      angle_count = angle_count * pi / 180
      if op_x != 3:
        # endpoint[0] = ops[op_x](pos[0], self.side_len * abs(cos(inner_angle)))
        endpoint[0] = ops[op_x](pos[0], self.side_len * abs(cos(angle_count)))
        if op_y == 3:
          endpoint[0] = ops[op_x](pos[0], self.side_len)
      if op_y != 3:
        # endpoint[1] = ops[op_y](pos[1], self.side_len * abs(sin(inner_angle)))
        endpoint[1] = ops[op_x](pos[1], self.side_len * abs(sin(angle_count)))
        if op_x == 3:
          endpoint[1] = ops[op_y](pos[1], self.side_len)
      pg.draw.line(self.surface, self.color, pos, endpoint)
      self.vertices.append(pos)
      pos = endpoint[:]
      pg.draw.circle(window, BLUE, (int(pos[0]), int(pos[1])), 5)
      print(angle_count)
      print(inner_angle)
      print(pos)


def stone_of_philosophers(inner_radius):
  side_len = inner_radius + 2 * SQRT_3 * inner_radius
  start_point = [CENTER[0] + side_len / 2, CENTER[1] + inner_radius]
  triangle = Regular_Polygon(window, RED, 3, start_point, side_len)
  pg.draw.circle(window, BLUE, CENTER, inner_radius, 1)
  pg.draw.rect(window, GREEN, (CENTER[0] - inner_radius, CENTER[1] - inner_radius, 
                               inner_radius * 2, inner_radius * 2), 1)
  triangle.draw()
  centroid = (int((triangle.vertices[0][0] + triangle.vertices[1][0] + triangle.vertices[2][0]) / 3), 
              int((triangle.vertices[0][1] + triangle.vertices[1][1] + triangle.vertices[2][1]) / 3))
  a = start_point[0] - centroid[0]
  b = start_point[1] - centroid[1]
  outer_radius = int(sqrt(a ** 2 + b ** 2))
  pg.draw.circle(window, WHITE, centroid, outer_radius, 1)
  pentagon = Regular_Polygon(window, WHITE, 5, [250, 250], 50)
  pentagon.draw()
  

def regs():
  for i in [*range(3, 10)]:
      reg = Regular_Polygon(window, WHITE, i, [250, 250], 100)
      reg.draw()



def main():
  radius = 50
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
