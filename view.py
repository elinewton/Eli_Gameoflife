import pygame

from model import Model

class GoLView:

    def __init__(self):
        self.width = 1000
        self.height = 700 
        self._DS = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Game of Life')

    def update(self):
        self._DS.fill((200, 200, 200))
        self.drawGrid()
        self.drawBox(100, 600)
        self.drawBox(300, 600)
        self.drawBox(600, 600)
        self.drawBox(800, 600)
        self.cellChange()
      
        pygame.display.update()



    def drawGrid(self):
        blockSize = 20 #Set the size of the grid block
        for x in range(0, self.width, blockSize):
            for y in range(0, int(self.height * 4/5), blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self._DS, (0,0,0), rect, 1)


    def drawBox(self, x, y):
        pygame.draw.rect(self._DS, (255,255,255), pygame.Rect(x, y, 90, 50), 2)