import pygame
pygame.mixer.init()
pygame.init() #iniciando a biblioteca
pygame.mixer.music.load('roling.mp3') #carrega o arquivo
pygame.mixer.music.play()
pygame.event.wait()

