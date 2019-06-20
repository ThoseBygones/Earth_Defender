# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:24:33 2019

@author: Sherlock Holmes
"""

import pygame
from pygame.sprite import Sprite

class Spaceship(Sprite):
    """飞船类"""
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # 飞船的移动标志（上下左右）
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """根据飞船的移动标志改变飞船的位置"""
        # 飞船向左移动但未移出屏幕的最左端
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.spaceship_speed_factor
        # 飞船向右移动但未移出屏幕的最右端
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.spaceship_speed_factor
        # 飞船向上移动但还未太靠近屏幕顶端
        if self.moving_up and (self.rect.top > self.screen_rect.top + 2 * 
                               self.rect.width):
            self.centery -= self.ai_settings.spaceship_speed_factor
        # 飞船向下移动但还未移出屏幕底端
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.spaceship_speed_factor
        """同时按下相反方向按键时飞船位置不会改变"""
        
        # 根据self.center的值更新self.rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    
    
    def place_center(self):
        """将飞船放置在屏幕底部中间处"""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height / 2
