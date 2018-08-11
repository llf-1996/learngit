# coding:utf-8
'''
v2 : 游戏中的各种尺寸处理
游戏窗口屏幕的：宽高
英雄飞机的：宽、高、x、y
使用pygame提供的方法pygame.Rect()存储数据

v3: 精灵对象[图片、位置、速度] [更新]，一个游戏元素
pygame.sprite.Sprite
存放精灵对象的精灵组
pygame.sprite.Group   >>> 更新(update-调用所有精灵对象的update方法) >>> 渲染draw(screen)

'''
import pygame


class GameSprite(pygame.sprite.Sprite):
    '''
    游戏精灵
    '''
    def __init__(self, image_path, speed=1):
        # 手工运行父类初始化方法
        super().__init__()
        '''

        :param image_path: 图片路径
        :param speed: 速度
        '''
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


##########################################################################
##########################################################################
##########################################################################
SCREEN_SIZE = (512, 768)

# # 定义游戏资源 长方形资源
# # 屏幕资源
# screen_rect = pygame.Rect(0, 0, 512, 768)
# # 英雄资源
# hero_rect = pygame.Rect(196, 500, 120, 79)

# 英雄飞机的：宽度和高度

# 创建游戏窗口
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption('飞机大战')
# 游戏初始化
pygame.init()

# 游戏背景
background = GameSprite('./images/bg_img_1.jpg', speed=0)
# # 添加背景精灵到精灵组中
# resource = pygame.sprite.Group(background)

# 英雄飞机
hero = GameSprite('./images/hero.png', speed=2)
# 添加精灵对象到精灵组中
resource = pygame.sprite.Group(background, hero)

# 游戏循环
while True:
    # 精灵组 刷新渲染所有包含的精灵
    resource.update()
    resource.draw(screen)

    # 当前屏幕刷新
    pygame.display.update()


pygame.quit()



