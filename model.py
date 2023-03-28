
class Model:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rows = int(self.width/20)
        self.columns = int(self.height/20)

#Rules for Game of Life
#if cell == alive && cell_neighbors == 2 or cell_neighbors == 3:
 #   cell == alive

#if cell == alive && cell_neighbors <= 1:
  #  cell == dead

#if cell == dead && cell_neighbors == 3:
 #   cell == alive


    def alive(self,alive):
        self.alive = 1
    

    def updateGrid(self,cellCount,grid):
        cellCount = 0
        self.grid = grid
        for i in range(self.rows):
            for j in range(self.columns):
                mid = [i,j]
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        c = grid[r][c]
                        if c == 1:
                            cellCount += 1
                        next[i][j] = checkLife(cellCount)


    def checkLife(self,cellCount):
        self.cell = int(cell)
        cellCount = 0
        if ((self.cell == self.alive) and ((cellCount == 2) or (cellCount == 3))):
            self.cell = self.alive

        elif ((self.cell == self.alive) and (cellCount <=1)):
            self.cell = 0

        elif ((self.cell == 0) and (cellCount == 3)):
            self.cell = self.alive



            

        
