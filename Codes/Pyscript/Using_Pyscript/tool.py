import datetime


def get_today():
    today = datetime.date.today().strftime("%Y-%m-%d")
    return today


import numpy as np


def wave(frequency, amplitude=1, phase=0):
    def _wave(time):
        return amplitude * np.sin(2 * np.pi * frequency * time + phase)

    return _wave
