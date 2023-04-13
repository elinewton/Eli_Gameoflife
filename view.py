import pygame
import random

from model import GoLModel

class GoLView:

    def __init__(self):

        self.model = None
        self.width = 1000
        self.height = 700 
        self.grid = None
        self.rows = int(self.width/20) + 2
        self.columns = int((self.height*4/5)/20) + 2  

        self._DS = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Conways Game of Life')

    def setModel(self,model):
        self.model = model
        self.grid = self.model.currentGrid()  

    
    def update(self):
        self.grid = self.model.currentGrid()  
        self._DS.fill((115, 117, 116))
        self.drawCells()
        self.drawGrid()

        self.drawBox(100, 600)
        self.drawBox(300, 600)
        self.drawBox(600, 600)
        self.drawBox(800, 600)
        self.drawPlayButton()

      
        pygame.display.update()

    def drawCell(self,i,j):
        pygame.draw.rect(self._DS, (89, 255, 125), pygame.Rect(i,j, 20, 20))


    def drawCells(self,):
        for i in range(0,self.rows-1):
            for j in range(0,self.columns-2):
                if self.grid[i][j] == 1:
                    self.drawCell(i*20,j*20)
                else:
                    self.grid[i][j] = 0

                    
    def drawGrid(self):
        blockSize = 20 #Set the size of the grid block
        for x in range(0, self.width, blockSize):
            for y in range(0, int(self.height * 4/5), blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self._DS, (0,0,0), rect, 1)


    def drawBox(self, x, y):
        pygame.draw.rect(self._DS, (255,255,255), pygame.Rect(x, y, 90, 50), 2)

    def drawPlayButton(self):
        pygame.draw.circle(self._DS, (255,255,255), (500, 630), 30, width = 0)
        pygame.draw.polygon(self._DS, (0,0,0), ((490,615), (490,645), (515,630)), width = 3)
