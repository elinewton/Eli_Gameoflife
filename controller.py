import pygame

from pygame.math import Vector2
from model import GoLModel
from view import GoLView

class GoLController:

    def __init__(self,model,view):
        self.model = model
        self.view = view
        self.numcols = 1000//20
        self.numrows = 700//20
        self.go = False

    def eventDispatch(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.view.InStartStop(pos) == True:
                self.go = not self.go
            elif self.view.inB1(pos) == True:
                self.model.fillRandom()


                

        
    
    #def autofill(self):