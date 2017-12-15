from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile as wav

def draw_plot(array, where=211, desc_xlabel="time", desc_ylabel="Hz"):
	subplot(where)
	length = len(array)

	plot(range(length), array, '*')
	xlim([0, length])
	yscale('log')
	xlabel(desc_xlabel)
	ylabel(desc_ylabel)

def draw_spectrum(array, where=212, desc_xlabel="time", desc_ylabel="Hz", cut=100000):
	subplot(where)
	sgn = fft(array)
	signal = abs(sgn)

	for i, value in enumerate(signal):
		if value < cut:
			signal[i] = 0
			sgn[i] = 0

	stem(range(len(signal)), signal, '-*')
	return abs(ifft(sgn))

if __name__ == "__main__":
	w, signal = wav.read("err.wav")
	
	signal = [s[0] for s in signal] # First channel is s[0]
	signal = signal[::10]
	draw_plot(signal)

	array = draw_spectrum(signal, cut=10000)
	draw_plot(array, where=212)

	show()
