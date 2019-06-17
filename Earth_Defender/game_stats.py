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
        self.game_state = self.ai_settings.GAME_READY
        # 设置游戏的最高分
        self.high_score = 0
        # 设置游戏初始等级
        self.level = 1
        # 每一级内击杀外星人数量
        self.kill_cnt = 0
        # 记录游戏的帧数（对100取模）
        self.game_frame = 0
        
    """初始化在游戏运行期间可能变化的统计信息"""
    def reset_stats(self):
        # 初始化飞船的数量
        self.spaceship_cnt = self.ai_settings.spaceship_limit
        # 初始化游戏得分
        self.score = 0
        # 初始化每一等级的初始击杀数量
        self.kill_cnt = 0
        # 初始化游戏的帧数
        self.game_frame = 0
    