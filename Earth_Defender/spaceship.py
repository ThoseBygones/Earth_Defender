# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:24:33 2019

@author: Sherlock Holmes
"""

import pygame
from pygame.sprite import Sprite

"""飞船类"""
class Spaceship(Sprite):
    
    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        
        # 飞船的移动标志（向左和向右）
        self.moving_left = False
        self.moving_right = False
        
    """根据飞船的移动标志改变飞船的位置"""
    def update(self):
        """更新飞船的self.center值而不是self.rect对象"""
        # 飞船向左移动但未移出屏幕的最左端
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.spaceship_speed_factor
        # 飞船向右移动但未移出屏幕的最右端
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.spaceship_speed_factor
        """同时按下的时候飞船位置不会改变"""
        
        # 根据self.center的值更新self.rect对象
        self.rect.centerx = self.center
        
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
    
    """将飞船放置在屏幕地步中间处"""
    def place_center(self):
        self.center = self.screen_rect.centerx
