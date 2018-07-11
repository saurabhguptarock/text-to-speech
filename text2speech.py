import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('say something')
    while 1:
        audio = r.listen(source)
        try:
            print('Google thinks you said: ' + r.recognize_google(audio))

        except Exception:
            pass
