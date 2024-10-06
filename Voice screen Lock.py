from scipy.io import wavfile
import speech_recognition as speech
import numpy as np
#Create recognizer object
voice = speech.Recognizer()

#use Microphone
with speech.Microphone() as source:
    
    print("Speak your password")
    
    #Take audio input from user
    voice_command = voice.listen(source)
    
    try:
        
        #Extract text fromm audio
        text = voice.recognize_google(voice_command)
        
        print(text)
        
        #Store audio at given memory location
        with open('E:\Projects\Voice screen Lock') as f :
            f.write(voice_command.get_wav_data())
        
        #Read audio file from given location
        sample_rate , data = wavfile.read('E:\Projects\Voice screen Lock')

        #Calculating frequency
        w = np.fft.fft(data)
        freqs = np.fft.fftfreq(len(w))
        print(w)
        print(freqs)
        
    except:
        print("Audio not clear")