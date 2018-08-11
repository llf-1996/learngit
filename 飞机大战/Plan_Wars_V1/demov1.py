import pygame

hero_y = 500

# 初始化所有的pygame模块
pygame.init()

# 创建一个游戏窗口
screen = pygame.display.set_mode((512, 768), 0, 32)

# 设置游戏窗口标题
pygame.display.set_caption('飞机大战')

# 添加一个背景图片
background_image = pygame.image.load('./images/bg_img_1.jpg')

# 需要用户不断的进行操作，保证游戏的持续运行，游戏场景循环！
while True:
    # 将背景图片渲染到窗口中展示
    screen.blit(background_image, (0, 0))

    # 添加英雄飞机到窗口中
    hero = pygame.image.load('./images/hero.png')
    screen.blit(hero, (196, hero_y))
    hero_y -= 5
    if hero_y < -79:
        hero_y = 768

    # 渲染展示
    pygame.display.update()

# 程序退出
pygame.quit()

