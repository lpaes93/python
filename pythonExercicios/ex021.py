# Exercício 21 - Faça um programa que leia um arquivo de áudio MP3.
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# Nào consegui fazer tocar.
