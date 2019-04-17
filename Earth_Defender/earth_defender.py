# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:45:48 2019

@author: Sherlock Holmes
"""

import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from spaceship import Spaceship
import game_functions as gf
from pygame.sprite import Group

"""游戏运行主函数"""
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 导入设置文件中对窗口的设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口顶部导航栏标题
    pygame.display.set_caption("Earth Defender")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建得分板
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船实例
    spaceship = Spaceship(ai_settings, screen)
    # 创建一个子弹编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_alien_group(ai_settings, screen, spaceship, aliens)
        
    # 开始游戏的主循环
    while True:
        # 监视并响应键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, spaceship, 
                        aliens, bullets)
        
        if stats.game_active:
            # 更新飞船的状态
            spaceship.update()
            # 更新子弹的状态
            gf.update_bullets(ai_settings, screen, stats, sb, spaceship, 
                              aliens, bullets)
            # 更新外星人的状态（在更新子弹后）
            gf.update_aliens(ai_settings, screen, stats, sb, spaceship, aliens, 
                             bullets)
        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, spaceship, aliens, 
                         bullets, play_button)
        
run_game()