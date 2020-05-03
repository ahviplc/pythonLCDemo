from platform import system

_system = system()

if _system == 'Windows':
    from .player import WinPlayer as Player
elif _system == 'Darwin':
    from .player import OSXPlayer as Player
else:
    #from .player import NixPlayer as Player
    raise NotImplemented(f'暂不支持该操作系统: {_system}')

del _system
