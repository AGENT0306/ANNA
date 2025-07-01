import speech_recognition as sr

# Simple speech recognition class

class STT(object):
    def __init__(self, mic_index=None):
        print("Initializing STT")
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def start_stt(self):
        with self.mic as source:
            print("Say something!")
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_whisper(audio)
        except sr.UnknownValueError:
            return "Sorry, could not understand audio!"