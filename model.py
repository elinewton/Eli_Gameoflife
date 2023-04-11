import random

class GoLModel:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rows = int(self.width/20) + 2
        self.columns = int(self.height/20) + 2 
        self.grid = [[0]*self.columns for i in range(self.rows)]      
        self.fillRandom()


    def toggleCell(self,i,j):
        cell = self.grid[i+1][j+1] = ((self.grid[i+1][j+1] + 1)%2)
        return cell
    
    def currentGrid(self):
        return [self.grid[r][1:-1]for r in range(1,self.rows)]

    def cellCount(self,i,j):
        count = 0
        for r in range(i-1,i+2):
            for c in range(j-1,j+2):
                count += self.grid[r][c]
        count -= self.grid[i][j]
        return count
    
    def fillRandom(self):
        for i in range(0,self.rows-2):
            for j in range(0,self.columns-2):
                num = random.randint(0,10)
                if num < 7:
                    self.grid[i][j] = 1
                else:
                    self.grid[i][j] = 0


    def updateGrid(self):
        next = [[0]*self.columns for i in range(self.rows)]
        for i in range(1,self.rows-1):
            for j in range(1,self.columns-1):
                mid = [i,j]
                cell_Life = self.checkLife(self.cellCount(i,j),i,j)
                next[i][j] = cell_Life
        self.grid = next 
                

    def checkLife(self,cellCount,i,j):
        if ((self.grid[i][j] == 1) and ((cellCount == 2) or (cellCount == 3))):
            return 1

        elif ((self.grid[i][j] == 1) and (cellCount <=1)):
            return 0
        
        elif ((self.grid[i][j] == 1) and (cellCount >3)):
            return 0

        elif ((self.grid[i][j] == 0) and (cellCount == 3)):
            return 1
        else:
            return 0

