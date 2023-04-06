import pygame
from pygame.math import Vector2
from model import Model
from view import GoLView

class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view

    #def cellChange(self, event):
        #if event.type == pygame.MOUSEBUTTONDOWN:
         #   self._DS.fill((255,255,0))
            
