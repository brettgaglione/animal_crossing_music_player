import datetime
import os
import eyed3
import pygame

directory = "/Users/brettgaglione/Music/BrettsLocalMusic/animal_crossing_soundtrack/"

songNames = ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM"]
pathsToFiles = []

for filename in os.listdir(directory):
    song = eyed3.load(directory + filename)
    if song.tag.title in songNames:
        pathsToFiles.append(directory + filename)

dict = zip(range(24), pathsToFiles)

pygame.mixer.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load(dict[datetime.datetime.now().time().hour][1])
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10) # Ticks are to make sure play(0) and get_busy() arent calling too closely together so they work properly.
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
    if not pygame.mixer.music.get_busy(): #if song ends, play another
        pygame.mixer.music.load(dict[datetime.datetime.now().time().hour][1])
        pygame.mixer.music.play(0)