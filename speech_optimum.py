from numpy import vectorize
import speech_recognition as sr
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


r=sr.Recognizer()

with sr.AudioFile('audioplay.wav') as source:
    print("speak now")
    audio = r.listen(source)

    try:
        
        text=r.recognize_google(audio)
        string='Hello I am Aryan I am 20 I study in MIT'
        text=text.lower()
        string=string.lower()
        sentences=[text,string]
        vectorizer=CountVectorizer().fit_transform(sentences)
        vectors=vectorizer.toarray()
        
        csim=cosine_similarity(vectors)
        print(csim[1][0]*100)
    except:
        print("sorry couldnot recognize")