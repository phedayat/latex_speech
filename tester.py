'''
Parsia Hedayat, Started 2/11/2020
Testing SpeechRecognition
'''

import speech_recognition as sr

print(sr.__version__)

r = sr.Recognizer() # initializes instance of Recognizer for audio recognition

file = sr.AudioFile("audio1.flac") # the audio file to transcribe

with file as src:
    audio = r.record(src) # the contents of the audio file

st = r.recognize_google(audio) # generated string from audio file using the Google Web Speech API

'''
Testing string functions on the transcribed audio file
'''
print(st.find('fox')) # gives index of first letter of 'fox' if found
print(st.find('over')) # gives index of first letter of 'over' if found
print(st.find('crack')) # gives index of first letter of 'crack' if found (will not be found, so returns -1)

toFind = 'fox jumped'

'''
Finds the desired word or phrase and replaces it with something, in this case 'WORKED'
'''
if st.find(toFind) != -1:
    newSt = st.replace(toFind, 'WORKED')

print(newSt)