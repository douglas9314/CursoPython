# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP#

import pygame
print('--== Desafio 021 ==--')
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
import time
time.sleep(360)