import speech_recognition as sr

class SttEngine:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recognize(self):
        try:
            with self.mic as source:
                audio = self.r.listen(source, timeout=5, phrase_time_limit=5)
            user = self.r.recognize_google(audio, language = "ko-KR")
            print('말씀하신 단어는 '+ user)
            return user
        except sr.UnknownValueError:
            print('Unknown Value Error')
        except sr.RequestError:
            print('Request Error')
        except sr.WaitTimeoutError:
            print('Timeout Error')