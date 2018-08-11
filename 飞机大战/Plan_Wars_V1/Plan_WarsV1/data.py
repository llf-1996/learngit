# coding:utf-8
import pygame
# 自定义一个事件
# 创建敌机事件
ENEMY_CREATE = pygame.USEREVENT
# 敌机开火事件
ENEMY_FIRE = pygame.USEREVENT + 1   # 自定义下一个事件

SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)

hero = None
resources = None
enemys = None
screen = None
