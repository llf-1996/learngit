# coding:utf-8

import pygame
import random
import data
import time


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


class BackgroudSprite(GameSprite):
    '''背景精灵'''
    def __init__(self, image_path, speed=1, prepare=False):
        super().__init__(image_path, speed)

        if prepare:
            self.rect.y = -data.SCREEN_SIZE[1]

    def update(self):
        # 调用父类的方法，执行运动
        super().update()
        # 子类中判断边界
        if self.rect.y > data.SCREEN_SIZE[1]:
            self.rect.y = -data.SCREEN_SIZE[1]


# class BolSprite(GameSprite):
#     def __init__(self, image_path, speed):
#         super().__init__(image_path, speed)
#         # self.image = pygame.image.load(image_path)
#
#
#             # time.sleep(1)

class Plan(GameSprite):
    def __init__(self, image_path, speed, hp):
        super().__init__(image_path, speed)
        self.hp = hp
        # 音效
        self.bol_m = pygame.mixer.Sound('./music/bol1.wav')  # 爆炸音效
        self.fire_m = pygame.mixer.Sound('./music/枪声1.wav')  # 英雄飞机开火音效

    def bol(self):
        self.bol_m.play()

        for img in ['./images/enemy2_down3.png', './images/enemy2_down3.png',
                    './images/enemy2_down3.png', './images/enemy2_down3.png',
                    './images/enemy2_down4.png', './images/enemy2_down4.png']:
            # pass
            self.image = pygame.image.load(img)
            time.sleep(0.03)
            # xuanran_zhanshi()  # todo
            # 精灵组渲染
            data.resources.update()
            data.resources.draw(data.screen)
            # 子弹精灵组渲染
            data.hero.bullets.update()
            data.hero.bullets.draw(data.screen)

            #  渲染敌机精灵组中的所有飞机
            data.enemys.update()
            data.enemys.draw(data.screen)
            # 屏幕更新
            pygame.display.update()
        # time.sleep(0.1)
        # 销毁
        self.kill()

    def fire(self):
        '''飞机开火'''
        self.fire_m.play()  # 开火音效


class HeroSprite(Plan):
    '''英雄精灵对象'''
    def __init__(self, hp):
        super().__init__('./images/hero.png', speed=0, hp=hp)
        # 初始化英雄飞机的位置
        self.rect.x = data.SCREEN_RECT.centerx
        self.rect.y = data.SCREEN_RECT.centery + 300
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= data.SCREEN_RECT.width - self.rect.width:
            self.rect.x = data.SCREEN_RECT.width - self.rect.width
        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= data.SCREEN_RECT.height - self.rect.height:
            self.rect.y = data.SCREEN_RECT.height - self.rect.height

    def __del__(self):
        # self.bol()
        print('英雄飞机销毁...')

    def fire(self):
        '''飞机攻击'''
        # 子弹少于6个添加子弹到精灵组对象
        if len(self.bullets) <= 6:
        # 创建子弹
            bullet = BulletSprite(self.rect.centerx, self.rect.y)
            self.bullets.add(bullet)
            super().fire()

    def bol(self, hurt):
        self.hp -= hurt
        if self.hp <= 0:
            super().bol()
            pygame.quit()
            exit()


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


class EnemySprite(Plan):
    '''敌方飞机'''

    def __init__(self, hp=100):
        ''''''
        # 初始化敌方飞机的数据：图片、速度
        super().__init__('./images/enemy2.png', speed=random.randint(2, 3), hp=hp)
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, data.SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 100

    def update(self):
        super().update()
        # 边界判断
        if self.rect.y > data.SCREEN_RECT.height:
            # 敌方飞机超出屏幕销毁
            self.kill()

    def bol(self, hurt):
        self.hp -= hurt
        if self.hp <= 0:
            super().bol()
        # super().bol()

