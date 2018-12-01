# reads audio files
# only supports WAV so far

# using scipy to read wav files
from scipy.io.wavfile import read
import numpy as np

def ReadWAV(filename):
    sampleRate, array = read(filename)
    # only supports integral sample
    if not np.issubdtype(array.dtype, np.integer):
        raise RuntimeError('audio file dtype ({}) is not an integral type, which is not supported'.format(array.dtype))

    # generate a warning if the audio file is not a stereo file
    if len(array.shape) != 2 or array.shape[1] != 2:
        print('WARNING: the audio file is not a stereo file. A new stereo audio file with the first channel duplicated is used.')
        newShape = [array.shape[0], 2]
        newArray = np.zeros(newShape, array.dtype)
        for i in range(2):
            newArray[:, i] = array[:, 0]
        array = newArray

    typeInfo = np.iinfo(array.dtype)

    res = {'sample_rate' : sampleRate, 'array' : array, 'dtype_min' : typeInfo.min, 'dtype_max' : typeInfo.max}
    return res