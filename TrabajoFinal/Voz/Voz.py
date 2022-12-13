import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv 
import speech_recognition as sr
import time
from gtts import gTTS
import pygame
from playsound import playsound


s = gTTS("Pelícano", lang="es-ES")
s.save('pelicano.mp3')

