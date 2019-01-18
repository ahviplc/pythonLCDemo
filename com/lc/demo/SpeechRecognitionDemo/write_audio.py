#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
write_audio.py
麦克风的使用
使用 SpeechRecognition 软件包——一个功能全面且易于使用的 Python 语音识别库。
Version: 1.0
Author: LC
DateTime: 2019年1月18日11:36:41
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

# 若系统没有默认麦克风（如在 RaspberryPi 上）或想要使用非默认麦克风，则需要通过提供设备索引来指定要使用的麦克风。读者可通过调用 Microphone 类的list_microphone_names（）函数来获取麦克风名称列表。
# print(sr.Microphone.list_microphone_names())
# for sml in sr.Microphone.list_microphone_names():
#     print(sml)

# 此时将使用默认系统麦克风，而不是使用音频文件作为信号源。读者可通过创建一个Microphone 类的实例来访问它。
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a RAW file
with open("write_audio_microphone-results.raw", "wb") as f:
    f.write(audio.get_raw_data())

# write audio to a WAV file
with open("write_audio_microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# write audio to an AIFF file
with open("write_audio_microphone-results.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

# write audio to a FLAC file
with open("write_audio_microphone-results.flac", "wb") as f:
    f.write(audio.get_flac_data())
