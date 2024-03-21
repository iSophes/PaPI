from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from threading import Thread
import random
import time

from SpeechConverter import InputSpeech

Images = [[
    "duck",
    "Images/Duck.png",
    ["Quack", "Kaczka"],
], [
  "cow", 
  "Images/cow.png", 
  ["Moo"]], 
    ["pig", 
     "Images/pig.png", 
     ["Oink"]
    ]]

def Count():
  for i in range (2):
    TextLabel.config(text="Say what the image is! ("+(i+1)+")")
  

def StartInput():
  print("woo")
  TextLabel.config(text="Say what the image is!")
  time.sleep(1)
  Thread(group=None, target=Count, args=[])
  InputGiven = InputSpeech()

  Submit(InputGiven)


def Correct(SoundWord, Animal):
  global TextBox
  global SelectedImage
  global canvas
  global Img

  if SoundWord:
    TextLabel.config(text="Well Done! A " + Animal + " goes " + SoundWord +
                     "!")

  if not SoundWord:
    TextLabel.config(text="Well Done! That's correct! It is a " + Animal + "!")

  time.sleep(1)

  NewSel = Images[random.randint(0, len(Images) - 1)]

  while NewSel == SelectedImage:
    NewSel = Images[random.randint(0, len(Images) - 1)]

  SelectedImage = NewSel
  Img = ImageTk.PhotoImage(Image.open(SelectedImage[1]).resize((347, 260)))

  NewImageLabel = Label(root, image=Img)
  NewImageLabel.place(anchor=CENTER, relx=0.5, rely=0.5)
  StartInput()


def Wrong():

  TextLabel.config(text="Sorry, that's incorrect! Try again!")
  TextBox.delete("0", END)
  time.sleep(1)
  TextLabel.config(text="Say what the image is!")


def Submit(InputGiven):
  global SelectedImage

  IsCorrect = False

  if SelectedImage[0].lower() == InputGiven.lower():
    IsCorrect = True

  for Result in SelectedImage[2]:
    if InputGiven.lower() == Result.lower():
      IsCorrect = True

  if IsCorrect:
    NewThread = Thread(group=None,
                       target=Correct,
                       args=[None, SelectedImage[0]])
    NewThread.start()
    return 'break'

  NewThread = Thread(group=None, target=Wrong, args=[])
  NewThread.start()
  return 'break'


root = Tk()
root.geometry("500x400")
root.title("PAPI Work")
root.resizable(width=True, height=True)

SelectedImage = Images[random.randint(0, len(Images) - 1)]

Img = ImageTk.PhotoImage(Image.open(SelectedImage[1]).resize((347, 260)))
ImageLabel = Label(root, image=Img)
ImageLabel.place(anchor=CENTER, relx=0.5, rely=0.5)

'''TextBox = Entry(root)
TextBox["wrap"] = None
TextBox.place(relx=0.5, rely=0.875, anchor=CENTER)
'''
TextLabel = Label(root, text="Say what the image is!")
TextLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

time.sleep(1)
StartInput()

root.mainloop()




