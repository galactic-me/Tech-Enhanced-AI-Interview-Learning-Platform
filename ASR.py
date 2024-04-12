pip3 install speechrecognition
import speech_recognition as sr
import os

r = sr.Recognizer()
r.energy_threshold = 10000
with sr.Microphone() as source:
    print('Say something')
    audio = r.listen(source)
    print("Done")

try:
    text = r.recognize_google(audio)
    f=open("output.txt","w")
    f.truncate(0) 
    f.write(text)
    f.write("\n")
    f.close()
    print(text)
    os.system("say '"+'I think you said,'+text+'!'+"'")

except Exception as e:
    print(e)

