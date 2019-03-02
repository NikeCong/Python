import sys
import time

import pygame
from pygame import locals

BACKGROUND_IMG = "BattleFly/res/img_bg_level_1.jpg"
PLAYERPLANE_IMG = "BattleFly/res/hero.png"
APP_ICON = "BattleFly/res/app.ico"
BULLET_IMG = "BattleFly/res/bullet_11.png"

class BackGround:
    window = None
    def __init__(self,x,y):
        self.img = pygame.image.load(BACKGROUND_IMG)
        self.x = x
        self.y = y

    def display(self):
        self.y += 1
        if self.y > Game.WINDOW_HEIGHT:
            self.y = 0
        else:
            BackGround.window.blit(self.img, (self.x, self.y))
            BackGround.window.blit(self.img, (self.x, self.y - Game.WINDOW_HEIGHT))


class Game:
    WINDOW_WIDTH = 512
    WINDOW_HEIGHT = 768

    def run(self):
        self.frame_init()
        while True:
            self.back_ground.display()
            self.heroplane.display()
            pygame.display.update()
            self.event_test()

    def frame_init(self):
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
        app_icon = pygame.image.load(APP_ICON)
        pygame.display.set_icon(app_icon)
        pygame.display.set_caption("飞机大战")

        BackGround.window = self.window
        self.back_ground = BackGround(0,0)

        self.heroplane = PlayerPlane()



    def event_test(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                sys.exit()


class PlayerPlane:

    def __init__(self):
        self.img = pygame.image.load(PLAYERPLANE_IMG)
        self.x = 220
        self.y = 700
        BackGround.window.blit(self.img, (self.x, self.y))

    def display(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        print(pygame.mouse.get_pos())
        if pos_x > 466:
            pos_x = 466

        if pos_x <= 45:
            pos_x = 45

        if pos_y > 740:
            pos_y = 740

        if pos_y <= 38:
            pos_y = 38

        BackGround.window.blit(self.img, (pos_x-50, pos_y-40))
        mouse_state = pygame.mouse.get_pressed()
        bullet = Bullet()
        if mouse_state[0] == 1:
            bullet.display(pos_x-9, pos_y-70)


class EnemyPlane:
    pass

class Bullet:
    def __init__(self):
        self.img = pygame.image.load(BULLET_IMG)


    def display(self,x,y):
        BackGround.window.blit(self.img, (x, y))

def main():
    Game().run()

if __name__ =="__main__":
    main()
