import pygame
import sys


# 02-窗体初始化  ========================================================

# 1.创建窗体对象
pygame.display.set_mode((width,height))
# 参数：元组，包含窗体的宽，高
# 返回值：窗体对象

# 2.刷新界面显示窗体，该操作需要反复执行，否则屏幕上无法观察到动态刷新出的变化效果
pygame.display.update()



# 03-窗体设置   ========================================================

# 3.加载图标文件为图片对象
pygame.image.load("图片路径")
# 参数：字符串，对应的图片路径
# 返回值：图片对象

# 4.设置窗体图标
pygame.display.set_icon(image)
# 参数：图片对象

# 5.设置窗体的标题文本
pygame.display.set_caption("plane battle")
# 参数：字符串，窗体显示的文字



# 04-关闭窗体(事件)   ========================================================

# 6.获取pygame界面的所有事件
pygame.event.get()
# 返回值：事件列表

# 7.获取事件类别
event.type
# QUIT             none
# ACTIVEEVENT      gain, state
# KEYDOWN          unicode, key, mod
# KEYUP            key, mod
# MOUSEMOTION      pos, rel, buttons
# MOUSEBUTTONUP    pos, button
# MOUSEBUTTONDOWN  pos, button
# JOYAXISMOTION    joy, axis, value
# JOYBALLMOTION    joy, ball, rel
# JOYHATMOTION     joy, hat, value
# JOYBUTTONUP      joy, button
# JOYBUTTONDOWN    joy, button
# VIDEORESIZE      size, w, h
# VIDEOEXPOSE      none
# USEREVENT        code

# 8.导入pygame本地设置的资源，包含程序执行过程中所使用的各种常量，例如键盘按钮，鼠标按钮等
import pygame.locals

# 9.窗体按钮X
pygame.locals.QUIT

# 10.退出系统
sys.exit()



# 05-背景制作   ========================================================

# 11.添加要显示的对象到窗体中显示
window.blit(img, (x, y))
# 参数1：可显示的对象，对象可以是图片，可以是文本信息
# 参数2：元组，包含显示的位置x与y坐标



# 12-玩家飞机移动控制（鼠标移动）   ========================================================

# 12.鼠标移动事件
pygame.locals.MOUSEMOTION

# 13.获取鼠标位置
pygame.mouse.get_pos()
# 返回值：元组，包含位置x与y坐标



# 13-玩家发射子弹（鼠标左键按住事件）   ========================================================

# 14.获取鼠标按键按住状态
pygame.mouse.get_pressed()
# 返回值：列表，包含左中右键盘是否被按下，0 - 未按下，1 - 按下



# 15-碰撞检测（子弹与敌机）   ========================================================

# 15.创建矩形对象
pygame.locals.Rect(x,y,w,h)
# 参数1：整数，x坐标
# 参数2：整数，y坐标
# 参数3：整数，宽度
# 参数4：整数，高度
# 返回值：矩形对象

# 16.判断两个矩形是否相交
pygame.Rect.colliderect(rect1, rect2)
# 参数1：矩形对象，矩形1
# 参数2：矩形对象，矩形2
# 返回值：布尔值，矩形是否相交



# 18-游戏结束信息展示   ========================================================

# 17.创建字体对象
pygame.font.Font(font_name, size)
# 参数1：字符串，字体文件对应的路径
# 参数2：整数，字号大小
# 返回值：字体对象

# 18.创建可显示的文本对象
font_over.render("显示文字", 抗锯齿度, (r, g, b))
# 参数1：字符串，要显示的文字信息
# 参数2：整数，抗锯齿度，加强平滑度，推荐使用1
# 参数3：元组，字体颜色，包含RGB三色值
# 返回值：可显示的文本对象

# 19.加载文本对象到屏幕
self.window.blit(text_obj, rect)
# 参数1：文本对象
# 参数2：矩形，显示的位置和大小区域

# 20.初始化pygame可以读取系统模块
pygame.init()

# 19-声音效果处理   ========================================================

# 21.初始化声音模块
pygame.mixer.init()

# 22.加载背景音乐文件
pygame.mixer.music.load("文件路径")
#参数：字符串，声音文件路径

# 23.播放背景音乐
pygame.mixer.music.play()

# 24.创建音效对象
sound = pygame.mixer.Sound("文件路径")
#参数：字符串，声音文件路径
#返回值：声音文件对象

# 25.播放音效
sound.play()
