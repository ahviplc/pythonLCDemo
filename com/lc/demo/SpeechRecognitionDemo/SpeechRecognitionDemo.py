#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SpeechRecognitionDemo.py
使用 SpeechRecognition 软件包——一个功能全面且易于使用的 Python 语音识别库。
Version: 1.0
Author: LC
DateTime: 2019年1月18日10:21:47
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import speech_recognition as sr

# 指定要转换的音频源文件（english.wav）
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio_files\\harvard.wav")
"""
this they'll smell of old we're lingers it takes heat to bring out the odor called it restores health and zest case all the colt is fine with him couples all pastore my favorite is as full food is the hot cross mon

"""

CHINESE_AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio_files\\chinese.flac")
"""
traffic atm
其实是:砸自己的脚
"""

ENGLISH_AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio_files\\english.wav")
"""
one two three
"""

# 定义SpeechRecognition对象并获取音频源文件（harvard.wav）中的数据
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file  # 获取前四秒的内容:audio = r.record(source, duration=4)

# print(type(audio))  # <class 'speech_recognition.AudioData'>

# 使用CMU Sphinx引擎去识别音频

# print(r.recognize_sphinx(audio, show_all=True))

try:
    print("Sphinx thinks you said: \n" + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

with sr.AudioFile(CHINESE_AUDIO_FILE) as source:
    chinese_audio = r.record(source)  # read the entire audio file

# 使用CMU Sphinx引擎去识别音频-中文
try:
    print("Sphinx thinks you said 中文: \n" + r.recognize_sphinx(chinese_audio))

# r.recognize_sphinx(chinese_audio,language='zh-CN')
# 则报错:
# Sphinx error 中文;missing PocketSphinx language data directory:
# "E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\venv\lib\site-packages\speech_recognition\pocketsphinx-data\zh-CN"

except sr.UnknownValueError:
    print("Sphinx could not understand audio 中文")
except sr.RequestError as e:
    print("Sphinx error 中文; {0}".format(e))

# # 使用recognize_google引擎去识别音频
# try:
#     print("google thinks you said: \n" + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("google could not understand audio")
# except sr.RequestError as e:
#     print("google error; {0}".format(e))

# # 使用Microsoft Bing Voice Recognition引擎去识别音频
# BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said: \n" + r.recognize_bing(audio, key=BING_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))


# 使用其他引擎去识别音频
# ... ...


# 识别器类
# SpeechRecognition 的核心就是识别器类。
#
# Recognizer API 主要目是识别语音，每个 API 都有多种设置和功能来识别音频源的语音，分别是：
#
# recognize_bing(): Microsoft Bing Speech
# recognize_google(): Google Web Speech API
# recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
# recognize_houndify(): Houndify by SoundHound
# recognize_ibm(): IBM Speech to Text
# recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
# recognize_wit(): Wit.ai
# 以上七个中只有 recognition_sphinx（）可与CMU Sphinx 引擎脱机工作， 其他六个都需要连接互联网。
#
# SpeechRecognition 附带 Google Web Speech API 的默认 API 密钥，可直接使用它。其他六个 API 都需要使用 API 密钥或用户名/密码组合进行身份验证，因此本文使用了 Web Speech API。
#
# 这 7 个 recognize_*()  识别器类都需要输入 audio_data 参数，且每种识别器的 audio_data 都必须是 SpeechRecognition 的 AudioData 类的实例。
#
# AudioData 实例的创建有两种路径：音频文件或由麦克风录制的音频，先从比较容易上手的音频文件开始。
#
# 音频文件的使用
# 首先需要下载音频文件（https://github.com/realpython/python-speech-recognition/tree/master/audio_files），保存到 Python 解释器会话所在的目录中。
#
# AudioFile 类可以通过音频文件的路径进行初始化，并提供用于读取和处理文件内容的上下文管理器界面。
#
#
#
# 支持文件类型
# SpeechRecognition 目前支持的文件类型有：
#
# WAV: 必须是 PCM/LPCM 格式
#
# AIFF
#
# AIFF-C
#
# FLAC: 必须是初始 FLAC 格式；OGG-FLAC 格式不可用
#
# 若是使用 Linux 系统下的 x-86 ，macOS 或者是 Windows 系统，需要支持 FLAC文件。若在其它系统下运行，需要安装 FLAC 编码器并确保可以访问 flac 命令。
#
# 麦克风的使用
# 若要使用 SpeechRecognizer 访问麦克风则必须安装 PyAudio 软件包。
# Windows
# Windows 用户可直接调用 pip 来安装 PyAudio。
# $ pip install pyaudio

# pyaudio安装测试
# 安装了 PyAudio 后可从控制台进行安装测试。
#
# $ python -m speech_recognition
# 请确保默认麦克风打开并取消静音，若安装正常则应该看到如下所示的内容：
#
# (venv) E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\com\lc\demo\SpeechRecognitionDemo> python -m speech_recognition
# A moment of silence, please...
# Set minimum energy threshold to 45.43250699217339
# Say something!
# Got it! Now to recognize it...
# Uh oh! Couldn't request results from Google Speech Recognition service; recognition connection failed: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
