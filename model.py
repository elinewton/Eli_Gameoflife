
class Model:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rows = int(self.width/20) + 1
        self.columns = int(self.height/20) + 1
        self.grid = [[0]*self.columns]*self.rows

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
        count -= self.grid[r][c]
        return count


    def updateGrid(self,cellCount,grid):
        next = [[0]*self.columns]*self.rows
        cellCount = 0
        self.grid = grid
        for i in range(self.rows):
            for j in range(self.columns):
                mid = [i,j]
                cell_Life = self.checkLife(cellCount(i,j),i,j)
                next[i][j] = cell_Life
        self.grid = next
                

    def checkLife(self,cellCount,i,j):
        if ((self.grid[i][j] == 1) and ((cellCount == 2) or (cellCount == 3))):
            return 1

        elif ((self.grid[i][j] == 1) and (cellCount <=1)):
            return 0

        elif ((self.grid[i][j] == 0) and (cellCount == 3)):
            return 1
            

        
