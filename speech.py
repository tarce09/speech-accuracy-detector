import speech_recognition as sr

r=sr.Recognizer()

with sr.AudioFile('audioplay.wav') as source:
    print("speak now")
    audio = r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("you said :",text)
    except:
        print("sorry couldnot recognize")