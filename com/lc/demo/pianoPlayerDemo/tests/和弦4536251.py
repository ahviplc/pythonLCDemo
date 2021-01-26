import sys
import os

# pythonLCDemo下的com/lc/demo/pianoPlayerDemo
# pythonLCDemo/com/lc/demo/pianoPlayerDemo
# 将此路径加入系统路径 此路径下piano_player的包才可被找到
sys.path.append(os.path.abspath('..'))
# 下面这个引入才可用
from piano_player import Player

sheet_music = [
    ('F3', 0.001), ('A3', 0.001), ('C4', 1),  # 4和弦
    ('F3', 0.001), ('A3', 0.001), ('C4', 1),  # 4和弦
    ('G3', 0.001), ('B3', 0.001), ('D4', 1),  # 5
    ('G3', 0.001), ('B3', 0.001), ('D4', 1),  # 5
    ('E3', 0.001), ('G3', 0.001), ('B3', 1),  # 3
    ('E3', 0.001), ('G3', 0.001), ('B3', 1),  # 3
    ('A3', 0.001), ('C4', 0.001), ('E4', 1),  # 6
    ('A3', 0.001), ('C4', 0.001), ('E4', 1),  # 6
    ('D3', 0.001), ('F3', 0.001), ('A3', 1),  # 2
    ('D3', 0.001), ('F3', 0.001), ('A3', 1),  # 2
    ('G3', 0.001), ('B3', 0.001), ('D4', 1),  # 5
    ('G3', 0.001), ('B3', 0.001), ('D4', 1),  # 5
    ('C4', 0.001), ('E4', 0.001), ('G4', 1),  # 1
    ('C4', 0.001), ('E4', 0.001), ('G4', 1),  # 1
    ('C4', 0.5), ('E4', 0.5), ('G4', 2),  # 1
]

Player.play_many(sheet_music)
