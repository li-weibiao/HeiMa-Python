import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 在plane_sprites设置了一个常量，通过size
        # 来返回一个大小的元组，因为set_mode接受一个元组的值
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件 - 创建敌人飞机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 以毫秒为单位
        # 设置定时器事件 - 子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)     # 间隔0.5秒发射子弹

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        # bg1 = Background("./images/background.png")
        # bg2 = Background("./images/background.png")
        # bg2.rect.y = -bg2.rect.height
        bg1 = Background()
        bg2 = Background(True)  # 由精灵自己负责初始位置

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌人飞机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)  # 设置了一个常量
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()  # 通过类名调用静态方法
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌人飞机出场")
                # 创建敌人飞机精灵
                enemy = Enemy()

                # 将敌人飞机精灵添加到敌人飞机精灵组
                self.enemy_group.add(enemy)
            # 捕捉发射子弹的事件
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")

        # 使用键盘提供的方法获取键盘按键 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            # print("向右移动....")
            self.hero.speed = 2        # 通过设置这速度，来实现英雄左右移动
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1. 子弹摧毁敌人飞机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)  # 第一个True是子弹碰撞敌人飞机，子弹被摧毁
        # 第二个True是敌人飞机碰撞子弹，敌人飞机被摧毁

        # 2. 敌人飞机碰撞毁灭英雄飞机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)  # 实现后会返回一个列表值

        # 判断列表是否有内容
        if len(enemies) > 0:

            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)  # 敌人飞机也要知道在哪个屏幕，所以传递了screen参数

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod  # 静态方法，不需要实例
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
