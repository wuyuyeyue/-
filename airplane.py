import pygame
# from pygame.locals import *
import random
import time
'''面对对象编程： 实现飞机的显示，并且可以控制飞机的移动'''
# 创建玩家类
class Player(object):
    def __init__(self,screen):# 主窗口对象要传递过来，因为要展示所以必须有screen
        '''

        :param screen: 主窗体对象
        '''
        # 定位
        self.x=150
        self.y=450
        # 设置要显示内容的窗口
        self.screen=screen
        # 生成飞机图片对象
        self.imageName='./demo/ji.jpg'
        self.image=pygame.image.load(self.imageName)
        self.bulletList=[]
    def moveleft(self):
        '''
        左移动
        :return:
        '''
        if self.x>0:
            self.x-=10
        pass
    def moveright(self):
        '''
        右移动
        :return:
        '''
        if self.x<355:
            self.x+=10
        pass
    def moveup(self):
        '''
        上移动
        :return:
        '''
        if self.y>0:
            self.y-=10
        pass
    def movedown(self):
        '''
        下移动
        :return:
        '''
        if self.y<455:
            self.y+=10
        pass
    def display(self):
        '''
        在主窗口中显示
        :return: 
        '''
        self.screen.blit(self.image,(self.x,self.y))
        #完善子弹的展示逻辑

        needDelItemlist=[]
        for item in self.bulletList:
            if item.judge():
                #needDelItemlist.append(item)
                self.bulletList.remove(item)




        # for i in needDelItemlist:
        #     self.bulletList.remove(i)
        #     pass
        for bullet in self.bulletList:
            bullet.display() # 显示子弹位置
            bullet.move() # 让子弹移动，下次显示子弹修改后的位置
            pass
    # 发射子弹
    def fire(self):
        # 创建一个新的子弹对象
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)


    pass


# 创建玩家子弹类
class Bullet(object):
    def __init__(self,x,y,screen):# 主窗口对象要传递过来，因为要展示所以必须有screen
        '''
        :param x:
        :param y:
        :param screen:
        '''
        self.x=x+13
        self.y=y-20
        self.screen=screen
        self.imageName='./demo/qiu.png'
        self.image=pygame.image.load(self.imageName)
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y-=0.2  # 子弹移动速度
        pass
    def judge(self):
        '''
        判断子弹是否到达边界
        :return:
        '''
        if self.y<0:
            return True
        else:
            return False

# 创建敌人类
class Enemy(): # 继承的话只是继承了上面的类方法，并不能继承self
    def __init__(self,screen): # 主窗口对象要传递过来，因为要展示所以必须有screen
        # 设置一个默认初始移动方向
        self.direction='right'
        # 定位
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机图片对象
        self.imageName = './demo/muji.png'
        self.image = pygame.image.load(self.imageName)
        self.bulletList = []
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for item in self.bulletList:
            if item.judge():
                self.bulletList.remove(item)
        for bullet in self.bulletList:
            bullet.display() # 显示子弹位置
            bullet.move() # 让子弹移动，下次显示看到子弹修改后的位置

    def fire(self):
        '''
        敌机发射,导入随机数据
        :return:
        '''
        num=random.randint(1,500) # 创建随机数，如果是这个数则发射子弹
        if num==100:

            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(newBullet)
        pass
    def move(self):
        if self.direction == 'right':
            self.x += 0.2
        elif self.direction == 'left':
            self.x -= 0.2
        if self.x >350:
            self.direction = 'left'
        elif self.x < 10:
            self.direction = 'right'
            pass
# 创建敌人子弹
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x = x + 13
        self.y = y - 20
        self.screen = screen
        self.imageName = './demo/dan.jpg'
        self.image = pygame.image.load(self.imageName)


    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y += 0.1  # 子弹移动速度
    def judge(self):
        '''
        判断子弹是否到达边界
        :return:
        '''
        if self.y > 500:
            return True
        else:
            return False


# 定义控制函数

def key_control(plyobj):
    '''
    定义普通函数 用来实现键盘检测
    :param plyobj:可控制检测的对象
    :return:
    '''
    # 获取键盘事件
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == pygame.QUIT:
            print('退出')
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print('left')
                plyobj.moveleft() # 调用函数实现移动
                pass

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('right')
                plyobj.moveright()
                pass

            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                print('up')
                plyobj.moveup()
                pass

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                print('down')
                plyobj.movedown()
                pass

            elif event.key == pygame.K_SPACE:
                print('fire')
                plyobj.fire()


            # pass占位符放在哪里都一样
            # 如果在开发程序时，不希望立刻编写分支内部的代码
            # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！
            # 程序运行时，pass 关键字不会执行任何的操作！

    pass

# 主函数框架
def main ():
    # 首先创建一个窗口 用来显示内容
    screen= pygame.display.set_mode((400,500),depth=32)
    # 设定背景图片
    background = pygame.image.load('./demo/background.jpg')
    # 设置title
    pygame.display.set_caption('阶段总结，飞机游戏')

    #添加背景音乐
    pygame.mixer.init()
    pygame.mixer_music.load('./demo/jinitaimei.mp3')
    pygame.mixer_music.set_volume(0.5) # 设置音量
    pygame.mixer_music.play(-1) # 循环次数，-1代表无限循环

    # 创建玩家实例对象
    player = Player(screen)
    # 创建敌人实例对象
    enemy = Enemy(screen)

    #设定要显示的内容
    while True:
        screen.blit(background,(0,0)) #显示背景图片0.0代表坐标
        player.display() #显示玩家图片0.0代表坐标
        enemy.display()
        enemy.move() # 不触发不会动
        enemy.fire() # 不处罚不会发射
        # 获取键盘事件
        key_control(player)


        # 更新显示内容
        pygame.display.update()
        time.sleep(0.001)

    pass
if __name__=='__main__':
    main()