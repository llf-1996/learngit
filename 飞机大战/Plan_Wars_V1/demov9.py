'''
v2 : 游戏中的各种尺寸处理
游戏窗口屏幕的：宽高
英雄飞机的：宽、高、x、y
使用pygame提供的方法pygame.Rect()存储数据

v3: 精灵对象[图片、位置、速度] [更新]，一个游戏元素
pygame.sprite.Sprite
存放精灵对象的精灵组
pygame.sprite.Group   >>> 更新(update-调用所有精灵对象的update方法) >>> 渲染draw(screen)

v4: 游戏正式开发
背景处理：让背景实现无缝滚动

v5: 英雄飞机出场

v6: 监听用户键盘事件

v7: 英雄飞机移动边界处理,开火

v8：敌方飞机出场，自定义事件-定时器

v9：碰撞检测
    1.子弹和敌机
    2.敌机和英雄飞机
    3. 爆炸效果、敌机血量

'''
import pygame
import random
# import data
import time

# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
# OTHER_EVENT = pygame.USEREVENT + 1   # 自定义下一个事件


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵对象：用于表示游戏中的各种元素'''
    def __init__(self, image_path, speed=1):
        # 调用父类初始化数据
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''默认运动更新方法'''
        self.rect.y += self.speed

    def bol(self):
        for img in ['./images/enemy2_down3.png', './images/enemy2_down3.png',
                    './images/enemy2_down3.png', './images/enemy2_down3.png',
                    './images/enemy2_down4.png', './images/enemy2_down4.png']:
            # pass
            time.sleep(0.01)
            self.image = pygame.image.load(img)
            xuanran_zhanshi()
        # 销毁
        self.kill()


class BackgroudSprite(GameSprite):
    '''背景精灵'''
    def __init__(self, image_path, prepare=False):
        super().__init__(image_path)

        if prepare:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类的方法，执行运动
        super().update()
        # 子类中判断边界
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


# class BolSprite(GameSprite):
#     def __init__(self, image_path, speed):
#         super().__init__(image_path, speed)
#         # self.image = pygame.image.load(image_path)
#
#
#             # time.sleep(1)


class HeroSprite(GameSprite):
    '''英雄精灵对象'''
    def __init__(self):
        super().__init__('./images/hero.png', speed=0)
        # 初始化英雄飞机的位置
        self.rect.x = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 300
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def __del__(self):
        # self.bol()
        print('英雄飞机销毁...')

    def fire(self):
        '''飞机攻击'''
        # 创建子弹
        bullet = BulletSprite(self.rect.centerx, self.rect.y)
        # 添加到精灵组对象
        self.bullets.add(bullet)


class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self, x, y):
        super().__init__('./images/bullet2.1.png', speed=-5)
        self.rect.x = x - self.rect.width/2
        self.rect.y = y - self.rect.height
        # data.bullet_width = self.rect.width
        # data.bullet_height = self.rect.height

    def update(self):
        # 调用父类分方法进行操作
        super().update()

        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()

    def __del__(self):
        print('子弹已经销毁...')


class EnemySprite(GameSprite):
    '''敌方飞机'''
    def __init__(self):
        ''''''
        # 初始化敌方飞机的数据：图片、速度
        super().__init__('./images/enemy2.png', speed=random.randint(2, 4))
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 100

    def update(self):
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 敌方飞机超出屏幕销毁
            self.kill()

    def bol(self):
        self.hp -= 20
        if self.hp <= 0:
            super().bol()
        # super().bol()


def xuanran_zhanshi():
    # 精灵组渲染
    resources.update()
    resources.draw(screen)
    # 子弹精灵组渲染
    hero.bullets.update()
    hero.bullets.draw(screen)

    #  渲染敌机精灵组中的所有飞机
    enemys.update()
    enemys.draw(screen)
    # 屏幕更新
    pygame.display.update()


##########################################
SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)
# 游戏初始化
pygame.init()

# 定义游戏窗口
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 24)
pygame.display.set_caption('飞机大战')

# 定义背景精灵
bg1 = BackgroudSprite('./images/bg_img_2.jpg')
bg2 = BackgroudSprite('./images/bg_img_2.jpg', prepare=True)
# 定义英雄飞机精灵对象
hero = HeroSprite()

# 定义精灵组对象
resources = pygame.sprite.Group(bg1, bg2, hero)
# 定义敌机精灵组对象
enemys = pygame.sprite.Group()
# 间隔一定的时间，触发一次创建敌机的事件
pygame.time.set_timer(ENEMY_CREATE, 1000)

# 定义时钟对象
clock = pygame.time.Clock()

# 游戏场景循环
while True:
    # 定义时钟刷新帧，每秒让循环运行多少次！
    clock.tick(60)

    # 监听所有的事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
        for event in event_list:
            # 如果当前的事件是QUIT事件
            if event.type == pygame.QUIT:
                # 卸载所有的pygame资源，退出程序
                pygame.quit()
                exit()
            if event.type == ENEMY_CREATE:
                print('创建一架敌机....')
                enemy = EnemySprite()
                # 添加到敌方飞机精灵组中
                enemys.add(enemy)

            # if event.type == pygame.KEYDOWN:
            #     if  event.key == pygame.K_LEFT:
            #         print('英雄飞机向左移动。。。')
            #     if event.key == pygame.K_RIGHT:
            #         print('英雄飞机向右移动')
            #     if event.key == pygame.K_UP:
            #         print('英雄飞机向上移动')
            #     if event.key == pygame.K_DOWN:
            #         print('英雄飞机向下移动....')
            #     if event.key == pygame.K_SPACE:
            #         print('英雄飞机开火...')

    # 获取当前用户键盘上被操作的案件
    key_down = pygame.key.get_pressed()

    if key_down[pygame.K_LEFT]:
        print('向左移动《《《《')
        hero.rect.x -= 5
    if key_down[pygame.K_RIGHT]:
        print('向右移动》》》》')
        hero.rect.x += 5
    if key_down[pygame.K_UP]:
        print('向上移动^^^^^^^^^^')
        hero.rect.y -= 5
    if key_down[pygame.K_DOWN]:
        print('向下移动')
        hero.rect.y += 5
    if key_down[pygame.K_SPACE]:
        print('飞机开火...')
        hero.fire()

    # 碰撞检测, 子弹和敌机
    re1 = pygame.sprite.groupcollide(enemys, hero.bullets, False, True)
    for i in re1:
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print(type(i))
        # i.hp -= 50
        i.bol()
    # print('#########################')
    # print(type(re1))
    # print(re1)
    # print(re1.keys())
    # print('##############################')

    # 敌机和英雄飞机
    e = pygame.sprite.spritecollide(hero, enemys, True)
    if len(e):
        hero.bol()
        # hero.kill()
        pygame.quit()
        exit()
    # 渲染展示
    xuanran_zhanshi()
    # # 精灵组渲染
    # resources.update()
    # resources.draw(screen)
    #
    # # 子弹精灵组渲染
    # hero.bullets.update()
    # hero.bullets.draw(screen)
    #
    # #  渲染敌机精灵组中的所有飞机
    # enemys.update()
    # enemys.draw(screen)
    #
    # # 屏幕更新
    # pygame.display.update()

# 卸载游戏模块
pygame.quit()

