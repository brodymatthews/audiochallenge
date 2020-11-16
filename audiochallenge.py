from tkinter import *

import pygame
from pydub import AudioSegment
from pygame import mixer
from tkinter import filedialog

pygame.mixer.init()

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.filename =  filedialog.askopenfilename(initialdir = "Desktop",title = "choose your file",filetypes = (("wav files","*.wav"),("all files","*.*")))
        print (root.filename)
    def play(self):
         print("play click")
         pygame.mixer.music.load(self.filename)
         pygame.mixer.music.play()
    def pause(self):
         if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
         else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()

root = Tk()
app= MusicPlayer(root)
root.mainloop()

