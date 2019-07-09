#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Tetris_75rows.py
俄罗斯方块 小游戏
Version: 1.0
Author: LC
DateTime: 2019年7月9日14:29:00
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

# Python Pygame 俄罗斯方块(Tetris)
# 运行需要安装pygame模块

"""

import pygame, sys, random, time

block_initial_position, score, times, gameover, press, all_block, background = [20, 5], [0], 0, [], False, [
    [[0, 0], [0, -1], [0, 1], [0, 2]], [[0, 0], [0, 1], [-1, 1], [-1, 0]], [[0, 0], [0, -1], [-1, 0], [-1, 1]],
    [[0, 0], [0, 1], [-1, -1], [-1, 0]], [[0, 0], [0, 1], [1, 0], [0, -1]], [[0, 0], [1, 0], [-1, 0], [1, -1]],
    [[0, 0], [1, 0], [-1, 0], [1, 1]]], [[0 for column in range(0, 10)] for row in range(0, 22)]
background[0], select_block = [1 for column in range(0, 10)], list(random.choice(all_block))


def new_draw():
    for row, column in select_block:
        row += block_initial_position[0]
        column += block_initial_position[1]
        pygame.draw.rect(screen, (255, 165, 0), (column * 25, 500 - row * 25, 23, 23))
    for row in range(0, 20):
        for column in range(0, 10):
            if background[row][column]: pygame.draw.rect(screen, (0, 0, 255), (column * 25, 500 - row * 25, 23, 23))


def move_left_right(n):
    y_drop, x_move = block_initial_position
    x_move += n
    for row, column in select_block:
        row += y_drop
        column += x_move
        if column < 0 or column > 9 or background[row][column]: break
    else:
        block_initial_position.clear(), block_initial_position.extend([y_drop, x_move])


def rotate():
    rotating_position = [(-column, row) for row, column in select_block]
    for row, column in rotating_position:
        row += block_initial_position[0]
        column += block_initial_position[1]
        if column < 0 or column > 9 or background[row][column]: break
    else:
        select_block.clear(), select_block.extend(rotating_position)


def move_down():
    y_drop, x_move = block_initial_position
    y_drop -= 1
    for row, column in select_block:
        row += y_drop
        column += x_move
        if background[row][column] == 1: break
    else:
        block_initial_position.clear()
        block_initial_position.extend([y_drop, x_move])
        return
    for row, column in select_block: background[block_initial_position[0] + row][block_initial_position[1] + column] = 1
    complete_row = []
    for row in range(1, 21):
        if 0 not in background[row]: complete_row.append(row)
    complete_row.sort(reverse=True)
    for row in complete_row:
        background.pop(row)
        background.append([0 for column in range(0, 10)])
    score[0] += len(complete_row)
    pygame.display.set_caption('Tetris,Score:' + str(score[0]) + ' LC')
    select_block.clear()
    select_block.extend(list(random.choice(all_block)))
    block_initial_position.clear()
    block_initial_position.extend([20, 4])
    for row, column in select_block:
        row += block_initial_position[0]
        column += block_initial_position[1]
        if background[row][column]: gameover.append(1)


pygame.init()
screen = pygame.display.set_mode((250, 500))
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move_left_right(-1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move_left_right(1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            rotate()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            press = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            press = False
    if press: times += 10
    if times >= 50:
        move_down()
        times = 0
    else:
        times += 1
    if gameover: sys.exit()
    new_draw()
    pygame.time.Clock().tick(200)
    pygame.display.flip()
