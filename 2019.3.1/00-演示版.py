"""
飞机大战
"""
import sys  # 导入系统模块
import random  # 导入随机数
import pygame
import pygame.locals    # 导入pygame本地策略

#  设计图片常量
IMG_BACKGROUND = "BattleFly/res/img_bg_level_1.jpg"
# 设置敌机图片库常量元组
IMG_ENEMYS = ("BattleFly/res/img-plane_1.png","BattleFly/res/img-plane_2.png","BattleFly/res/img-plane_3.png","BattleFly/res/img-plane_4.png","BattleFly/res/img-plane_5.png","BattleFly/res/img-plane_6.png","BattleFly/res/img-plane_7.png")
IMG_PLAYER = "BattleFly/res/hero2.png"    #  设置玩家飞机图片
IMG_BULLET = "BattleFly/res/bullet_13.png"    #  设置子弹图片
#  创建所有显示的图形父类Model
class Model:
    window = None   #  主窗体对象，用于模型访问使用
    #  构造方法
    def __init__(self,img,x,y):
        self.img = pygame.image.load(img)   #  背景图片
        self.x = x  #  窗体中放置的x坐标
        self.y = y  #  窗体中放置的y坐标
    #  将模型加入窗体的方法抽取到父类
    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    @staticmethod            #  碰撞操作与模型对象无关，属于模型相关操作，定义为静态方法
    def is_hits(rect1,rect2):     #  定义双方是否碰撞的静态方法
        return pygame.Rect.colliderect(rect1, rect2)   #  返回两个矩形是否相交，即是否碰撞
class Background(Model):    #  继承父类
    #  定义背景移动的方法
    def move(self):
        self.y += 1
    #  覆盖父类display方法
    def display(self):
        #  加入判断，如果第一张图片移动距离超出屏幕，回复第一张图片的坐标
        if self.y > Game.WINDOW_HEIGHT:
            self.y = 0
        else:   #  如果没有超出屏幕就贴图
            self.window.blit(self.img, (self.x, self.y))
            self.window.blit(self.img, (self.x, self.y - Game.WINDOW_HEIGHT))   #  将背景图片展示第二遍，坐标位置与第一遍展示上下拼接吻合
class PlayerPlane(Model):    # 继承父类
    #  覆盖init方法
    def __init__(self,img,x,y):
        super().__init__(img,x,y)    #  调用父类构造方法
        self.bullets = []   #  定义子弹列表为空，默认没有子弹
    #  覆盖display方法
    def display(self,enemys):    #  在显示飞机和子弹的同时，传入敌机列表，判断子弹是否与敌机相撞，添加enemys形参
        remove_bullets = [] # 定义被删除的子弹列表
        self.window.blit(self.img, (self.x, self.y))      #  飞机显示复制过来
        for bullet in self.bullets: #  循环子弹
            # 优化子弹存储队列，超出屏幕移除子弹
            if bullet.y < -29 :     # 如果子弹位置超出屏幕
                remove_bullets.append(bullet)  # 将要删除的子弹加入列表
            else:   #  如果子弹位置未超出屏幕范围
                rect1 = pygame.locals.Rect(bullet.x,bullet.y,20,29)    #  创建子弹矩形对象，传入x,y,width,height
                for enemy in enemys :                   #  对未超出屏幕显示范围的子弹与所有敌机进行碰撞检测
                    rect2 = pygame.locals.Rect(enemy.x,enemy.y,100,68)     #  创建敌机矩形对象
                    #  调用碰撞检测方法，传入当前子弹对象，传入敌机对象，判断是否碰撞
                    if Model.is_hits(rect1,rect2):     #  如果碰撞
                        s = pygame.mixer.Sound("BattleFly/res/bomb.wav")  #  添加混音音效文件
                        s.play()    #  播放爆破效果音
                        enemy.is_hited = True           #  设置当前敌机为被击中状态
                        enemy.bomb.show = True          #  设置爆破效果状态开启
                        enemy.bomb.x = enemy.x          #  设置爆破效果开启位置x坐标
                        enemy.bomb.y = enemy.y          #  设置爆破效果开启位置y坐标
                        remove_bullets.append(bullet)   #  将产生碰撞的子弹加入删除列表
                        break                          #  当前子弹击中了一架敌机，终止对剩余敌机的碰撞检测，终止敌机循环

        for bullet in remove_bullets :  # 循环删除子弹列表
            self.bullets.remove(bullet)     # 从原始子弹列表中删除要删除的子弹

        rect1 = pygame.locals.Rect(self.x, self.y, 120, 78)  #  创建玩家矩形对象
        for enemy in enemys :     #  循环敌机列表
            #  调用碰撞检测方法，传入玩家对象，传入敌机对象，判断是否碰撞
            rect2 = pygame.locals.Rect(enemy.x, enemy.y, 100, 68)   #  创建敌机矩形对象
            if Model.is_hits(rect1, rect2):  #   如果碰撞
                #  玩家碰撞位置添加游戏结束音乐
                pygame.mixer.music.load("BattleFly/res/gameover.wav")  #  加载游戏背景音乐文件为游戏结束
                pygame.mixer.music.play(loops=1)  #  播放背景音乐  loops=1 控制播放次数
                enemy.is_hited = True  #  设置当前敌机为被击中状态
                return False    #  设置当前操作返回False
        return  True    #  设置正常操作状态下返回True
class EnemyPlane(Model):    # 继承父类
    # 覆盖init方法
    def __init__(self):
        img = IMG_ENEMYS[random.randint(0,6)]  #  设置图片随机从元组中获取
        x = random.randint(0,Game.WINDOW_WIDTH - 100)  # 设置x坐标随机生成 横向位置 0 到屏幕宽度 到 飞机宽度(100)
        y = random.randint( -Game.WINDOW_HEIGHT, - 68)  # 设置y坐标随机生成 纵向位置 -屏幕高度 到 -飞机高度
        super().__init__(img,x,y)   # 调用父类构造方法
        self.is_hited = False   #  添加敌机被击中的状态
        self.bomb = Bomb()  #  为敌机添加绑定的爆破效果对象
    #   定义敌机移动的方法
    def move(self):
        # 控制敌机到达底部后，返回顶部
        if self.y > Game.WINDOW_HEIGHT or self.is_hited:  #  添加敌机被击中后的处理，更换位置，更换图片    #  敌机超出屏幕
            self.img = pygame.image.load(IMG_ENEMYS[random.randint(0, 6)])  # 修改敌机到达底部后返回的图片随机生成，同初始化策略
            self.x = random.randint(0, Game.WINDOW_WIDTH - 100)    # 修改敌机到达底部后返回顶部的策略，x随机生成，同初始化策略
            self.y = random.randint(-Game.WINDOW_HEIGHT, - 68)    # 修改敌机到达底部后返回顶部的策略，y随机生成，同初始化策略
            self.is_hited = False   #  重置敌机是否被击中状态为False
        else:  #  敌机未超出屏幕
            self.y += 4  #  控制敌机移动速度

    def display(self):  #  覆盖父类显示方法
        super().display()   #  调用父类方法
        #  设置爆破效果的显示策略
        if self.bomb.show == True : #  如果爆破状态开启
            self.bomb.display() #  调用爆破对象的显示方法
class Bullet(Model):    # 继承父类
    #  定义子弹移动的方法
    def move(self):
        self.y -= 12  # 控制子弹移动速度
class Bomb(Model):#  创建爆炸效果类
    def __init__(self): #  定义单独的初始化方法
        self.imgs = [pygame.image.load("BattleFly/res/bomb-" + str(v) + ".png") for v in range(1, 7)]     #  加载爆炸效果使用的所有图片列表
        self.show = False   #  定义是否开启爆破效果属性
        self.times = 0  #  定义爆破图片展示控制变量

    def display(self):  #  定义单独的贴图显示方法
        #  爆破效果展示
        """  控制爆破展示完毕后恢复状态
         if self.show :  #  如果开启爆破效果
         """
        if self.show and self.times < len(self.imgs)*10  :  #  控制爆破展示速度  #  控制爆破展示完毕后恢复状态 #  如果开启爆破效果
            self.window.blit(self.imgs[self.times // 10], (self.x, self.y))  #  控制爆破展示速度 #  修改爆破图片展示每次递增
            self.times += 1 #  控制变量每次+1
        else:   #  控制爆破展示完毕后恢复状态
            self.show = False   #  控制爆破展示完毕后恢复状态
            self.times = 0  #  控制爆破展示完毕后恢复状态

class Game:
    WINDOW_WIDTH = 512  #  设置窗体宽度高度
    WINDOW_HEIGHT = 768 #  设置窗体宽度高度

    #  定义构造方法
    def __init__(self):
        self.game_state = True  #  初始化游戏状态，默认为True
        self.game_begin = False #  TODO 1.初始化游戏启动状态，默认为Flase

    # 主程序，运行游戏入口
    def run(self):
        pygame.init()   #  初始化pygame读取系统操作
        self.frame_init() # 执行窗体初始化

        pygame.mixer.init()                         #  初始化背景音乐模块
        pygame.mixer.music.load("BattleFly/res/bg.wav")      #  加载背景音乐文件
        pygame.mixer.music.play()                   #  播放背景音乐

        self.model_init() #  执行元素初始化
        while True: #  反复刷新窗体，使窗体保持在屏幕上
            self.background.display()   #  反复刷新背景
            self.background.move()  #  调用背景移动操作，反复执行，构造背景向下的画面

            # TODO 2.游戏未启动时显示游戏选择界面，贴文字信息；游戏启动后正常游戏，显示游戏贴图。
            if self.game_begin == False:    # TODO 3.未启动游戏
                font_over = pygame.font.Font("BattleFly/res/DENGB.TTF", 40)   # TODO 5.设置大字体
                text_over = font_over.render("飞机大战", 1, (255, 255, 0))  # TODO 5.设置文字
                self.window.blit(text_over, pygame.locals.Rect(256 - 80, 200, 226, 43))   # TODO 5.设置显示位置

                font_over = pygame.font.Font("BattleFly/res/DENGB.TTF", 18)   # TODO 6.设置小字体
                text_over = font_over.render("请选择难度", 1, (255, 255, 255))
                self.window.blit(text_over, pygame.locals.Rect(256 - 45, 300, 226, 43))

                font_over = pygame.font.Font("BattleFly/res/DENGB.TTF", 30)   # TODO 7.设置中字体
                text_over = font_over.render("1-简单", 1, (0, 255, 0))
                self.window.blit(text_over, pygame.locals.Rect(256 - 46, 340, 226, 43))

                text_over = font_over.render("2-普通", 1, (255, 255, 255))
                self.window.blit(text_over, pygame.locals.Rect(256 - 46, 390, 226, 43))

                text_over = font_over.render("3-别开玩笑", 1, (255, 0, 0))
                self.window.blit(text_over, pygame.locals.Rect(256 - 152 / 2, 440, 226, 43))
            else:   # TODO 4.启动游戏
                for enemy in self.enemys :   #   加入所有敌机
                    enemy.display()     #   显示每驾敌机
                    enemy.move()        #   每驾敌机移动

                #  对游戏状态进行判定
                if self.game_state :    #  如果游戏状态为游戏中，显示玩家飞机
                    self.game_state = self.player.display(self.enemys)  # 接收到游戏状态，备用  #  飞机加入时，传入敌机列表实参self.enemys   #  加入玩家飞机
                else:   #  如果游戏状态为结束
                    font_over = pygame.font.Font("BattleFly/res/DENGB.TTF", 40)   #  创建字体对象
                    text_over = font_over.render("GAME OVER", 1, (255, 0, 0))   #  创建文本对象
                    self.window.blit(text_over, pygame.locals.Rect(143, 300, 226, 43))  #  添加文本对象到屏幕上

                for bullet in self.player.bullets:  #  循环子弹
                    bullet.display()    #  加入子弹
                    bullet.move()       # 调用子弹移动操作

            pygame.display.update() #  刷新窗体
            self.event_init() # 反复监控是否存在事件执行

    #  初始化窗体
    def frame_init(self):
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))  #  初始化窗体
        Model.window = self.window  # 将窗口对象传入模型类中
        image = pygame.image.load("BattleFly/res/app.ico")    #  加载图标文件为图片对象
        pygame.display.set_icon(image)  #  设置窗体图标为图片
        pygame.display.set_caption("plane battle")  #  设置窗体的标题

    #  初始化窗体中的元素
    def model_init(self):
        self.background = Background(IMG_BACKGROUND,0,0)    #  初始化背景对象，放置在0,0位
        self.enemys = []     #  定义敌机列表，保存多驾敌机
        """ TODO 删除敌机初始化操作
        for _ in range(5):  #  循环产生5架敌机
            self.enemys.append(EnemyPlane())     # 修改创建敌机操作
        """
        self.player = PlayerPlane(IMG_PLAYER, 200, 500)  #  初始化窗体对象，放置在200,500位

    #  初始化事件
    def event_init(self):
        for event in pygame.event.get():    # 获取所有的事件
            if event.type == pygame.locals.QUIT:      # 判断是不是点击的关闭按钮
                sys.exit()              # 系统退出

            if event.type == pygame.locals.MOUSEMOTION and self.game_state:  #  添加玩家移动控制判定条件   #  设置监听鼠标移动事件
                pos = pygame.mouse.get_pos()  # 获取鼠标位置
                self.player.x = pos[0] - 60  # 设置飞机中心位置在鼠标位置(x)  横坐标 - 飞机宽度1半
                self.player.y = pos[1] - 39  # 设置飞机中心位置在鼠标位置(y)  纵坐标 - 飞机高度1半


            if event.type == pygame.locals.KEYDOWN :            # TODO 8.添加键盘按键监听事件
                print("-----------------"+str(event.key))

                if self.game_begin:                             # TODO 9.当游戏开始时，接收难度调整
                    if event.key == 61:                         # TODO 13.如果按键是自定义按键
                        self.enemys.append(EnemyPlane())        # TODO 14.添加敌人
                    elif event.key == 45:
                        self.enemys.pop()                       # TODO 15.减少敌人
                    elif event.key == 27:  # TODO 10.如果按键是ESC
                        sys.exit()
                    elif event.key == 13:  # TODO 10.如果按键是ENTER
                        self.game_begin = False
                        self.run()
                else:                                           # TODO 9.当游戏未开始时，接收难度选择，并开始游戏
                    if event.key == pygame.locals.K_1:          # TODO 10.如果按键是1
                        for _ in range(5):                      # TODO 11.循环添加5驾飞机
                            self.enemys.append(EnemyPlane())
                        self.game_begin = True                  # TODO 12.设置游戏为开始状态
                    elif event.key == pygame.locals.K_2:        # TODO 10.如果按键是2
                        for _ in range(30):
                            self.enemys.append(EnemyPlane())
                        self.game_begin = True
                    elif event.key == pygame.locals.K_3:        # TODO 10.如果按键是3
                        for _ in range(300):
                            self.enemys.append(EnemyPlane())
                        self.game_begin = True

        if self.game_state:  #  添加发射子弹的控制判断
            press_mouse = pygame.mouse.get_pressed()  # 获取鼠标按键压下事件，返回得到元组，保存鼠标左中右键按下状态（1,0,0）
            if press_mouse[0] == 1:  # 判断左键是否按下
                pos = pygame.mouse.get_pos()  # 获取鼠标位置
                bullet = Bullet(IMG_BULLET, pos[0] - 10,
                                pos[1] - 39 - 29)  # 创建子弹，横坐标为鼠标x坐标 - 子弹宽度1半，纵坐标为鼠标y坐标 - 飞机高度1版 - 子弹高度
                self.player.bullets.append(bullet)  # 加入飞机子弹列表


if __name__ == "__main__":
    Game().run()

