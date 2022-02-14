from spectrogram import Spectrogram
from matplotlib import pyplot as plt 

def main()-> None:
    samples = []
    colors = ['#335EFF', '#3396FF', '#5EFF33', '#33FF3C', '#FF3633','#FF4C33', '#6133FF', '#9333FF']
    filters = ['Filtro Pasa Altos', 'Pura', 'Filtro Pasa Banda','Filtro Pasa Bajos']
    samples.append(Spectrogram('SeñalPura.wav'))
    samples.append(Spectrogram('Espectro_Pasa_Altos.wav'))
    samples.append(Spectrogram('Espectro_Pasa_Bajos.wav'))
    samples.append(Spectrogram('Espectro_Pasa_Banda.wav'))
    plot_input_data(len(samples), samples, colors, filters)
    plot_output_data(len(samples), samples, colors, filters)

def plot_input_data(n_samples, samples, colors, filters)-> None:
    plt.figure(figsize=(15,15))
    plt.tight_layout()
    for i in range(n_samples):
        plt.subplot(2, 4, (2*i)+1) 
        plt.plot(samples[i-1].get_time, samples[i-1].get_data[:], color=colors[(2*i)])
        plt.title(f'Señal {filters[i]}')
        plt.xlabel("Tiempo, s")
        plt.ylabel("Amplitud, units")
        plt.grid(linestyle = '--', linewidth = 0.5)
        plt.subplot(2, 4, (2*i)+2) 
        plt.plot(samples[i-1].get_time[1000:3000], samples[i-1].get_data[1000:3000], color=colors[(2*i)+1])
        plt.title(f'Señal ampliada {filters[i]}')
        plt.xlabel("Tiempo, s")
        plt.ylabel("Amplitud, units")
        plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()

def plot_output_data(n_samples, samples, colors, filters)-> None:
    plt.figure(figsize=(15,15))
    plt.tight_layout()
    for i in range(n_samples):
        plt.subplot(2, 2, (i+1)) 
        plt.plot(samples[i-1].get_FFT[1], samples[i-1].get_FFT[2], color=colors[i*2])
        plt.title(f'Espectrograma {filters[i]}')
        plt.semilogx()
        plt.xlim(1,)
        plt.xlabel("Frecuencia, Hz")
        plt.ylabel("Amplitud, units")
        plt.grid(True, which="both", ls="-", linewidth = 0.5)
    plt.show()

if __name__=='__main__':
    main()