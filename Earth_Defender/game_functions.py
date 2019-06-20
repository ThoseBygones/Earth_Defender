# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:34:34 2019

@author: Sherlock Holmes
"""

import sys
from time import sleep
import pygame
import random
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, spaceship, bullets):
    """发射子弹的控制函数"""
    # 屏幕中的子弹数量不超过限制数量
    if len(bullets) < ai_settings.bullets_limit:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, spaceship)
        bullets.add(new_bullet)
     
def create_alien(ai_settings, screen, aliens):
    """创建一个外星人"""
    alien = Alien(ai_settings, screen)
    # 计算外星人能出现的水平范围
    available_space_l = alien.rect.width
    available_space_r = ai_settings.screen_width - alien.rect.width
    # 外星人间距为外星人宽度
    alien.centerx = random.uniform(available_space_l, available_space_r)
    alien.rect.centerx = alien.centerx
    alien.rect.centery = 0 - alien.rect.height / 2
    aliens.add(alien)
    
def create_alien_group(ai_settings, screen, stats, aliens):
    """创建外星人编组"""
    # 按照一定频率创建外星人
    if stats.game_frame % 80 == 0:
        create_alien(ai_settings, screen, aliens)


def check_keydown_events(event, ai_settings, screen, stats, spaceship, 
                         bullets):
    """监视并响应按下键盘按键事件"""
    # 退出
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    # 左箭头
    if event.key == pygame.K_LEFT:
        # 飞船向左移动
        spaceship.moving_left = True
    # 右箭头
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动
        spaceship.moving_right = True
    # 上箭头
    if event.key == pygame.K_UP:
        # 飞船向上移动
        spaceship.moving_up = True
    # 下箭头
    if event.key == pygame.K_DOWN:
        # 飞船向下移动
        spaceship.moving_down = True
    # 空格
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, spaceship, bullets)
    # 回车
    if event.key == pygame.K_RETURN:
        pause_game(ai_settings, stats)

def check_keyup_events(event, spaceship):
    """监视并响应松开键盘按键事件"""
    # 左箭头
    if event.key == pygame.K_LEFT:
        # 飞船停止移动
        spaceship.moving_left = False
    # 右箭头
    if event.key == pygame.K_RIGHT:
        # 飞船停止移动
        spaceship.moving_right = False
    # 上箭头
    if event.key == pygame.K_UP:
        # 飞船向上移动
        spaceship.moving_up = False
    # 下箭头
    if event.key == pygame.K_DOWN:
        # 飞船向下移动
        spaceship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, continue_button, 
                 spaceship, aliens, bullets):
    """监视并相应鼠标和键盘事件"""
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 键盘事件(按键按下)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                    event, ai_settings, screen, stats, spaceship, bullets)
        # 键盘事件（按键松开）
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
        # 鼠标事件（鼠标按下）
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if stats.game_state == ai_settings.GAME_READY:
                check_play_button(ai_settings, screen, stats, sb, play_button, 
                                  spaceship, aliens, bullets, mouse_x, mouse_y)
            elif stats.game_state == ai_settings.GAME_PAUSED:
                check_continue_button(ai_settings, stats, sb, continue_button, 
                                      mouse_x, mouse_y)

def pause_game(ai_settings, stats):
    """暂停游戏"""
    stats.game_state = ai_settings.GAME_PAUSED
    pygame.mouse.set_visible(True)

def check_play_button(ai_settings, screen, stats, sb, play_button, spaceship,
                      aliens, bullets, mouse_x, mouse_y):
    """在玩家单击“开始游戏”按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_state == 0:
        # 重置游戏设置
        ai_settings.init_dynamic_settings()
        # 隐藏鼠标的光标
        pygame.mouse.set_visible(False)
        # 重置游戏的统计信息
        stats.reset_stats()
        stats.game_state = ai_settings.GAME_ACTIVE
        # 重置显示的游戏的统计信息
        sb.draw_score()
        sb.draw_high_score()
        sb.draw_level()
        sb.draw_spaceships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建新的外星人并让飞船居中
        create_alien_group(ai_settings, screen, stats, aliens)
        spaceship.place_center()

def check_continue_button(ai_settings, stats, sb, continue_button, 
                          mouse_x, mouse_y):
    """在玩家单击“继续游戏”按钮时开始游戏"""
    button_clicked = continue_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_state == ai_settings.GAME_PAUSED:
        # 隐藏鼠标的光标
        pygame.mouse.set_visible(False)
        stats.game_state = ai_settings.GAME_ACTIVE
        # 重置显示的游戏的统计信息
        sb.draw_score()
        sb.draw_high_score()
        sb.draw_level()
        sb.draw_spaceships()
      
def update_screen(ai_settings, screen, stats, sb, spaceship, aliens, bullets, 
                  play_button, continue_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 显示背景图片
    screen.blit(ai_settings.bg_image, (0, 0))
    # 在飞船和外星人之后重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    spaceship.blitme()
    # 绘制外星人群
    aliens.draw(screen)
    # 显示得分
    sb.show_score()
    # 如果游戏处于非活跃状态，就绘制Play按钮
    if stats.game_state == 0:
        screen.blit(ai_settings.ift_image, (0, 0))
        play_button.draw_button()
    elif stats.game_state == 2:
        continue_button.draw_button()
    # 显示最新绘制的屏幕
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, spaceship, aliens, bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
    # 检查是否有子弹击中了外星人。如果有，则删除相应的子弹和外星人
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, spaceship, 
                                  aliens, bullets)
    
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, spaceship, 
                                  aliens, bullets):
    """处理子弹和外星人的碰撞"""
    # 第一个True表示若重叠，则删除子弹
    # 第二个True表示若重叠，则删除外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 子弹消灭外星人时，更新得分
    if collisions:
        # 对每个被消灭的外星人都记录得分
        for aliens in collisions.values():
            kill_number = len(aliens)
            stats.score += ai_settings.alien_points * kill_number
            stats.kill_cnt += kill_number
            sb.draw_score()
        check_high_score(stats, sb)
    
    # 当消灭的外星人达到一定数量时，提升游戏等级
    if stats.kill_cnt == 20:
        stats.kill_cnt = 0
        # 删除现有的子弹，加快游戏节奏并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.draw_level()
        # 穿件新的外星人群
        create_alien_group(ai_settings, screen, stats, aliens)
    
def random_aliens_direction(aliens):
    """为每个外星人随机一个横向移动的方向"""
    for alien in aliens:
        alien.random_direction()
    
def check_aliens_edges(aliens):
    """让所有到达边缘的外星人变向"""
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.direction *= -1

def spaceship_hit(ai_settings, screen, stats, sb, spaceship, aliens, bullets):
    """处理被外星人撞到的飞船"""
    if stats.spaceship_cnt > 0:
        # 飞船被撞到，则飞船数减1
        stats.spaceship_cnt -= 1
        #print("Spaceship: " + str(stats.spaceship_cnt))
        # 更新得分板
        sb.draw_spaceships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将新的飞船放到屏幕底部中央
        create_alien(ai_settings, screen, aliens)
        spaceship.place_center()
        # 暂停0.5秒给玩家作为缓冲
        sleep(0.5)
    else:
        stats.game_state = ai_settings.GAME_READY
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(screen, aliens):
    """检查是否有外星人飞出屏幕的底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.top >= screen_rect.bottom:
            # 将飞出屏幕的外星人移除
            aliens.remove(alien)

def update_aliens(ai_settings, screen, stats, sb, spaceship, aliens, bullets):
    """更新外星人群中所有外星人的位置"""
    # 让每个外星人选择一个横向移动的方向
    random_aliens_direction(aliens)
    # 检查是否有外星人位于屏幕边缘
    check_aliens_edges(aliens)
    aliens.update()
    
    # 检查外星人和飞船之间是否发生碰撞
    if pygame.sprite.spritecollideany(spaceship, aliens):
        spaceship_hit(ai_settings, screen, stats, sb, spaceship, aliens, 
                      bullets)
    # 检查是否有外星人到底屏幕底端
    check_aliens_bottom(screen, aliens)

def check_high_score(stats, sb):
    """检查是否出现新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.draw_high_score()
