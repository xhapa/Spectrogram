from random import sample
from spectrogram import Spectrogram

def main()-> None:
    sample_1 = Spectrogram('1kHz.wav')
    sample_1.play_sound()
    sample_1.plot_input_wave()
    sample_1.plot_fft()
    sample_1.max_value()

    print(sample_1.get_data, type(sample_1.get_data))
    print(sample_1.get_total_time, type(sample_1.get_total_time))
    print(sample_1.get_number_of_samples, type(sample_1.get_number_of_samples))
    print(sample_1.get_frecuency_sample, type(sample_1.get_frecuency_sample))
    print(sample_1.get_data, type(sample_1.get_data))

    print(sample_1.get_FFT, type(sample_1.get_FFT[0]), type(sample_1.get_FFT[1]), type(sample_1.get_FFT[2]))

if __name__=='__main__':
    main()