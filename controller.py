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
        

    #def cellChange(self, event):
        #if event.type == pygame.MOUSEBUTTONDOWN:
         #   self._DS.fill((255,255,0))
        
    def highlightCell(self):
        blockSize = 20 #Set the size of the grid block
        for x in range(0, self.width, blockSize):
            for y in range(0, int(self.height * 4/5), blockSize):
                #if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos() <= (x,y) and pygame.mouse.get_pos() >= (x+blockSize,y+blockSize):

