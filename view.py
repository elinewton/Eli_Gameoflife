import pygame 


class GoLView:

    def __init__(self):
        self.width = 500
        self.height = 700
        self._DS = pygame.display.set_mode((self.width,self.height))

    def update(self):
        self._DS.fill((255,255,255))
        self.drawGrid()
        #pygame.draw.line(self._DS, (0,0,0), (300, 0), (300, 300), 2)
        #pygame.draw.line(self._DS, (0,0,0), (0, 0), (300, 0), 2)
        #pygame.draw.line(self._DS, (0,0,0), (0, 0), (0, 300), 2)
        #pygame.draw.line(self._DS, (0,0,0), (0, 300), (300, 300), 2)
        pygame.display.update()

    def drawGrid(self):
        blockSize = 20 
        for x in range(0, 500, blockSize):
            for y in range(0, 500, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self._DS, (0, 0, 0), rect, 1)
            