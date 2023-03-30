import pygame
import sys

class Test:
    def __init__(self, test):
        print(self)
        print(self.__class__)
        print(__name__)
        print(__class__)
        print(self.__module__)
        self.name = "BYZ"
        self.ship = test.ship
        # self.settings = test.settings
        # self.alien_invasion = test.alien_invasion
        self.aaa = test.settings


# Test()

running = True
while running:
    screen = pygame.display.set_mode((100, 100))
    # set background
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("4444")
            if event.key == pygame.K_RIGHT:
                print("66666")
            if event.key == pygame.K_UP:
                print("8888")
            if event.key == pygame.K_q:
                print("qqqq")
            if event.key == pygame.K_1:
                print("1111")
            pygame.display.update()