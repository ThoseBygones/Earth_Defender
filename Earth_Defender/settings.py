# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:03:46 2019

@author: Sherlock Holmes
"""

import pygame

"""存储《地球保卫者》的所有设置"""
class Settings():
    """初始化游戏的设置"""
    def __init__(self):
        # 定义常量
        self.GAME_READY = 0
        self.GAME_ACTIVE = 1
        self.GAME_PAUSED = 2
        
        # 设置屏幕
        self.screen_width = 800
        self.screen_height = 660
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('images/background.png')
        
        # 设置飞船数量限制
        self.spaceship_limit = 3
        
        # 设置子弹基本参数
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = (255, 255, 255)
        self.bullets_limit = 10
        
        # 设置外星人向下移动的速度
        self.alien_drop_speed = 10
        
        # 游戏节奏加快的速率
        self.speedup_rate = 1.2
        
        # 随着游戏节奏加快，消灭外星人获得分数增加的倍率
        self.score_rate = 1.2
        
        # 设置游戏动态参数
        self.init_dynamic_settings()
    
    """初始化随游戏进行而变化的设置"""    
    def init_dynamic_settings(self):
        # 设置飞船的速度
        self.spaceship_speed_factor = 2
        # 设置子弹的飞行速度
        self.bullet_speed_factor = 2.5
        # 设置外星人的移动速度
        self.alien_speed_factor = 1
        # alien_direction为-1时表示向左移动，为1时表示向右移动
        self.alien_direction = 1
        # 设置消灭每个外星人的得到的基础分数
        self.alien_points = 50
        
    """提高速度设置"""
    def increase_speed(self):
        self.spaceship_speed_factor *= self.speedup_rate
        self.bullet_speed_factor *= self.speedup_rate
        self.alien_speed_factor *= self.speedup_rate
        self.alien_points = int(self.alien_points * self.score_rate)
        