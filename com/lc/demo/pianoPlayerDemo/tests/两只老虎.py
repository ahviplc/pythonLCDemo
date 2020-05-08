import sys

print(sys.path)
# ['C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc\\demo\\pianoPlayerDemo\\tests', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\plugins\\python\\helpers\\pycharm_display', 'D:\\Python37\\python37.zip', 'D:\\Python37\\DLLs', 'D:\\Python37\\lib', 'D:\\Python37', 'D:\\Python37\\lib\\site-packages', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend']

sys.path.append(r'C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demo\pianoPlayerDemo')

'''python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中'''

print(sys.path)
# ['C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc\\demo\\pianoPlayerDemo\\tests', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\plugins\\python\\helpers\\pycharm_display', 'D:\\Python37\\python37.zip', 'D:\\Python37\\DLLs', 'D:\\Python37\\lib', 'D:\\Python37', 'D:\\Python37\\lib\\site-packages', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend', 'C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc\\demo\\pianoPlayerDemo']

# pythonLCDemo下的com/lc/demo/pianoPlayerDemo

from piano_player import Player

# 设置曲谱
sheet_music = (
    ('C4', 0.5), ('D4', 0.5), ('E4', 0.5), ('C4', 0.5),  # 两只老虎
    ('C4', 0.5), ('D4', 0.5), ('E4', 0.5), ('C4', 0.5),  # 两只老虎
    ('E4', 0.5), ('F4', 0.5), ('G4', 1),  # 跑得快
    ('E4', 0.5), ('F4', 0.5), ('G4', 1),  # 跑得快
    ('G4', 0.25), ('A4', 0.25), ('G4', 0.25), ('F4', 0.25), ('E4', 0.5), ('C4', 0.5),  # 一只没有耳朵
    ('G4', 0.25), ('A4', 0.25), ('G4', 0.25), ('F4', 0.25), ('E4', 0.5), ('C4', 0.5),  # 一只没有尾巴
    ('D4', 0.5), ('G3', 0.5), ('C4', 1),  # 真奇怪
    ('D4', 0.5), ('G3', 0.5), ('C4', 1)  # 真奇怪
)

Player.play_many(sheet_music)
