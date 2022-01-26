import math
import pygame
from random import randint
from math import sin, cos, radians, tan


class Point:
    def __init__(self, idx, pos, screen, color) -> None:
        self.rad = radians(idx*6)
        self.x = pos[0]
        self.y = pos[1]
        self.t = 0
        self.screen = screen
        self.color = color
        self.v0 = 2  # 初速度
        self.limit = 51

    def get_pos(self) -> list:
        self.t += 1
        self.x += self.v0 * cos(self.rad)
        self.y -= self.v0 * sin(self.rad) - 0.08 * self.t
        return [self.x, self.y]

    def draw(self) -> None:
        if self.t >= 31:
            self.limit = randint(35, 50)
        if self.limit < self.t:
            return
        pygame.draw.circle(self.screen, self.color, self.get_pos(), 2)


class Fireworks:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.pos = [-1, -1]
        self.can_fire = True  # 一次只能发射一个烟花,免得出问题,刷新图层盖住就不好了

    def run(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.can_fire:
                return
            self.pos = pygame.mouse.get_pos()
            self.fire_to()

    def fire_to(self) -> None:
        self.can_fire = False

        color = (randint(0, 255), randint(0, 255), randint(0, 255))

        try:
            k = (600 - self.pos[1]) / (self.pos[0] - 400)
        except ZeroDivisionError:
            # x==400!
            pass
        tmp_x, tmp_y = 400, 600
        if self.pos[0] > 400:
            dX = 0.5
            dY = - dX * k
        elif self.pos[0] == 400:
            dX = 0
            dY = -0.5
        else:
            dX = -0.5
            dY = - dX * k
        v0 = 1  # 目标速度,根据dX与dY求解dX'和dY'
        # 斜方向速度
        dV = math.sqrt(dX**2 + dY**2)
        # 相似成比例求解
        dX *= v0 / dV
        dY *= v0 / dV
        while round(tmp_y) != self.pos[1]:
            tmp_x += dX
            tmp_y += dY
            self.screen.fill((0, 0, 0))
            pygame.draw.circle(self.screen, color, [tmp_x, tmp_y], 2)
            pygame.display.update()

        # 到达位置,炸开!
        self.bomb(color)

        self.can_fire = True

    def bomb(self, color) -> None:
        self.screen.fill((0, 0, 0))
        pygame.display.update()
        ps = []
        for i in range(60):
            ps.append(Point(i, self.pos, self.screen, color))
        for j in range(100):
            print(".")  # 减缓爆炸
            self.screen.fill((0, 0, 0))
            for point in ps:
                point.draw()
                print(".")  # 经测试,还是太快了
            pygame.display.update()
        self.screen.fill((0, 0, 0))
