# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:18:15 2019

@author: Sherlock Holmes
"""

"""记录游戏统计信息的类"""
class GameStats():
    """初始化统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 设置游戏的最高分
        self.high_score = 0
        # 设置游戏初始等级
        self.level = 1
        
    """初始化在游戏运行期间可能变化的统计信息"""
    def reset_stats(self):
        # 初始化飞船的数量
        self.spaceship_cnt = self.ai_settings.spaceship_limit
        # 初始化游戏得分
        self.score = 0
    