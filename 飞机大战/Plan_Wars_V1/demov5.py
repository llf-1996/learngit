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

'''
import pygame


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵对象：用于表示游戏中的各种元素'''
    def __init__(self, image_path, speed = 1):
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


class HeroSprite(GameSprite):
    '''英雄精灵对象'''
    def __init__(self):
        super().__init__('./images/hero.png', speed=0)
        # 初始化英雄飞机的位置
        self.rect.x = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 300

    # def update


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

# 定义英雄飞机对象
hero = HeroSprite()

# 定义精灵组对象
resources = pygame.sprite.Group(bg1, bg2, hero)

# 游戏场景循环
while True:
    # 精灵组渲染
    resources.update()
    resources.draw(screen)

    # 屏幕更新
    pygame.display.update()

# 卸载游戏模块
pygame.quit()

