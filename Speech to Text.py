# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 01:48:33 2023
@author: EKWUGHA NNAEMEKA THANKGOD
"""

import speech_recognition as sr
from time import sleep

# Instantiation of the Recognizer class
r = sr.Recognizer()

audfile = sr.AudioFile("nnaemeka.wav")
with audfile as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    sleep(5)
    Data = r.record(source)

try:
    print("Transcription Process...")
    sleep(5)
    transcribed = r.recognize_google(Data, language="en-USA")
except Exception as error:
    print(f"An error occurred during the processing, {error}")

print("\n\n")
print("||||||||||TRANSCRIPTION||||||||||\n")
print(transcribed)
