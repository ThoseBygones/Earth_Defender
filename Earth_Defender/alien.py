# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:41:40 2019

@author: Sherlock Holmes
"""

import pygame
from pygame.sprite import Sprite
import random

"""外星人类"""
class Alien(Sprite):
    """初始化外星人并设置其初始位置"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像，并设置其self.rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.centerx = self.rect.width / 2
        self.rect.centery = self.rect.height / 2
        
        # 存储外星人的准确位置（中心坐标）
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # 外星人在横向的移动方向
        # 值为-1时表示向左移动，为0时表示不左右移动，为1时表示向右移动
        self.direction = 0

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
    
    def random_direction(self):
        """为外星人选择一个横向移动的方向"""
        self.direction = random.randint(-1, 1)
    
    def update(self):
        """更新外星人位置"""
        self.centerx += self.direction * self.ai_settings.alien_speed_factor
        self.centery += self.ai_settings.alien_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    