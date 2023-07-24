"""
坦克大战游戏的需求
1.项目中有哪些类？
2.每个类中有哪些方法？
"""
import pygame, time, random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)
"""新增功能：加载主窗口"""


# 主类
class MainGame():
    window = None
    my_tank = None
    # 定义敌方坦克的列表
    enemyTankList = []
    # 定义敌方坦克的数量
    enemyTankCount = 5

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 初始化我方坦克
        MainGame.my_tank = Tank(350, 250)
        # 初始化敌方坦克，并将敌方坦克添加到列表中
        self.createEnemyTank()
        # 设置窗口的标题
        pygame.display.set_caption("坦克大战1.0")
        while True:
            # 使坦克的移动速度变慢点
            time.sleep(0.02)
            # 给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            MainGame.window.blit(self.getTextSuface('敌方坦克剩余数量%d' % len(MainGame.enemyTankList)), (10, 10))
            # 调用显示坦克的方法
            MainGame.my_tank.displayTank()
            # 循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            # 如果坦克的开关开启，才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            pygame.display.update()

    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            enemyTank.displayTank()
            enemyTank.randMove()

    # 结束游戏
    def endGame(self):
        print("谢谢，欢迎再次游戏")
        exit()

    # 左上角文字绘制
    def getTextSuface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有的字体名称
        # print(pygame.font.get_fonts())
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
                    # 切换方向
                    MainGame.my_tank.direction = 'L'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print("按下左键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:
                    MainGame.my_tank.direction = 'R'
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print("按下右键，坦克向右移动")
                elif event.key == pygame.K_UP:
                    MainGame.my_tank.direction = 'U'
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print("按下上键，坦克向上移动")
                elif event.key == pygame.K_DOWN:
                    MainGame.my_tank.direction = 'D'
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print("按下下键，坦克向下移动")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
            # 松开方向键停止，修改坦克的开关
            if event.type == pygame.KEYUP:
                # 判断松开的键是上、下、左、右时候才停止坦克移动
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    MainGame.my_tank.stop = True

    # 初始化敌方坦克，并将敌方坦克添加到列表中
    def createEnemyTank(self):
        top = 100
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0, 600)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)


# 坦克类
class Tank():
    # 添加距离左边left，距离上边top
    def __init__(self, left, top):
        # 保存加载图片
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif'),
        }
        # 方向
        self.direction = 'U'
        # 根据当前方向获取图片
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = 1
        # 坦克移动的开关
        self.stop = True

    # 射击
    def shot(self):
        pass

    # 移动
    def move(self):
        # 判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left < SCREEN_WIDTH - self.rect.height:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top < SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed

    # 显示坦克的方法
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        # 加载图片集
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif'),
        }
        # 方向
        self.direction = self.randDirection()
        # 根据方向获得图片
        self.image = self.images[self.direction]
        # 区域
        self.rect = self.image.get_rect()
        # 对left和right赋值
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = speed
        # 移动
        self.flag = True
        # 新增加一个步数变量
        self.step = 20

    # 随机生成敌方坦克的方向
    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    # 敌方坦克随机移动方法
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            # 让步数复位
            self.step = 60
        else:
            self.move()
            # 步数递减
            self.step -= 1


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
