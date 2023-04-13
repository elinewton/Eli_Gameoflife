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
        pygame.display.set_caption('Game of Life')

    def setModel(self,model):
        self.model = model
        self.grid = self.model.currentGrid()  

    
    def update(self):
        self.grid = self.model.currentGrid()  
        self._DS.fill((115, 117, 116))
        self.drawCells()
        self.drawGrid()
        self.b1 = self.drawBox(100, 600)
        self.b2 = self.drawBox(275, 600)
        self.b4 = self.drawBox(625, 600)
        self.b5 = self.drawBox(800, 600)
        self.drawStartStop()
      
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
        r = pygame.Rect(x,y,100,50)
        pygame.draw.rect(self._DS, (255,255,255), r, width = 0)
        return r

    def drawStartStop(self):
        self.drawBox(450,600)
        pygame.draw.polygon(self._DS, (0,0,0), ((490,610), (490,640), (515,625)), width = 3)

    def InStartStop(self, pos):
        return pygame.Rect(450,600,100,50).collidepoint(pos)
        
    def inB1(self,pos):
        return self.b1.collidepoint(pos)