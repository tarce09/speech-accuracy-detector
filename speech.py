import speech_recognition as sr
import Levenshtein as Lev

r=sr.Recognizer()

with sr.AudioFile('audioplay.wav') as source:
    print("speak now")
    audio = r.listen(source)

    try:
        text=r.recognize_google(audio)
        string='Hello I am Aryan I am 20 I study in MIT'
        text=text.lower()
        string=string.lower()
        print(Lev.distance(text,string))
        print("you said :",text)
    except:
        print("sorry couldnot recognize")