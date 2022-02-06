import matplotlib
from scipy.io import wavfile

import sounddevice as sd
import numpy as np
from matplotlib import pyplot as plt 
class Spectrogram:
    matplotlib.rcParams.update({'font.size': 12, 'font.family': 'serif'})

    def __init__(self, filename) -> None:
        self.__fs, self.__data = wavfile.read(filename)
        self.__data = self.__data / 2.0**15
        self.__N = self.__data.shape[0]
        self.__total_time = self.__N/self.__fs 
        self.time = np.arange(0,self.__total_time,self.__total_time/self.__N)
        self.FFT()

    @property
    def get_data(self):
        return self.__data

    @property
    def get_time(self):
        return self.time

    @property
    def get_total_time(self):
        return self.__total_time

    @property
    def get_number_of_samples(self):
        return self.__N

    @property
    def get_frecuency_sample(self):
        return self.__fs

    def FFT(self):
        self._fft_spectrum = np.fft.rfft(self.__data)
        self._freq = np.fft.rfftfreq(self.__data.size, d=1./self.__fs)
        self._fft_spectrum_abs = np.abs(self._fft_spectrum)
    
    @property
    def get_FFT(self) -> tuple:
        return (self._fft_spectrum, self._freq, self._fft_spectrum_abs)
    
    def max_value(self):
        print(type(np.argmax(self._fft_spectrum)*self.__fs/self.__N))
        return np.argmax(self._fft_spectrum)*self.__fs/self.__N
    
    def play_sound(self):
        sd.play(self.__data)

    def plot_input_wave(self):
        plt.figure(figsize=(15,5))
        plt.subplot(121)
        plt.plot(self.time, self.__data[:], 'r')
        plt.grid(linestyle = '--', linewidth = 0.5)
        plt.xlabel("Tiempo, s")

        plt.subplot(122)
        plt.plot(self.time[1000:3000], self.__data[1000:3000])
        plt.grid(linestyle = '--', linewidth = 0.5)
        plt.xlabel("Tiempo, s")

        plt.tight_layout()
        plt.show()

    def plot_fft(self):
        plt.figure(figsize=(7,5))
        plt.plot(self._freq, self._fft_spectrum_abs)
        plt.semilogx()
        plt.grid(True, which="both", ls="-", linewidth = 0.5)
        plt.xlim(1,)
        plt.xlabel("Frecuencia, Hz")
        plt.ylabel("Amplitud, units")
        plt.show()