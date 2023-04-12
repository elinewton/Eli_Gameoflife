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

    def eventDispatch(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseCtrl(event)

    def mouseCtrl(self):
        currloc = (pygame.mouse.get_pos())
    #def autofill(self):

    
