import abc
import time
import os
from concurrent.futures import ThreadPoolExecutor

from .errors import PlayException


class Player(abc.ABC):
    file_format = 'mp3'
    BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'res', 'sound')

    @abc.abstractmethod
    def _play_sound(cls, file, playing_time=None):
        """
        播放音频
        :param file: 音频文件
        :param playing_time: 播放时长（秒）, 默认完整播放
        :return: None
        """
        pass

    @classmethod
    def play(cls, tone, playing_time=None, show_log=True):
        """
        播放钢琴音源文件
        :param tone: 音调（A0-G7）
        :param playing_time: 播放时长（秒），默认完整播放
        :param show_log: 是否显示日志
        """
        if show_log:
            print(f'[{time.strftime("%F %T")}] {tone}')
        cls._play_sound(os.path.join(cls.BASE_DIR, f'{tone}.{cls.file_format}'), playing_time)

    @classmethod
    def play_many(cls, tone_list):
        with ThreadPoolExecutor() as pool:
            for tone in tone_list:
                pool.submit(cls.play(*tone))


class WinPlayer(Player):
    @classmethod
    def _play_sound(cls, file, playing_time=None):
        """
        Utilizes windll.winmm. Tested and known to work with MP3 and WAVE on
        Windows 7 with Python 2.7. Probably works with more file formats.
        Probably works on Windows XP thru Windows 10. Probably works with all
        versions of Python.
        Inspired by (but not copied from) Michael Gundlach <gundlach@gmail.com>'s mp3play:
        https://github.com/michaelgundlach/mp3play
        I never would have tried using windll.winmm without seeing his code.
        """
        from ctypes import c_buffer
        from ctypes import windll
        from random import random
        from sys import getfilesystemencoding

        def win_command(*command):
            buf = c_buffer(255)
            command = ' '.join(command).encode(getfilesystemencoding())
            error_code = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
            if error_code:
                error_buffer = c_buffer(255)
                windll.winmm.mciGetErrorStringA(error_code, error_buffer, 254)
                raise PlayException(f'\n\tError {error_code} for command:\n'
                                    f'\t\t{command.decode()}\n'
                                    f'\t{error_buffer.value.decode()}')
            return buf.value

        alias = 'playsound_' + str(random())
        win_command(f'open "{file}" alias', alias)
        win_command('set', alias, 'time format milliseconds')
        # 获取音频时长（毫秒）
        duration = win_command('status', alias, 'length')
        win_command('play', alias, 'from 0 to', duration.decode())

        if playing_time is None:
            time.sleep(float(duration) / 1000)
        else:
            time.sleep(playing_time)


class OSXPlayer(Player):
    @classmethod
    def _play_sound(cls, file, playing_time=None):
        """
        Utilizes AppKit.NSSound. Tested and known to work with MP3 and WAVE on
        OS X 10.11 with Python 2.7. Probably works with anything QuickTime supports.
        Probably works on OS X 10.5 and newer. Probably works with all versions of
        Python.
        Inspired by (but not copied from) Aaron's Stack Overflow answer here:
        http://stackoverflow.com/a/34568298/901641
        I never would have tried using AppKit.NSSound without seeing his code.
        """
        from AppKit import NSSound
        from Foundation import NSURL

        if '://' not in file:
            if not file.startswith('/'):
                from os import getcwd
                file = f'{getcwd()}/{file}'
            file = f'file://{file}'

        nssound = NSSound.alloc().initWithContentsOfURL_byReference_(NSURL.URLWithString_(file), True)
        if not nssound:
            raise IOError(f'Unable to load sound named: {file}')
        nssound.play()

        if playing_time is None:
            time.sleep(nssound.duration())
        else:
            time.sleep(playing_time)


# class NixPlayer(Player):
#     @classmethod
#     def _play_sound(cls, file, playing_time=None):
#         """
#         Play a sound using GStreamer.
#         Inspired by this:
#         https://gstreamer.freedesktop.org/documentation/tutorials/playback/playbin-usage.html
#         """
#         if not block:
#             raise NotImplementedError("block=False cannot be used on this platform yet")
#
#         # pathname2url escapes non-URL-safe characters
#         import os
#         try:
#             from urllib.request import pathname2url
#         except ImportError:
#             # python 2
#             from urllib import pathname2url
#
#         import gi
#         gi.require_version('Gst', '1.0')
#         from gi.repository import Gst
#
#         Gst.init(None)
#
#         playbin = Gst.ElementFactory.make('playbin', 'playbin')
#         if sound.startswith(('http://', 'https://')):
#             playbin.props.uri = sound
#         else:
#             playbin.props.uri = 'file://' + pathname2url(os.path.abspath(sound))
#
#         set_result = playbin.set_state(Gst.State.PLAYING)
#         if set_result != Gst.StateChangeReturn.ASYNC:
#             raise PlaysoundException("playbin.set_state returned " + repr(set_result))
#
#         # FIXME: use some other bus method than poll() with block=False
#         # https://lazka.github.io/pgi-docs/#Gst-1.0/classes/Bus.html
#         bus = playbin.get_bus()
#         bus.poll(Gst.MessageType.EOS, Gst.CLOCK_TIME_NONE)
#         playbin.set_state(Gst.State.NULL)
