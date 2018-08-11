# coding:utf-8

import pygame
import game_sprites
import data


##########################################

class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode(data.SCREEN_SIZE, 0, 24)
        pygame.display.set_caption('飞机大战')
        data.screen = self.screen

        # 定义时钟对象
        self.clock = pygame.time.Clock()

        # 自定义一个事件
        self.ENEMY_CREATE = pygame.USEREVENT
        # 时钟刷新帧数
        self.the_tick = 45

    def create_scene(self):
        self.bg1 = game_sprites.BackgroudSprite('./images/bg_img_2.jpg')
        self.bg2 = game_sprites.BackgroudSprite('./images/bg_img_2.jpg', prepare=True)
        self.hero = game_sprites.HeroSprite(hp=500)
        # 定义精灵组对象
        self.resources = pygame.sprite.Group(self.bg1, self.bg2, self.hero)
        # 定义敌机精灵组对象
        self.enemys = pygame.sprite.Group()

        data.enemys = self.enemys
        data.hero = self.hero
        data.resources = self.resources

        # 间隔一定的时间，触发一次创建敌机的事件
        pygame.time.set_timer(self.ENEMY_CREATE, 2000)

        # bgm
        pygame.mixer_music.load('./music/fight.wav')
        pygame.mixer_music.play(-1)

    def xuanran_zhanshi(self):
        # 精灵组渲染
        self.resources.update()
        self.resources.draw(self.screen)
        # 子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        #  渲染敌机精灵组中的所有飞机
        self.enemys.update()
        self.enemys.draw(self.screen)
        # 屏幕更新
        pygame.display.update()

    def check_collide(self):
        # 碰撞检测, 子弹和敌机
        re1 = pygame.sprite.groupcollide(self.enemys, self.hero.bullets, False, True)
        for i in re1:
            i.bol(50)

        # 敌机和英雄飞机
        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e):
            self.hero.bol(100)
            # time.sleep(0.25)
            # # hero.kill()
            # pygame.quit()
            # exit()

    def check_event(self):
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
                if event.type == self.ENEMY_CREATE:
                    print('创建一架敌机....')
                    enemy = game_sprites.EnemySprite()
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(enemy)

                if event.type == pygame.KEYDOWN:
                    #     if  event.key == pygame.K_LEFT:
                    #         print('英雄飞机向左移动。。。')
                    #     if event.key == pygame.K_RIGHT:
                    #         print('英雄飞机向右移动')
                    #     if event.key == pygame.K_UP:
                    #         print('英雄飞机向上移动')
                    #     if event.key == pygame.K_DOWN:
                    #         print('英雄飞机向下移动....')
                    if event.key == pygame.K_SPACE:
                        print('英雄飞机开火...')
                        self.hero.fire()

        # 获取当前用户键盘上被操作的案件
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            print('向左移动《《《《')
            self.hero.rect.x -= 5
        if key_down[pygame.K_RIGHT]:
            print('向右移动》》》》')
            self.hero.rect.x += 5
        if key_down[pygame.K_UP]:
            print('向上移动^^^^^^^^^^')
            self.hero.rect.y -= 5
        if key_down[pygame.K_DOWN]:
            print('向下移动')
            self.hero.rect.y += 5
        # if key_down[pygame.K_SPACE]:
        #     print('飞机开火...')
        #     hero.fire()

    def start(self):
        # 游戏初始化
        pygame.init()
        # 创建场景
        self.create_scene()

        # 游戏场景循环
        while True:
            # 定义时钟刷新帧，每秒让循环运行多少次！
            self.clock.tick(self.the_tick)
            # 事件监听
            self.check_event()
            # 碰撞检测
            self.check_collide()
            # 渲染展示
            self.xuanran_zhanshi()
        # 卸载游戏模块
        pygame.quit()

