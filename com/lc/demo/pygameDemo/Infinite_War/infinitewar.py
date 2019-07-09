#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
infinitewar.py
飞机大战 小游戏
Version: 1.0
Author: LC
DateTime: 2019年7月9日14:20:57
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""

from pygame.sprite import *
from pygame import *
from random import *
from sys import *


class game_plane():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.plane_image = image.load('images/plane.png')
        self.rect = self.plane_image.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.act_up = False
        self.act_down = False
        self.act_right = False
        self.act_left = False
        self.act_fire = False
        self.draw_plane_active = True

    def plane_move(self):
        if self.act_up and self.rect.top >= 0:
            self.rect.y -= 5
        if self.act_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += 5
        if self.act_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += 5
        if self.act_left and self.rect.left >= 0:
            self.rect.x -= 5

    def draw_plane(self):
        if self.draw_plane_active:
            self.screen.blit(self.plane_image, self.rect)

    def reset_plane_position(self):
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx


class game_plane_bullet(Sprite):
    def __init__(self, screen, plane):
        super().__init__()
        self.screen = screen
        self.plane_bullet_image = image.load('images/plane_bullet.png')
        self.rect = self.plane_bullet_image.get_rect()
        self.rect.top = plane.rect.top
        self.rect.centerx = plane.rect.centerx

    def draw_plane_bullet(self, time, plane_bullet_group, plane, screen):
        if plane.act_fire and time % 15 == 0:
            plane_bullet = game_plane_bullet(screen, plane)
            plane_bullet_group.add(plane_bullet)
        for every_plane_bullet in plane_bullet_group.sprites():
            every_plane_bullet.rect.y -= 10
            if every_plane_bullet.rect.bottom <= 0:
                plane_bullet_group.remove(every_plane_bullet)
            self.screen.blit(every_plane_bullet.plane_bullet_image, every_plane_bullet.rect)


class game_red_enemy(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.red_enemy_image = image.load('images/red_enemy.png')
        self.rect = self.red_enemy_image.get_rect()
        self.rect.bottom = self.screen_rect.top
        self.rect.left = randint(0, 800 - 128)

    def draw_red_enemy(self, red_enemy_group, score, screen, time, level):
        if time % (70 - (2 * level.level)) == 0:
            red_enemy = game_red_enemy(screen)
            red_enemy_group.add(red_enemy)
        for every_red_enemy in red_enemy_group.sprites():
            every_red_enemy.rect.y += (1.9 + (0.2 * level.level))
            if every_red_enemy.rect.bottom >= self.screen_rect.bottom:
                red_enemy_group.remove(every_red_enemy)
                score.score -= 50
            self.screen.blit(every_red_enemy.red_enemy_image, every_red_enemy.rect)


class game_blue_enemy(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.blue_enemy_image = image.load('images/blue_enemy.png')
        self.rect = self.blue_enemy_image.get_rect()
        self.rect.bottom = self.screen_rect.top
        self.rect.left = randint(0, 800 - 128)

    def draw_blue_enemy(self, blue_enemy_group, score, screen, time, level):
        if time % (50 - (2 * level.level)) == 0:
            blue_enemy = game_blue_enemy(screen)
            blue_enemy_group.add(blue_enemy)
        for every_blue_enemy in blue_enemy_group.sprites():
            every_blue_enemy.rect.y += (0.9 + (0.2 * level.level))
            if every_blue_enemy.rect.bottom >= self.screen_rect.bottom:
                blue_enemy_group.remove(every_blue_enemy)
                score.score -= 25
            self.screen.blit(every_blue_enemy.blue_enemy_image, every_blue_enemy.rect)


class game_enemy_bullet(Sprite):
    def __init__(self, screen, enemy_bullet_group, red_enemy_group):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.enemy_bullet_image = image.load('images/enemy_bullet.png')
        self.rect = self.enemy_bullet_image.get_rect()
        for every_red_enemy in red_enemy_group.sprites():
            self.rect.bottom = every_red_enemy.rect.bottom
            self.rect.centerx = every_red_enemy.rect.centerx

    def draw_enemy_bullet(self, time, enemy_bullet_group, screen, red_enemy_group, level):
        if time % 75 == 0:
            enemy_bullet = game_enemy_bullet(screen, enemy_bullet_group, red_enemy_group)
            enemy_bullet_group.add(enemy_bullet)
        for every_enemy_bullet in enemy_bullet_group.sprites():
            every_enemy_bullet.rect.y += (3 + (0.2 * level.level))
            if every_enemy_bullet.rect.bottom >= self.screen_rect.bottom:
                enemy_bullet_group.remove(every_enemy_bullet)
            self.screen.blit(every_enemy_bullet.enemy_bullet_image, every_enemy_bullet.rect)


class game_sound():
    def __init__(self):
        self.bgm = 'sound/bgm.mp3'

    def play_sound(self):
        mixer.music.load(self.bgm)
        mixer.music.set_volume(0.5)


class game_score():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score = 0
        self.draw_score()

    def draw_score(self):
        self.score_font = font.SysFont('arial', 50)
        self.score_format = '{:,}'.format(int(round(self.score, -1)))
        self.score_image = self.score_font.render(self.score_format, True, (255, 255, 255))
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.bottom = self.screen_rect.bottom - 20
        self.screen.blit(self.score_image, self.score_image_rect)
        self.score_txt_image = self.score_font.render('Score ', True, (255, 255, 255))
        self.score_txt_image_rect = self.score_txt_image.get_rect()
        self.score_txt_image_rect.right = self.score_image_rect.left
        self.score_txt_image_rect.centery = self.score_image_rect.centery
        self.screen.blit(self.score_txt_image, self.score_txt_image_rect)


class game_level():
    def __init__(self, screen, score):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.level = 1
        self.draw_level(score)

    def draw_level(self, score):
        self.level_font = font.SysFont('arial', 50)
        self.level_image = self.level_font.render(str(self.level), True, (255, 255, 255))
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.screen_rect.right - 20
        self.level_image_rect.bottom = score.score_image_rect.top - 20
        self.screen.blit(self.level_image, self.level_image_rect)
        self.level_txt_image = self.level_font.render('Level ', True, (255, 255, 255))
        self.level_txt_image_rect = self.level_txt_image.get_rect()
        self.level_txt_image_rect.right = self.level_image_rect.left
        self.level_txt_image_rect.centery = self.level_image_rect.centery
        self.screen.blit(self.level_txt_image, self.level_txt_image_rect)


class game_attack():
    def __init__(self, screen, level):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.attack_font = font.SysFont('arial', 40)
        self.attack_index_font = font.SysFont('arial', 70)
        self.times = 0
        self.draw_attack(level)

    def draw_attack(self, level):
        if self.times > 0:
            self.times_image = self.attack_index_font.render(str(self.times), True, (255, 165, 0))
            self.times_image_rect = self.times_image.get_rect()
            self.times_image_rect.right = self.screen_rect.right - 20
            self.times_image_rect.bottom = level.level_image_rect.top - 20
            self.screen.blit(self.times_image, self.times_image_rect)
            self.attack_image = self.attack_font.render('Under Attack! x ', True, (255, 255, 255))
            self.attack_image_rect = self.attack_image.get_rect()
            self.attack_image_rect.right = self.times_image_rect.left
            self.attack_image_rect.centery = self.times_image_rect.centery
            self.screen.blit(self.attack_image, self.attack_image_rect)


class game_background():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.background_image_1 = image.load('images/background.png')
        self.background_image_rect_1 = self.background_image_1.get_rect()
        self.background_image_rect_1.top = 0
        self.background_image_2 = image.load('images/background.png')
        self.background_image_rect_2 = self.background_image_2.get_rect()
        self.background_image_rect_2.top = -self.screen_rect.bottom

    def draw_background(self):
        self.background_image_rect_1.y += 1
        if self.background_image_rect_1.top >= self.screen_rect.bottom:
            self.background_image_rect_1.top = 0
        self.screen.blit(self.background_image_1, self.background_image_rect_1)
        self.background_image_rect_2.y += 1
        if self.background_image_rect_2.top >= 0:
            self.background_image_rect_2.top = -self.screen_rect.bottom
        self.screen.blit(self.background_image_2, self.background_image_rect_2)


def check_event(time, plane, screen, score):
    if not mixer.music.get_busy():
        mixer.music.play()
    mouse.set_visible(False)
    for game_event in event.get():
        if game_event.type == QUIT:
            exit()
        if game_event.type == KEYDOWN:
            if game_event.key == K_ESCAPE:
                exit()
            if game_event.key == K_p:
                check_pause(screen, score, pause_active=True)
            if game_event.key == K_UP:
                plane.act_up = True
            if game_event.key == K_DOWN:
                plane.act_down = True
            if game_event.key == K_RIGHT:
                plane.act_right = True
            if game_event.key == K_LEFT:
                plane.act_left = True
            if game_event.key == K_f:
                plane.act_fire = True
        if game_event.type == KEYUP:
            if game_event.key == K_UP:
                plane.act_up = False
            if game_event.key == K_DOWN:
                plane.act_down = False
            if game_event.key == K_RIGHT:
                plane.act_right = False
            if game_event.key == K_LEFT:
                plane.act_left = False
            if game_event.key == K_f:
                plane.act_fire = False


def plane_bullet_collide_enemy(plane_bullet_group, red_enemy_group, blue_enemy_group, score):
    plane_bullet_red_enemy_collision = sprite.groupcollide(plane_bullet_group, red_enemy_group, True, True)
    if plane_bullet_red_enemy_collision:
        for red_enemy_group in plane_bullet_red_enemy_collision.values():
            score.score += 150 * len(red_enemy_group)
            score.draw_score()
    plane_bullet_blue_enemy_collision = sprite.groupcollide(plane_bullet_group, blue_enemy_group, True, True)
    if plane_bullet_blue_enemy_collision:
        for blue_enemy_group in plane_bullet_blue_enemy_collision.values():
            score.score += 75 * len(blue_enemy_group)
            score.draw_score()


def enemy_bullet_collide_plane(plane, enemy_bullet_group, score, attack, level):
    if sprite.spritecollideany(plane, enemy_bullet_group):
        attack.times += 1
        attack.draw_attack(level)
        score.score -= 50
        score.draw_score()
        plane.reset_plane_position()


def plane_collide_blue_enemy(plane, blue_enemy_group, score, attack, level):
    if sprite.spritecollideany(plane, blue_enemy_group):
        attack.times += 1
        attack.draw_attack(level)
        score.score -= 75
        score.draw_score()
        plane.reset_plane_position()


def plane_collide_red_enemy(plane, red_enemy_group, score, attack, level):
    if sprite.spritecollideany(plane, red_enemy_group):
        attack.times += 1
        attack.draw_attack(level)
        score.score -= 100
        score.draw_score()
        plane.reset_plane_position()


def upgrade_level(time, level, score):
    if time % 500 == 0:
        level.level += 1
        level.draw_level(score)


def defeat(screen, score, sound, plane):
    if score.score < -1:
        defeat_image = image.load('images/defeat.png')
        defeat_image_rect = defeat_image.get_rect()
        screen_rect = screen.get_rect()
        defeat_image_rect.centerx = screen_rect.centerx
        defeat_image_rect.centery = screen_rect.centery
        screen.blit(defeat_image, defeat_image_rect)
        mixer.music.set_volume(0)
        plane.act_up = False
        plane.act_down = False
        plane.act_right = False
        plane.act_left = False
        plane.act_fire = False
        plane.draw_plane_active = False
        exit()


def check_pause(screen, score, pause_active=False):
    screen_rect = screen.get_rect()
    pause_font = font.SysFont('arial', 100)
    press_font = font.SysFont('arial', 50)
    pause_image = pause_font.render('Pause', True, (255, 165, 0))
    pause_image_rect = pause_image.get_rect()
    pause_image_rect.centerx = screen_rect.centerx
    pause_image_rect.centery = screen_rect.centery
    press_image = press_font.render('Press any key(Except Key:Esc)to continue', True, (255, 255, 255))
    press_image_rect = press_image.get_rect()
    press_image_rect.centerx = screen_rect.centerx
    press_image_rect.top = pause_image_rect.bottom
    while pause_active:
        if score.score >= 0:
            screen.blit(pause_image, pause_image_rect)
            screen.blit(press_image, press_image_rect)
        display.flip()
        for game_event in event.get():
            if game_event.type == QUIT:
                exit()
            if game_event.type == KEYDOWN:
                if game_event.key == K_ESCAPE:
                    exit()
                else:
                    pause_active = False


def run_game():
    time = 0
    init()
    mixer.init()
    screen = display.set_mode((800, 1000))
    display.set_caption('Infinite War -By LC')
    background = game_background(screen)
    score = game_score(screen)
    level = game_level(screen, score)
    sound = game_sound()
    plane = game_plane(screen)
    plane_bullet = game_plane_bullet(screen, plane)
    plane_bullet_group = Group()
    red_enemy = game_red_enemy(screen)
    red_enemy_group = Group()
    enemy_bullet_group = Group()
    enemy_bullet = game_enemy_bullet(screen, enemy_bullet_group, red_enemy_group)
    blue_enemy = game_blue_enemy(screen)
    blue_enemy_group = Group()
    attack = game_attack(screen, level)
    sound.play_sound()
    while True:
        time += 1
        plane_bullet_collide_enemy(plane_bullet_group, red_enemy_group, blue_enemy_group, score)
        enemy_bullet_collide_plane(plane, enemy_bullet_group, score, attack, level)
        plane_collide_blue_enemy(plane, blue_enemy_group, score, attack, level)
        plane_collide_red_enemy(plane, red_enemy_group, score, attack, level)
        background.draw_background()
        enemy_bullet.draw_enemy_bullet(time, enemy_bullet_group, screen, red_enemy_group, level)
        red_enemy.draw_red_enemy(red_enemy_group, score, screen, time, level)
        blue_enemy.draw_blue_enemy(blue_enemy_group, score, screen, time, level)
        plane.plane_move()
        plane.draw_plane()
        plane_bullet.draw_plane_bullet(time, plane_bullet_group, plane, screen)
        score.draw_score()
        level.draw_level(score)
        attack.draw_attack(level)
        upgrade_level(time, level, score)
        check_event(time, plane, screen, score)
        defeat(screen, score, sound, plane)
        check_pause(screen, score, pause_active=False)
        display.flip()


if __name__ == '__main__':
    run_game()
