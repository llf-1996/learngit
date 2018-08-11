# 1.准备工作
开发目标：飞机大战
需要资源：飞机大战需要的各种资源图片
游戏原理：~让图片产生动画，动画效果还原游戏场景！
	操作细节：让图片在很短的时间进行切换，完成一个模拟动画的效果！
需要技术：pygame:python中提供的专门用于游戏开发的一个模块！
	不是系统标准模块，第三方模块
	安装第三方模块：命令行~
		windows：管理员权限运行命令行-: pip install pygame
			pip: python install package

###设置屏幕字体
使用系统自带的字体：my_font = pygame.font.SysFont("arial", 16)
第一个参数是字体名，第二个自然就是大小，一般来说“Arial”字体在很多系统都是存在的，如果找不到的话，就会使用一个默认的字体，这个默认的字体和每个操作系统相关，你也可以使用pygame.font.get_fonts()来获得当前系统所有可用字体。
你也可以使用pygame.font.get_fonts()来获得当前系统所有可用字体。还有一个更好的方法的，使用TTF的方法：
my_font = pygame.font.Font("my_font.ttf", 16)
这个语句使用了一个叫做“my_font.ttf”，这个方法之所以好是因为你可以把字体文件随游戏一起分发，避免用户机器上没有需要的字体。。一旦你创建了一个font对象，你就可以

使用render方法来写字了，然后就能blit到屏幕上：
text_surface = my_font.render("Pygame is cool!", True, (0,0,0), (255, 255, 255))
第一个参数是写的文字；第二个参数是个布尔值，以为这是否开启抗锯齿，就是说True的话字体会比较平滑，不过相应的速度有一点点影响；第三个参数是字体的颜色；第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。
追加说明一下如何显示中文， 简单来说，首先你得用一个可以使用中文的字体，宋体、黑体什么的，或者你直接用中文TTF文件，然后文字使用unicode，即u”中文的文字”这种，最后不要忘了源文件里加上一句关于文件编码的“魔法注释”。
>注：设置字体必须在游戏初始化之后才可以。即pygame.init()

###python中format函数用于字符串的格式化
* 通过关键字
```
print('{名字}今天{动作}'.format(名字='a',动作='a'))#通过关键字
grade = {'name' : 'a', 'score': '59'}
print('{name}电工考了{score}'.format(**grade))#通过关键字，可用字典当关键字传入值时，在字典前加**即可
```
* 通过位置
```
print('{1}今天{0}'.format('拍视频','陈某某'))#通过位置
print('{0}今天{1}'.format('陈某某','拍视频'))
```

#2.pygame快速入门
pygame游戏模块
安装：pip install pygame
任意游戏
游戏开始时：加载pygame中各种资源：pygame.init()
游戏结束时：卸载pygame中各种资源：pygame.quit()
游戏界面
游戏窗口：pygame.display模块进行处理操作
set_mode(area, flags, depth)：窗口对象
area：游戏区域，元组(宽度，高度)
flags：整数参数，控制是否全屏等..
depth：图片颜色深度[8bit/16bit/24bit/32bit]
set_caption(title_name)
title_name：游戏窗口标题
加载图片：pygame.image
load(path)：将指定路径的图片，添加到内存中
渲染图片
窗口对象.blit(img, (x, y))：添加一个图片到游戏窗口的某个位置
窗口对象.update()：将添加到游戏窗口的对象，渲染到界面上展示

#3.游戏资源位置对象
pygame.Rect(left, top, width, height)
2D游戏中，所有的游戏资源都有四个具体的数据表示它在屏幕中的展示
距离屏幕左边的距离：left 也称为x坐标
距离屏幕上边的距离：top 也称为y坐标
资源本身的宽度：width
资源本省的高度：height

pygame中提供了一个用于表示这四个数据的对象：位置对象：pygame.Rect
rect = pygame.Rect(x, y, width, height)
获取左边的距离：rect.left | rect.x
获取上边的距离：rect.top | rect.y
获取元素的尺寸：rect.size
获取中间的位置：rect.centerx | rect.centery

位置对象Rect可以直接在屏幕对象的blit(资源, 位置)中进行使用
screen.blit(hero, (196, 500)) screen.blit(hero, hero_rect)

#4.游戏核心操作
游戏运行过程中-> 核心~图片在运动-> 大量的图片在运动
抽象：图片在运动

游戏对象所需参数：图片、位置、速度
pygame将所有的任意的游戏操作开发中用到的对象：封装一个类型
	精灵对象[图片、位置、速度][更新]
		pygame.sprite.Sprite
		QUSTION:如果游戏中出现了大量的图片~每个图片都是一个精灵对象~
	精灵组对象[添加精灵]->更新->渲染->将组中的所有精灵，全部渲染到窗口中！
		pygame.sprite.Group
			更新(update->调用所有精灵对象update)、渲染draw(screen)

所有的2D游戏开发：都是图片的转换！
	图片对象[图片路径、位置、运动速度][ 更新位置 ]
	游戏精灵对象——表示2D游戏中，任意的一个游戏元素
	
	为了方便我们操作大量的游戏元素[游戏精灵]：精灵组对象
	精灵组对象管理游戏中出现的所有精灵对象！

#5. 飞机大战程序流程
```
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
```

# 6. 游戏正式开始
###游戏背景处理：
	游戏背景的运动，需要两张一样的图片上下叠加，完成整体运动效果图。

游戏背景：也是游戏资源的一种，所以让 背景 继承游戏精灵类型
	游戏背景类型中，初始化方法定义背景的图片信息，重写update()方法完成自定义运动

###英雄飞机出场
我方英雄飞机，也是游戏资源的一种，但是运动方式需要通过键盘进行控制。英雄飞机~也定义成一种类型，继承游戏精灵类型，速度设置0，暂时不重写update()方法。

###事件操作
事件：发生的一个操作行为，如用户按下了鼠标左键！
操作：事件的响应，事件发生之后的处理方式[函数/方法]

pygame处理事件：pygame.event
获取所有的当前窗口中发生的事件：pygame.event.get() -> list类型
pygame对于键盘的交互方式，提供pygame.key
完成对用户键盘按下、抬起，按住等各种事件的直接处理

###控制游戏刷新帧
常规情况下，当画面每秒刷新24+以上，肉眼看到连续的动画！
正常游戏处理过程中，要求画面刷新帧在50+以上！
个人PC屏幕刷新60~

pygame怎么控制游戏的刷新帧
	默认情况，没有控制：循环游戏场景会短时间以最大的速度循环！极浪费系统性能
	pygame提供了一个时钟操作：通过时钟操作~精确控制循环刷新帧
pygame.time
	time.tick(每秒刷新帧) 让当前循环游戏场景每秒运行几次
	主要定义在游戏场景循环中，用于控制游戏场景刷新！

### 英雄子弹操作
子弹：一个独立的对象，依赖于英雄飞机，所以将子弹精灵组对象，做成英雄飞机的一个属性。

子弹：如果飞出边界~销毁
	销毁一个对象[python中如果一个对象不再使用自动销毁(没有变量指向)]

pygame提供了精灵对象的操作方式
	可以将对象自己从精灵组中移除同时销毁
	可以调用对象的kill()函数！

在子弹的继承的update()函数中，重写边界判断，一旦超出边界~移除自己！

###敌方飞机出场
敌方飞机~类型，敌人精灵-> 创建多个敌人-> 精灵组-> 渲染展示窗口中！
多长时间出现一个敌机？定时
出现的位置？顶部随机

定时器：间隔一定的事件，自动触发操作[事件]
自定义事件：pygame不可能包含所有游戏中可能发生的行为，所以提供了一个自定操作的事件：pygame.USEREVNET，确保用户在操作过程中，不会和系统中自己的事件冲突！ENEMY_CREATE = pygame.USEREVENT # 定义一个事件
```
ENEMY_FIRE = pygame.USEREVENT + 1   # 自定义下一个事件
# 间隔一定的时间，触发一次创建敌机的事件
pygame.time.set_timer(ENEMY_CREATE, 3000)   # 毫秒
# 间隔一定时间，敌机发射子弹
pygame.time.set_timer(ENEMY_FIRE, 1500)
```

###碰撞检测
采用pygame的碰撞检测方法
```
# 子弹碰撞检测，第一个True表示自动调用kill方法删除第一个精灵组即enemy.enemy_bullets；第二个同理，也可以设为False则不会该精灵。
pygame.sprite.groupcollide(enemy.enemy_bullets, self.hero.bullets, True, True)
e = pygame.sprite.spritecollide(self.hero, enemy.enemy_bullets, True)
# 敌机精灵组和英雄子弹精灵组碰撞检测
re1 = pygame.sprite.groupcollide(self.enemys, self.hero.bullets, False, True)
# 敌机精灵组和英雄飞机精灵碰撞检测
e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
```
> 调用kill()方法会调用__del__魔法方法。

### 渲染展示
两种方式，第一种调用窗口对象的blit()方法，第二种将哟偶系精灵添加到精灵组，调用精灵组的update()方法。两种方法不管哪一种最后一定要执行屏幕更新方法pygame.display.updata()才可以显示到屏幕上。
```
 # 精灵组渲染
 self.resources.update()
self.resources.draw(self.screen)
# 文字渲染
level_text = self.level_font.render('level:%s' % data.now, True, [255, 0, 0])
self.screen.blit(level_text, (0, 0))
 # 屏幕更新
 pygame.display.update()
```


---
