import pygame as pg
import random as rand

pg.init()
window_w = 500
window_h = window_w  # The window of this drawing is a square
window = pg.display.set_mode((window_w, window_h))
pg.display.flip()


def redraw():  # Redraw if space is pressed
    keys = pg.key.get_pressed()
    for key in keys:
        if key == pg.K_SPACE:
            window.fill(0, 0, 0)
            return True
        else:
            return False


def get_points():  # Define a random set of points within a set range
    points = []
    point_cnt = 10
    # draw_rng = int(window_w / 1.618)  # Set an outer boundary for drawing
    draw_rng = window_w
    for _ in [*range(0, point_cnt)]:
        points.append([rand.randrange(0, draw_rng, 10), rand.randrange(0, draw_rng, 30)])
    return points


def draw():
    points = get_points()
    points_1 = [x for x in points if x != points[0]]
    for start_point in points:
        for end_point in points_1:
            pg.draw.line(window, (0, 0, 255), start_point, end_point)
            pg.time.delay(10)
            pg.display.update()


def main():
    drawn = 0
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        if not drawn:
            draw()
            drawn = 1
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            window.fill((0, 0, 0))
            drawn = 0


if __name__ == "__main__":
    main()
