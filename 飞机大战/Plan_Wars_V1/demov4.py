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

v4: 游戏正式开发
背景处理：让背景实现无缝滚动
'''
import pygame


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵'''
    def __init__(self, image_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    '''背景精灵'''
    def __init__(self, speed=3, prepare=False):
        super().__init__('./images/bg_img_2.jpg')
        self.speed = speed
        if prepare:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类的update让其移动
        super().update()
        # 判断位置
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


###############################################
SCREEN_SIZE = (512, 768)
# 初始化
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('飞机大战')

# 渲染背景
# bg1 = GameSprite('./images/bg_img_2.jpg')
# bg2 = GameSprite('./images/bg_img_2.jpg')
bg1 = BackgroundSprite()
bg2 = BackgroundSprite(prepare=True)
# bg2.rect.y = -SCREEN_SIZE[1]

# 添加到精灵组
resources = pygame.sprite.Group(bg1, bg2)

# 游戏场景循环
while True:
    # 精灵组渲染
    resources.update()
    resources.draw(screen)

    # 窗口渲染展示
    pygame.display.update()

# 卸载模块
pygame.quit()
