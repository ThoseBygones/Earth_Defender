# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:41:40 2019

@author: Sherlock Holmes
"""

import pygame
from pygame.sprite import Sprite

"""外星人类"""
class Alien(Sprite):
    """初始化外星人并设置其初始位置"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像，并设置其self.rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    """在指定位置绘制外星人""" 
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    """判断外星人是否移动到屏幕的边缘"""
    def check_edges(self):
        # 如果碰到屏幕边缘，就返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    """向右移动外星人"""
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.alien_direction)
        self.rect.x = self.x
    