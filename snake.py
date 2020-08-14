import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x =  0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))

def redrawWindow(surface):
    global row, width
    surface.fill(0,0,0)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20 # Make this number smaller to make the game go faster
    win = pygame.display.set_mode((width, height))
    s = snake (('red', (10, 10))) # colour and position

    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10) # Determines speed of game (frames per second)

        redrawWindow(win)