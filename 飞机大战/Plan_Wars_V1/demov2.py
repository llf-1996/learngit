# coding:utf-8
'''
v2 : 游戏中的各种尺寸处理
游戏窗口屏幕的：宽高
英雄飞机的：宽、高、x、y
使用pygame提供的方法pygame.Rect()存储数据
'''
import pygame

pygame.init()

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

# 创建游戏背景图片+Rect位置对象
background_img = pygame.image.load('./images/bg_img_1.jpg')
background_rect = pygame.Rect(0, 0, *SCREEN_SIZE)

# 创建英雄飞机图片+Rect位置对象
hero = pygame.image.load('./images/hero.png')
hero_rect = pygame.Rect(196, 500, 120, 79)

# 游戏场景循环
while True:
    # 英雄飞机移动的操作
    hero_rect.y -= 2
    if hero_rect.y < -hero_rect.height:
        hero_rect.y = background_rect.height

    # 将背景和英雄飞机添加到窗口中
    screen.blit(background_img, background_rect)
    screen.blit(hero, hero_rect)

    # 渲染展示
    pygame.display.update()

pygame.quit()


