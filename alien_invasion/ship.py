import pygame


class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置
        当此类被alien_invasion调用时，ai_game就会被赋值为alien_invasion
        用的screen.get_rect是alien_invasion.py里的定义"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings    # 这里的self.settings是用的alien_invasion.py里边的

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 蓝天的背景里导入太阳
        # self.image = pygame.image.load('images/sun.jpg')
        # self.image = pygame.transform.scale(self.image, (200, 200))    # 图片太大，调整图片分辨率
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部中央（放在中央：center）
        # 这里意思是飞船的底部中心点和屏幕的底部中心点相等，所以相当于放在屏幕底部中心了
        self.rect.midbottom = self.screen_rect.midbottom
        # 或者指定屏幕的x和y坐标
        # self.rect.x = 100
        # self.rect.y = 200

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船而不是rect对象的x值，并通过飞船外接矩形的x坐标和屏幕右下角边缘坐标对比，限制飞船不能飞出屏幕外
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
