# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:45:48 2019

@author: Sherlock Holmes
"""

import os
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from spaceship import Spaceship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """游戏运行主函数"""
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置游戏进行过程中的定时器
    clock = pygame.time.Clock()
    # 导入设置文件中对窗口的设置
    ai_settings = Settings()
    # 计算机屏幕分辨率大小
    win_size = (1366, 768)
    # 设置窗口在计算机屏幕的正中间显示
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % ((win_size[0] - 
              ai_settings.screen_width) / 2, (win_size[1] - 
                                      ai_settings.screen_height) / 2)
    # 创建游戏窗口
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口顶部导航栏标题
    pygame.display.set_caption("Earth Defender")
    # 设置窗口顶部导航栏图标
    pygame.display.set_icon(ai_settings.game_icon)
    # 创建“开始游戏”按钮
    play_button = Button(ai_settings, screen, "开始游戏")
    # 创建“继续游戏”按钮
    continue_button = Button(ai_settings, screen, "继续游戏")
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
        
    # 开始游戏的主循环
    while True:
        # 控制游戏最大帧率为 120
        clock.tick(120)
        # 监视并响应键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, 
                        continue_button, spaceship, aliens, bullets)
        # 游戏处于进行状态
        if stats.game_state == ai_settings.GAME_ACTIVE:
            stats.game_frame = (stats.game_frame + 1) % 240
            # 还没有开始播放音乐
            if not pygame.mixer.music.get_busy():
                # 导入并开始播放背景音乐
                pygame.mixer.music.load(ai_settings.bg_music)
                pygame.mixer.music.play(loops = 0, start = 0.0)
            # 音乐已经处于激活状态但是暂停中
            elif stats.music_paused == True:
                # 继续播放音乐
                pygame.mixer.music.unpause()
                stats.music_paused = False
            #print(stats.game_frame)
            gf.create_alien_group(ai_settings, screen, stats, aliens)
            # 更新飞船的状态
            spaceship.update()
            # 更新子弹的状态
            gf.update_bullets(ai_settings, screen, stats, sb, spaceship, 
                              aliens, bullets)
            # 更新外星人的状态（在更新子弹后）
            gf.update_aliens(ai_settings, screen, stats, sb, spaceship, aliens, 
                             bullets)
        # 游戏处于暂停状态
        elif stats.game_state == ai_settings.GAME_PAUSED:
            # 音乐还在播放
            if stats.music_paused == False:
                # 暂停播放音乐
                pygame.mixer.music.pause()
                stats.music_paused = True
        # 游戏处于等待（开始或重新开始）状态
        elif stats.game_state == ai_settings.GAME_READY:
            # 音乐还在播放
            if pygame.mixer.music.get_busy():
                # 停止播放音乐
                pygame.mixer.music.stop()
        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, spaceship, aliens, 
                         bullets, play_button, continue_button)
        
run_game()
