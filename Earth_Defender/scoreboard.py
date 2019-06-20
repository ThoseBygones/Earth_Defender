# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:40:26 2019

@author: Sherlock Holmes
"""

import pygame.font
from pygame.sprite import Group
from spaceship import Spaceship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 显示得分信息时使用的字体设置
        self.text_color_1 = (230, 230, 230)
        self.text_color_2 = (255, 0, 0)
        self.font = pygame.font.SysFont("SimHei", 30)
        
        # 准备初始得分图像
        self.draw_score()
        # 准备最高得分图像
        self.draw_high_score()
        # 准备游戏等级图像
        self.draw_level()
        # 准备飞船图像
        self.draw_spaceships()
    
    def draw_score(self):
        """将得分转换为渲染的图像"""
        # 将得分圆整，保证分数是10的倍数
        rounded_score = round(self.stats.score, -1)
        score_str = "得分：" + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color_1)
        
        # 将得分板放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def draw_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "最高分：" + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
                                                 self.text_color_2)
        
        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def draw_level(self):
        """将等级转换为渲染的图像"""
        level_str = "等级：" + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color_1)
        # 将等级放在当前得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def draw_spaceships(self):
        """将剩余飞船数量渲染为图像"""
        self.spaceships = Group()
        for spaceship_cnt in range(self.stats.spaceship_cnt):
            spaceship = Spaceship(self.ai_settings, self.screen)
            spaceship.rect.x = 10 + spaceship_cnt * (spaceship.rect.width + 10)
            spaceship.rect.y = 10
            self.spaceships.add(spaceship)
    
    def show_score(self):
        """在屏幕上显示得分、等级、剩余飞船等游戏数据"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.spaceships.draw(self.screen)
