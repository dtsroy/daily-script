import pygame
from fireworks import Fireworks

g_fireworks = None  # 烟花主类


def init():
    global g_fireworks
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.mouse.set_visible(1)
    pygame.display.set_caption("烟花")
    g_fireworks = Fireworks(screen)


clock = pygame.time.Clock()


def loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        else:
            g_fireworks.run(event)
    clock.tick(24)
    pygame.display.update()
