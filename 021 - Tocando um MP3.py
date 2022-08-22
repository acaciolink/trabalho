import pygame # use pip install pygame no terminal para instalar
pygame.init()
pygame.mixer.music.load('amor.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

