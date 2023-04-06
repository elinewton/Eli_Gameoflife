import pygame
from view import GoLView
from model import GoLModel

class GoLController:
    def __init__(self,model,view):
        self.model = model
        self.view = view

    def eventDispatch(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseCtrl(event)

    