# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:34:34 2019

@author: Sherlock Holmes
"""

import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

"""发射子弹的控制函数"""
def fire_bullet(ai_settings, screen, spaceship, bullets):
    # 屏幕中的子弹数量不超过限制数量
    if len(bullets) < ai_settings.bullets_limit:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, spaceship)
        bullets.add(new_bullet)
     
"""计算每行可容纳多少个外星人"""
def get_number_aliens_x(ai_settings, alien_width):
    # 设置外星人出现的水平范围
    # 水平范围 = 屏幕宽度 - 2 * 外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 计算出一行能容纳的外星人数量
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

"""计算屏幕可容纳多少行外星人"""
def get_number_rows(ai_settings, spaceship_height, alien_height):
    # 设置外星人出现的垂直范围
    # 垂直范围 = 屏幕高度 - 3 * 外星人高度 - 飞船高度
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - spaceship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

"""创建一个外星人"""
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    # 外星人间距为外星人宽度
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

"""创建外星人群"""
def create_alien_group(ai_settings, screen, spaceship, aliens):
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, spaceship.rect.height, 
                                  alien.rect.height)
    # 创建多行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建第一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

"""监视并响应按下键盘按键事件"""
def check_keydown_events(event, ai_settings, screen, spaceship, bullets):
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
    # 空格
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, spaceship, bullets)

"""监视并响应松开键盘按键事件"""
def check_keyup_events(event, spaceship):
    # 左箭头
    if event.key == pygame.K_LEFT:
        # 飞船停止移动
        spaceship.moving_left = False
    # 右箭头
    if event.key == pygame.K_RIGHT:
        # 飞船停止移动
        spaceship.moving_right = False

"""监视并相应鼠标和键盘事件"""
def check_events(ai_settings, screen, stats, sb, play_button, spaceship, 
                 aliens, bullets):
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 键盘事件(按键按下)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                    event, ai_settings, screen, spaceship, bullets)
        # 键盘事件（按键松开）
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
        # 鼠标事件（鼠标按下）
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, 
                              spaceship, aliens, bullets, mouse_x, mouse_y)
    
"""在玩家单击Play按钮时开始游戏"""
def check_play_button(ai_settings, screen, stats, sb, play_button, spaceship,
                      aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.init_dynamic_settings()
        # 隐藏鼠标的光标
        pygame.mouse.set_visible(False)
        # 重置游戏的统计信息
        stats.reset_stats()
        stats.game_active = True
        # 重置显示的游戏的统计信息
        sb.draw_score()
        sb.draw_high_score()
        sb.draw_level()
        sb.draw_spaceships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人并让飞船居中
        create_alien_group(ai_settings, screen, spaceship, aliens)
        spaceship.place_center()
        
"""更新屏幕上的图像，并切换到新屏幕"""
def update_screen(ai_settings, screen, stats, sb, spaceship, aliens, bullets, 
                  play_button):
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
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
    if not stats.game_active:
        play_button.draw_button()
    # 显示最新绘制的屏幕
    pygame.display.flip()

"""更新子弹的位置，并删除已经消失的子弹"""
def update_bullets(ai_settings, screen, stats, sb, spaceship, aliens, bullets):
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
    
"""处理子弹和外星人的碰撞"""
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, spaceship, 
                                  aliens, bullets):
    # 第一个True表示若重叠，则删除子弹
    # 第二个True表示若重叠，则删除外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 子弹消灭外星人时，更新得分
    if collisions:
        # 对每个被消灭的外星人都记录得分
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.draw_score()
        check_high_score(stats, sb)
    
    # 当屏幕上所有的外星人都被消灭时，生成新的外星人群
    if len(aliens) == 0:
        # 删除现有的子弹，加快游戏节奏并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.draw_level()
        # 穿件新的外星人群
        create_alien_group(ai_settings, screen, spaceship, aliens)
    
"""有外星人到达边缘时采取相应的措施"""
def check_aliens_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_aliens_direction(ai_settings, aliens)
            break
        
"""将整群外星人的位置下移，并改变它们的方向"""
def change_aliens_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.alien_direction *= -1

"""处理被外星人撞到的飞船"""
def spaceship_hit(ai_settings, screen, stats, sb, spaceship, aliens, bullets):
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
        create_alien_group(ai_settings, screen, spaceship, aliens)
        spaceship.place_center()
        # 暂停0.5秒给玩家作为缓冲
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

"""检查是否有外星人到达屏幕的底端"""
def check_aliens_bottom(ai_settings, screen, stats, sb, spaceship, aliens, 
                        bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 按照飞船被撞到一样进行处理
            spaceship_hit(ai_settings, screen, stats, sb, spaceship, aliens, 
                          bullets)
            break

"""更新外星人群中所有外星人的位置"""
def update_aliens(ai_settings, screen, stats, sb, spaceship, aliens, bullets):
    # 检查是否有外星人位于屏幕边缘
    check_aliens_edges(ai_settings, aliens)
    aliens.update()
    
    # 检查外星人和飞船之间是否发生碰撞
    if pygame.sprite.spritecollideany(spaceship, aliens):
        spaceship_hit(ai_settings, screen, stats, sb, spaceship, aliens, 
                      bullets)
    # 检查是否有外星人到底屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, spaceship, aliens, 
                        bullets)

"""检查是否出现新的最高分"""
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.draw_high_score()
