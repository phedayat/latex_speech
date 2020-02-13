'''
Parsia Hedayat, Started 2/11/2020
Testing SpeechRecognition
'''

import speech_recognition as sr

print(sr.__version__)

r = sr.Recognizer() # initializes instance of Recognizer for audio recognition

file = sr.AudioFile("./audio_files/audio3.flac") # the audio file to transcribe

with file as src:
    audio = r.record(src) # the contents of the audio file

st = r.recognize_google(audio) # generated string from audio file using the Google Web Speech API

'''
Testing string functions on the transcribed audio file
'''
'''
print(st.find('fox')) # gives index of first letter of 'fox' if found
print(st.find('over')) # gives index of first letter of 'over' if found
print(st.find('crack')) # gives index of first letter of 'crack' if found (will not be found, so returns -1)
'''

commands = {"in":"\in", "to the power of":"^", "bbr":"\mathbb{R}"}

keyword = "command"
# toFind = 'fox jumped'

l = st.split()

'''
Finds the desired word or phrase and replaces it with something, in this case 
'WORKED'
'''
'''
if st.find(keyword) != -1:
    cmdKey = st.find(keyword) + len(keyword) + 1
    # newSt = st.replace(toFind, 'WORKED')
'''

'''
Loops through the list of words in our transcription to replace all commands
with their corresponding LaTeX command
'''
while keyword in l:
    cmdKey = l.index(keyword) + 1 # finds the index of the word that is the LaTeX command
    cmdValue = commands[l[cmdKey]] # gives the value of the LaTeX command in the \command format
    l.remove(l[cmdKey]) # removes the key from the list
    l.insert(cmdKey, cmdValue) # add the LaTeX command in its place
    l.remove(l[cmdKey - 1]) # removes the keyword 'command' from the list
else:
    print("No keywords found")

newSt = " ".join(l) # creates a string from the new list

print(newSt)
print(commands["in"])