# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:26:07 2019

@author: Sherlock Holmes
"""

import pygame.font

"""按钮类"""
class Button():
    """初始化按钮的属性"""
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮的尺寸和其他属性
        self.width, self.height = (200, 50)
        self.button_color = (245, 222, 179)
        self.text_color = (0, 0, 139)
        self.font = pygame.font.SysFont("sthupo", 42)
        
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 按钮的标签只需要创建一次
        self.create_msg(msg)
    
    """将msg渲染为图像，并使其在按钮上居中"""
    def create_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    """绘制一个用颜色填充的按钮，再绘制文本"""
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
