import speech_recognition as sr

class STT(object):
    def __init__(self, mic_index=None):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(device_index=mic_index)

    def start_stt(self):
        audio = self.recognizer.listen(self.mic)
        try:
            return "You said: " + self.recognizer.recognize_whisper(audio)
        except sr.UnknownValueError:
            return "Sorry, could not understand audio!"