import sys
import os

# pythonLCDemo下的com/lc/demo/pianoPlayerDemo
# pythonLCDemo/com/lc/demo/pianoPlayerDemo
# 将此路径加入系统路径 此路径下piano_player的包才可被找到
sys.path.append(os.path.abspath('..'))
# 下面这个引入才可用
from piano_player import Player

music = [
    ('A0', 0.125), ('B0', 0.125),
    ('C1', 0.125), ('D1', 0.125), ('E1', 0.125), ('F1', 0.125), ('G1', 0.125), ('A1', 0.125), ('B1', 0.125),
    ('C2', 0.125), ('D2', 0.125), ('E2', 0.125), ('F2', 0.125), ('G2', 0.125), ('A2', 0.125), ('B2', 0.125),
    ('C3', 0.125), ('D3', 0.125), ('E3', 0.125), ('F3', 0.125), ('G3', 0.125), ('A3', 0.125), ('B3', 0.125),
    ('C4', 0.125), ('D4', 0.125), ('E4', 0.125), ('F4', 0.125), ('G4', 0.125), ('A4', 0.125), ('B4', 0.125),
    ('C5', 0.125), ('D5', 0.125), ('E5', 0.125), ('F5', 0.125), ('G5', 0.125), ('A5', 0.125), ('B5', 0.125),
    ('C6', 0.125), ('D6', 0.125), ('E6', 0.125), ('F6', 0.125), ('G6', 0.125), ('A6', 0.125), ('B6', 0.125),
    ('C7', 0.125), ('D7', 0.125), ('E7', 0.125), ('F7', 0.125), ('G7', 0.125), ('A7', 0.125), ('B7', 0.125),
    ('C8', 0.125),
]
music += reversed(music)

Player.play_many(music)
