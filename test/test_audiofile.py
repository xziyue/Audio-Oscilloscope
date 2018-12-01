import numpy as np
from src.audiofile import *
import matplotlib.pyplot as plt

wavObj = ReadWAV('../sample/Jerobeam Fenderson - Spirals.wav')
print(np.min(wavObj['array']))
print(np.max(wavObj['array']))

size = 44100
plt.plot(np.arange(size), wavObj['array'][:size, :1])
plt.show()


print('fin')