# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:34:16 2019

@author: Sherlock Holmes
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船发射出子弹的类"""
    def __init__(self, ai_settings, screen, spaceship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen
        
        # 设置子弹参数并在坐标(0,0)处创建
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                                ai_settings.bullet_height)
        # 设置子弹初始位置在飞船的头部中间
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        # 用小数表示子弹的位置
        self.y = float(self.rect.y)
        # 设置子弹的颜色
        self.color = ai_settings.bullet_color
        # 设置子弹的速率
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """更新子弹的位置（向上飞）"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹位置的self.rect值
        self.rect.y = self.y
    
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
