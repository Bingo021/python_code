"""
坦克大战游戏的需求
1.项目中有哪些类？
2.每个类中有哪些方法？
"""
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)
"""新增功能：加载主窗口"""


# 主类
class MainGame():
    window = None

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置窗口的标题
        pygame.display.set_caption("坦克大战1.0")
        while True:
            # 给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            MainGame.window.blit(self.getTextSuface('敌方坦克剩余数量%d'%6),(10,10))
            pygame.display.update()

    # 结束游戏
    def endGame(self):
        print("谢谢，欢迎再次游戏")
        exit()

    # 左上角文字绘制
    def getTextSuface(self,text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有的字体名称
        print(pygame.font.get_fonts())
        # 获取字体Font对象
        font = pygame.font.SysFont('kaiti', 18)
        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        for event in eventList:
            # 判断按下的键是关闭还是键盘按下
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("按下左键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:
                    print("按下右键，坦克向右移动")
                elif event.key == pygame.K_UP:
                    print("按下上键，坦克向上移动")
                elif event.key == pygame.K_DOWN:
                    print("按下下键，坦克向下移动")


# 坦克类
class Tank():
    def __init__(self):
        pass

    # 射击
    def shot(self):
        pass

    # 移动
    def move(self):
        pass

    # 显示坦克的方法
    def displayTank(self):
        pass


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass


# 子弹类
class Bullet():
    def __init__(self):
        pass

    # 移动
    def move(self):
        pass

    # 显示子弹的方法
    def displayBullet(self):
        pass


# 墙壁类
class Wall():
    def __init__(self):
        pass

    # 显示墙壁的方法
    def displayWall(self):
        pass
    # 属性：是否可以通过


# 爆炸效果类
class Explode():
    def __init__(self):
        pass

    # 展示爆炸效果
    def displayExplode(self):
        pass


# 音效类
class Music():
    def __init__(self):
        pass

    # 播放音乐
    def play(self):
        pass


if __name__ == '__main__':
    MainGame().startGame()
