"""
坦克大战游戏的需求
1.项目中有哪些类？
2.每个类中有哪些方法？
"""
import pygame, time, random
from pygame.sprite import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


# 定义一个基类
class BaseItem(Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


# 主类
class MainGame():
    window = None
    my_tank = None
    # 定义敌方坦克的列表
    enemyTankList = []
    # 定义敌方坦克的数量
    enemyTankCount = 5
    # 存储我方子弹的列表
    myBulletList = []
    # 存储敌方子弹的列表
    enemyBulletList = []
    #存储爆炸效果的列表
    explodeList = []
    #存储墙壁的列表
    wallList = []
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
        self.createMytank()
        # 初始化敌方坦克，并将敌方坦克添加到列表中
        self.createEnemyTank()
        #初始化墙壁
        self.createWall()
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
            #判断我方坦克是否存活
            if MainGame.my_tank and MainGame.my_tank.live:
                # 调用显示坦克的方法
                MainGame.my_tank.displayTank()
            else:#删除我方坦克
                del MainGame.my_tank
                MainGame.my_tank=None
            # 循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            # 循环遍历显示我方坦克的子弹
            self.blitMyBullet()
            # 循环遍历显示敌方坦克的子弹
            self.blitEnemyBullet()
            #循环遍历爆炸列表，展示爆炸效果
            self.blitExplode()
            #循环遍历墙壁列表，来展示墙壁
            self.blitWall()
            # 如果坦克的开关开启，才可以移动
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
                    #检测我方坦克是否与墙壁发生碰撞
                    MainGame.my_tank.hitWall()
                    #检测我方坦克是否与敌方坦克发生碰撞
                    MainGame.my_tank.myTank_hit_enemyTank()
            pygame.display.update()

    #遍历墙壁列表展示墙壁
    def blitWall(self):
        for wall in MainGame.wallList:
            #判断墙壁是否存活
            if wall.live:
                #调用墙壁的显示方法
                wall.displayWall()
            else:
                #从墙壁列表移除
                MainGame.wallList.remove(wall)

    #初始化墙壁
    def createWall(self):
        for i in range(6):
            wall = Wall(i*130,220)
            #将墙壁添加到列表中
            MainGame.wallList.append(wall)

    def createMytank(self):
        MainGame.my_tank = MyTank(350, 300)
        #创建Music类对象
        music = Music('img/start.wav')
        #播放音乐
        music.play()

    #循环展示爆炸效果
    def blitExplode(self):
        for explode in MainGame.explodeList:
            #判断是否活着
            if explode.live:
                #展示
                explode.displayExplode()
            else:
                #在爆炸列表中移除
                MainGame.explodeList.remove(explode)

    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            # 先判断当前敌方坦克是否活着
            if enemyTank.live:
                enemyTank.displayTank()
                enemyTank.randMove()
                #调用检测是否与墙壁发生碰撞
                enemyTank.hitWall()
                if MainGame.my_tank and MainGame.my_tank.live:
                    #检测敌方坦克是否与我方坦克碰撞
                    enemyTank.enemyTank_hit_myTank()
                # 发射子弹
                enemyBullet = enemyTank.shot()
                if enemyBullet:
                    # 将敌方子弹存储到敌方子弹的列表中
                    MainGame.enemyBulletList.append(enemyBullet)
            else:  # 不活着，从敌方坦克列表移除
                MainGame.enemyTankList.remove(enemyTank)

    # 循环遍历我方子弹列表
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            # 判断当前子弹是否活着，如果是则进行显示及移动
            if myBullet.live:
                myBullet.displayBullet()
                # 调用子弹的移动方法
                myBullet.move()
                #调用检测我方子弹是否与敌方坦克发生碰撞
                myBullet.myBullet_hit_enemyTank()
                # 检测我方子弹是否与墙壁碰撞
                myBullet.hitWall()
            # 否则删除
            else:
                MainGame.myBulletList.remove(myBullet)

    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            # 判断当前子弹是否活着，如果是则进行显示及移动
            if enemyBullet.live:
                enemyBullet.displayBullet()
                # 调用子弹的移动方法
                enemyBullet.move()
                #调用敌方子弹与我方坦克碰撞的方法
                enemyBullet.enemyBullet_hit_myTank()
                #检测敌方子弹是否与墙壁碰撞
                enemyBullet.hitWall()
            # 否则删除
            else:
                MainGame.enemyBulletList.remove(enemyBullet)

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
                #当坦克不存走或者死亡
                if not MainGame.my_tank:
                    #判断按下的是Esc键，让坦克重生
                    if event.key == pygame.K_ESCAPE:
                        #让我方坦克重生及带调用创建坦克的方法
                        self.createMytank()
                if MainGame.my_tank and MainGame.my_tank.live:
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
                        # 如果当前我方子弹列表大小，小于等于3的时候才可以创建
                        if len(MainGame.myBulletList) < 3:
                            # 创建我方坦克发射子弹
                            myBullet = Bullet(MainGame.my_tank)
                            MainGame.myBulletList.append(myBullet)
                            #我方坦克发射子弹添加音效
                            music =Music('img/hit.wav')
                            music.play()

            # 松开方向键停止，修改坦克的开关
            if event.type == pygame.KEYUP:
                if MainGame.my_tank and MainGame.my_tank.live:
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
class Tank(BaseItem):
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
        # 坦克是否活着
        self.live = True
        #新增属性原来坐标
        self.oldLeft=self.rect.left
        self.oldTop=self.rect.top

    # 射击
    def shot(self):
        return Bullet(self)

    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    #检测坦克是否与墙壁发生碰撞
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self,wall):
                #将坐标设置为移动之前的坐标
                self.stay()

    # 移动
    def move(self):
        #移动后记录原始的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
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
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)

    def myTank_hit_enemyTank(self):
        #循环遍历敌方坦克列表
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(self,enemyTank):
                self.stay()

# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        # 调用父类的初始化方法
        super(EnemyTank, self).__init__(left, top)
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

    #敌方坦克与我方坦克是否发生碰撞
    def enemyTank_hit_myTank(self):
        if pygame.sprite.collide_rect(self,MainGame.my_tank):
            self.stay()

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

    # 重写shot（）方法
    def shot(self):
        # 随机生成100以内的数
        num = random.randint(1, 100)
        if num < 10:
            return Bullet(self)


# 子弹类
class Bullet(BaseItem):
    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load('img/enemymissile.gif')
        # 坦克的方向决定子弹的方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹的left和top与方向有关
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.height
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.height / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.height
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.height / 2
        # 子弹的速度
        self.speed = 6
        # 子弹的状态，是否碰到墙壁，如果碰到墙壁，修改状态
        self.live = True

    # 移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 碰墙改变状态
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False

    #子弹是否碰撞到墙壁
    def hitWall(self):
        #循环遍历墙壁列表
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self,wall):
                #修改子弹的生存状态，让子弹消失
                self.live=False
                wall.hp-=1
                if wall.hp<=0:
                    #修改墙壁的生存状态
                    wall.live=False

    # 显示子弹的方法
    def displayBullet(self):
        # 将图片surface加载到窗口
        MainGame.window.blit(self.image, self.rect)

    # 我方子弹与敌方坦克的碰撞
    def myBullet_hit_enemyTank(self):
        # 循环遍历敌方坦克列表，判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                # 修改敌方坦克和我方子弹状态
                enemyTank.live = False
                self.live = False
                #创建爆炸对象
                explode=Explode(enemyTank)
                #将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)

    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                #产生爆炸对象
                explode= Explode(MainGame.my_tank)
                #将爆炸对象添加到爆炸对象列表里
                MainGame.explodeList.append(explode)
                #修改敌方子弹与我方坦克的状态
                self.live=False
                MainGame.my_tank.live=False

# 墙壁类
class Wall():
    def __init__(self,left,top):
        #加载墙壁图片
        self.image = pygame.image.load('img/steels.gif')
        #获取墙壁的区域
        self.rect = self.image.get_rect()
        #设置位置
        self.rect.left=left
        self.rect.top=top
        #是否存活
        self.live=True
        #设置生命值
        self.hp=3
    # 显示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)
    # 属性：是否可以通过


# 爆炸效果类
class Explode():
    def __init__(self,tank):
        #爆炸的位置由当前子弹打中的坦克位置决定
        self.rect=tank.rect
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif')
        ]
        self.step = 0
        self.image=self.images[self.step]
        #是否活着
        self.live=True
    # 展示爆炸效果
    def displayExplode(self):
        if self.step<len(self.images):
            #根据索引获取爆炸对象
            self.image=self.images[self.step]
            self.step+=1
            # 添加到主窗口
            MainGame.window.blit(self.image,self.rect)
        else:
        #修改活着的状态
            self.live=False
            self.step=0

# 音效类
class Music():
    def __init__(self,filename):
        self.filename = filename
        #初始化音乐混合器
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(self.filename)

    # 播放音乐
    def play(self):
        pygame.mixer.music.play()


if __name__ == '__main__':
    MainGame().startGame()
