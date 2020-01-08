import os

from pydub import AudioSegment
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

sounds = {
    '1': AudioSegment.from_wav(f'{dir_path}/sounds/1.wav'),
    '2': AudioSegment.from_wav(f'{dir_path}/sounds/2.wav'),
    '3': AudioSegment.from_wav(f'{dir_path}/sounds/3.wav'),
    '4': AudioSegment.from_wav(f'{dir_path}/sounds/4.wav'),
    '5': AudioSegment.from_wav(f'{dir_path}/sounds/5.wav'),
    '6': AudioSegment.from_wav(f'{dir_path}/sounds/6.wav'),
    '7': AudioSegment.from_wav(f'{dir_path}/sounds/7.wav'),
    '8': AudioSegment.from_wav(f'{dir_path}/sounds/8.wav'),
    '9': AudioSegment.from_wav(f'{dir_path}/sounds/9.wav'),
    '0': AudioSegment.from_wav(f'{dir_path}/sounds/0.wav'),
    'blank': AudioSegment.from_wav(f'{dir_path}/sounds/blank.wav'),
}

pin_code = random.sample(range(0, 9), 7)

voice_pin = None

for number in pin_code:
    if not voice_pin:
        voice_pin = sounds[str(number)] + sounds['blank']
        continue
    voice_pin = voice_pin + sounds[str(number)] + sounds['blank']

voice_pin.export("voice-pin.mp3", format="mp3")
