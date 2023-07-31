import pygame as pg

y, step = 15, 16
head, segments = 17, [15, 16, 17]
n, apple = step, 99

# Ensure that n is non-zero to avoid ZeroDivisionError
if n == 0:
    n = 1

screen_size = [225] * 2
screen = pg.display.set_mode(screen_size, pg.SCALED)

running = True

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        elif e.type == pg.KEYDOWN:
            step = (e.key % 4 + 17 + 15) % 49 - n

    segments = segments[apple:] + [head + step]
    screen.fill('black')

    if apple == head:
        apple = segments[0]

    for i, v in enumerate([apple] + segments):
        pg.draw.rect(screen, 'green' if i else 'red',
                     ((v - 1) % n * y, (v - n) // n * y, y, y))

    pg.display.flip()

    head += step

    pg.time.wait(200)

pg.quit()
