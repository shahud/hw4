import numpy as np
import scipy.io.wavfile as sp
from scipy.fftpack import rfft, irfft
import matplotlib.pyplot as plot
import scipy.signal as sg

#whitenoise=np.random.randint(-32768,32767,44100,np.int16)

#sp.write('wht.wav', 44100, whitenoise)

class sigen:
    
    def __init__(self,para):
        if para == 'white':
            print('white noise creation')
            self.data=np.random.randint(-32768,32767,441,np.int16) # no need for normalization since there is max and min
           
        elif isinstance(para,str):
            print('read input file')
            (self.rate,self.data)=sp.read(para)
            self.data=np.asarray(self.data,np.int16)
            
        
        elif isinstance(para, list):
            print('found list')
            self.freqarr=np.zeros(44101)
            for i in range(len(para)):
                self.freqarr[(i+1)*440]=para[i]
            
            print(self.freqarr.size)
            
            print(np.where(self.freqarr!=0))
            self.data=np.absolute((np.fft.irfft(self.freqarr)))
            
            
            
    def write(self,para):
        self.data=self.data.astype(np.int16)
        sp.write(para, 44100, self.data)
        
    def showgraph(self):
        plot.subplot(211)
        plot.plot(self.data)
        plot.xlabel('time')
        plot.ylabel('amplitude')
        
        plot.subplot(212)
        fftdata=np.absolute((np.fft.rfft(self.data)))
        fftaxis=np.fft.rfftfreq(self.data.size,1/44100)
        print(fftdata.size)
        print(fftaxis.size)
        
        plot.plot(fftaxis,fftdata)
        plot.xlabel('frequency')
        plot.ylabel('amplitude')
        
        plot.show()
    
    def lowpassfilter(self,f):
        self.coeff=sg.firwin(1001,f/22050)
        self.data=sg.lfilter(self.coeff,[1],self.data)
        
    def highpassfilter(self,f):
        self.coeff=sg.firwin(1001,f/22050,pass_zero=False)
        self.data=sg.lfilter(self.coeff,[1],self.data)
            
'''

a=sigen('n1n.wav')
plot.figure(1)

a.showgraph()
a.lowpassfilter(100)
plot.figure(2)
a.showgraph()
'''
a=sigen('white')
a.write('whitenoise.wav')
