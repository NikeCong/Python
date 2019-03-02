import sys

import pygame
import pygame.locals


IMG_BACKGROUND = "BattleFly/res/img_bg_level_1.jpg"
APP_ICON = "BattleFly/res/app.ico"



class Model:
    window = None
    def __init__(self,background_path,x,y):
        self.img = pygame.image.load(background_path)
        self.x = x
        self.y = y

    def display(self, x, y):
        self.window.blit(self.img, (x, y))



class BackGround(Model):
    #  定义背景移动的方法
    def move(self):
        self.y += 1

    def display(self):
        #  加入判断，如果第一张图片移动距离超出屏幕，回复第一张图片的坐标
        if self.y > Game.WINDOW_HEIGHT:
            self.y = 0
        else:  # 如果没有超出屏幕就贴图
            super(BackGround,self).display(self.x,self.y)
            super(BackGround, self).display(self.x, self.y - Game.WINDOW_HEIGHT)  # 将背景图片展示第二遍，坐标位置与第一遍展示上下拼接吻合

class PlayerPlane(Model):
    pass

class Bullet():
    pass

class EnemyPlane():
    pass

class Bomb():
    pass

class Game:
    WINDOW_WIDTH = 512
    WINDOW_HEIGHT = 768

    def model_init(self):
        self.background = BackGround(IMG_BACKGROUND, 0, 0)  # 初始化背景对象，放置在0,0位
        Model.window.blit(self.background.img, (self.background.x, self.background.y))

    def frame_init(self):
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))  # 初始化窗体
        Model.window = self.window  # 将窗口对象传入模型类中
        img = pygame.image.load(APP_ICON)
        pygame.display.set_icon(img)
        pygame.display.set_caption("飞机大战小游戏")

    def run(self):
        self.frame_init()
        self.model_init()
        while True:
            self.background.move()
            self.background.display()
            pygame.display.update()
            self.event_init()



        #  初始化窗体中的元素


    def event_init(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                sys.exit()



def main():
    Game().run()

if __name__ == "__main__":
    main()
