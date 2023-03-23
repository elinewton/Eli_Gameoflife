import pygame
class GoLView:

    def __init__(self):
        self.width = 1000
        self.height = 700 
        self._DS = pygame.display.set_mode((self.width,self.height))

    def update(self):
        self._DS.fill((150, 224, 171))
        self.drawGrid()
      
        pygame.display.update()

    def drawGrid(self):
        blockSize = 20 #Set the size of the grid block
        for x in range(0, self.width, blockSize):
            for y in range(0, int(self.height * 4/5), blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self._DS, (0,0,0), rect, 1)