import speech_recognition as SpeechRecognition
import time

Recognizer = SpeechRecognition.Recognizer()

Array = {}


def ConvertToText(Audio):
  try:
    Text = Recognizer.recognize_google(Audio)
    return Text
  except SpeechRecognition.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    print("Please try again!")
    return "Fail"
  except SpeechRecognition.RequestError as Err:
    print(
        "Could not request results from Google Speech Recognition service; {0}"
        .format(Err))
    return "Fail"


def InputSpeech():

  with SpeechRecognition.Microphone() as Mic:
    Recognizer.adjust_for_ambient_noise(Mic, 5)
    Audio = Recognizer.listen(Mic)
    Text = ConvertToText(Audio)

    while not Text or Text == "Fail":
      Recognizer.adjust_for_ambient_noise(Mic, 5)
      Audio = Recognizer.listen(Mic)
      Text = ConvertToText(Audio)

    return Text
