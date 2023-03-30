# 管理图形、动画等功能模块
import pygame
# 系统的模块
import sys
# 游戏自定义配置的类
from setting import Settings
# 游戏自定义的飞船的类
from ship import Ship
# 游戏自定义的飞船子弹的类
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 原始代码
        # self.screen = pygame.display.set_mode((800, 400))

        # 配置独立后的代码
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        """全屏模式运行，但是必须要支持按"q"退出，不然右上角没有x可以点退出"""
        # self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)      # 这里self代表当前文件的内存地址

        # 设置背景色（用的是RGB值来指定颜色，每个值的取值范围是0~255）
        # 红色：(255, 0, 0);绿色：(0, 255, 0);蓝色：(0, 0, 255)，默认是黑色(0, 0, 0)
        # 相关配置放在setting.py的类中独立使用
        # self.bg_color = (135, 206, 235)

        self.num = 0

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的循环"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    """重构方法，使用辅助方法，辅助方法是在类中执行任务，并非用实例去调用--- 辅助方法是在名前加_"""

    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     # 当点击鼠标关闭窗口时，会触发pygame.QUIT事件
            #     sys.exit()
            if event.type == pygame.KEYDOWN:
                # 当按键时
                self.num += 1
                print(f"收到按键了{self.num}")
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键，一定一定记得，按键时输入法要是英文的！！！"""
        if event.key == pygame.K_RIGHT:
            # print(f"按了右键")
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # print(f"按了左键")
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # print(f"按了{event.key}键")
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 按下空格时发射子弹
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见，不断更新新屏幕，擦掉旧屏幕，有点像reload热更新，有新变化就更新了
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
