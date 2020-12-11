from matrix import *
from random import *
from enum import Enum
#import LED_display as LMD 
class TextColor():
    red    = "\033[31m"
    green  = "\033[32m"
    yellow = "\033[33m"
    blue   = "\033[34m"
    purple = "\033[35m"
    cyan   = "\033[36m"
    white  = "\033[37m"
    pink   = "\033[95m"
### end of class TextColor()

class TetrisState(Enum):
    Running = 0
    NewBlock = 1
    Finished = 2
### end of class TetrisState():

class Tetris():
    nBlockTypes = 0
    nBlockDegrees = 0
    setOfBlockObjects = 0
    iScreenDw = 0   # larget enough to cover the largest block

    def __init__(self, iScreenDy, iScreenDx):
        self.iScreenDy = iScreenDy
        self.iScreenDx = iScreenDx
        self.idxBlockDegree = 0
        arrayScreen = self.createArrayScreen()
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)
        self.justStarted = True
        self.top = 0
        self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2
        self.state = TetrisState.NewBlock
        return

    @classmethod
    def init(cls, setOfBlockArrays):
        Tetris.nBlockTypes = len(setOfBlockArrays)
        Tetris.nBlockDegrees = len(setOfBlockArrays[0])
        Tetris.setOfBlockObjects = [[0] * Tetris.nBlockDegrees for _ in range(Tetris.nBlockTypes)]
        arrayBlk_maxSize = 0

        for i in range(Tetris.nBlockTypes):
            if arrayBlk_maxSize <= len(setOfBlockArrays[i][0]):
                arrayBlk_maxSize = len(setOfBlockArrays[i][0])
        Tetris.iScreenDw = arrayBlk_maxSize     # larget enough to cover the largest block

        for i in range(Tetris.nBlockTypes):
            for j in range(Tetris.nBlockDegrees):
                mat = Matrix(setOfBlockArrays[i][j])
                mat.mulc(i+1)
                Tetris.setOfBlockObjects[i][j] = mat
        return
		
    def createArrayScreen(self):
        self.arrayScreenDx = Tetris.iScreenDw * 2 + self.iScreenDx
        self.arrayScreenDy = self.iScreenDy + Tetris.iScreenDw
        self.arrayScreen = [[0] * self.arrayScreenDx for _ in range(self.arrayScreenDy)]
        for y in range(self.iScreenDy):
            for x in range(Tetris.iScreenDw):
                self.arrayScreen[y][x] = 1
            for x in range(self.iScreenDx):
                self.arrayScreen[y][Tetris.iScreenDw + x] = 0
            for x in range(Tetris.iScreenDw):
                self.arrayScreen[y][Tetris.iScreenDw + self.iScreenDx + x] = 1

        for y in range(Tetris.iScreenDw):
            for x in range(self.arrayScreenDx):
                self.arrayScreen[self.iScreenDy + y][x] = 1

        return self.arrayScreen

    def accept(self, key): 
        if self.state == TetrisState.NewBlock:
            self.idxBlockType = int(key)
        self.state = TetrisState.Running
        if key == 'a':
            self.left -= 1
        elif key == 'd':
            self.left += 1
        elif key == 's':
            self.top += 1
        elif key == 'w':
            self.idxBlockDegree = (self.idxBlockDegree + 1)% (Tetris.nBlockDegrees)

        elif key == ' ':
            while (self.tempBlk.anyGreaterThan(1)==False):
                self.top += 1
                self.tempBlk = self.iScreen.clip(self.top,self.left,self.top+self.currBlk.get_dy(),self.left+self.currBlk.get_dx())
                self.tempBlk = self.tempBlk+self.currBlk
        self.currBlk = Matrix(Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree]) 
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
        self.tempBlk = self.tempBlk + self.currBlk 
        if self.tempBlk.anyGreaterThan(1):
            if key == 'a':
                self.left += 1
            elif key == 'd':
                self.left -= 1
            elif key == 's':
                self.top -= 1
                self.state = TetrisState.NewBlock
            elif key == 'w':
                self.idxBlockDegree = (self.idxBlockDegree - 1) % Tetris.nBlockDegrees
            elif key==' ':
                for i in range(5):
                    if self.tempBlk.anyGreaterThan(1):
                        self.top-=1
                        self.currBlk=Matrix(Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
                        self.tempBlk=self.iScreen.clip(self.top,self.left,self.top+self.currBlk.get_dy(),self.left+self.currBlk.get_dx())
                        self.tempBlk=self.tempBlk+self.currBlk
                if self.tempBlk.anyGreaterThan(1)==False:
                    self.state=TetrisState.NewBlock
            self.currBlk=Matrix(Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree])
            self.tempBlk=self.iScreen.clip(self.top,self.left,self.top+self.currBlk.get_dy(),self.left+self.currBlk.get_dx())
            self.tempBlk=self.tempBlk+self.currBlk
        self.oScreen=Matrix(self.iScreen)
        self.oScreen.paste(self.tempBlk,self.top,self.left)

        if self.state == TetrisState.NewBlock:
            self.oScreen = self.deleteFullLines()
            self.iScreen = Matrix(self.oScreen)
            self.top = 0
            self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2
            self.idxBlockDegree = 0

        if self.tempBlk.anyGreaterThan(1):
            self.state = TetrisState.Finished
            self.oScreen = Matrix(self.iScreen)

        return self.state
		

    def printScreen(self):
        array = self.oScreen.get_array()

        for y in range(self.oScreen.get_dy()-Tetris.iScreenDw):
            for x in range(Tetris.iScreenDw, self.oScreen.get_dx()-Tetris.iScreenDw):
                if array[y][x] == 0:
#                    LMD.set_pixel(y, 19-x, 0)
                    print(TextColor().white + "□", end='')
                elif array[y][x] == 1:
#                    LMD.set_pixel(y, 19-x, 1)
                    print(TextColor().white + "■", end='')
                elif array[y][x] == 2:
#                    LMD.set_pixel(y, 19-x, 2)
                    print(TextColor().pink + "■", end='')
                elif array[y][x] == 3:
#                    LMD.set_pixel(y, 19-x, 3)
                    print(TextColor().red + "■", end='')
                elif array[y][x] == 4:
#                    LMD.set_pixel(y, 19-x, 4)
                    print(TextColor().green + "■", end='')
                elif array[y][x] == 5:
#                    LMD.set_pixel(y, 19-x, 5)
                    print(TextColor().yellow + "■", end='')
                elif array[y][x] == 6:
#                    LMD.set_pixel(y, 19-x, 6)
                    print(TextColor().blue + "■", end='')
                elif array[y][x] == 7:
#                    LMD.set_pixel(y, 19-x, 7)
                    print(TextColor().cyan + "■", end='')
                elif array[y][x] == 8:
#                    LMD.set_pixel(y, 19-x, 2)
                    print(TextColor().purple + "■", end='')
                else:
                    print("XX", end='')
            print()
    # def printScreen(self):
    #     array = self.oScreen.get_array()

    #     for y in range(self.oScreen.get_dy()-Tetris.iScreenDw):
    #         for x in range(Tetris.iScreenDw, self.oScreen.get_dx()-Tetris.iScreenDw):
    #             if array[y][x] == 0:
    #                 print("□", end='')
    #                 #LMD.set_pixel(y, 19-x, 0)
    #             elif array[y][x] == 1:
    #                 print("■", end='')
    #                 #LMD.set_pixel(y, 19-x, 4)
    #             else:
    #                 print("XX", end='')
    #                 #continue
    #         print()

    def deleteFullLines(self): # To be implemented!!
        
        trash=0
        checkline = self.currBlk.get_dy()
        if self.top + self.currBlk.get_dy()-1 >= self.iScreenDy :
            checkline = self.iScreenDy - self.top
        arrayScreen = self.createArrayScreen()
        nScreen = Matrix(arrayScreen)
        spaceline = nScreen.clip(0, 0, 1, nScreen.get_dx())

        for i in range(checkline-1,-1,-1):
            xline = self.top+i+trash
            line = self.oScreen.clip(xline,0,xline+1,self.oScreen.get_dx())
            if line.sum() == self.oScreen.get_dx() :
                temp = self.oScreen.clip(0,0,xline,self.oScreen.get_dx())
                self.oScreen.paste(temp,1,0)
                self.oScreen.paste(spaceline,0,0)
                trash +=1
        
        return self.oScreen


   


### end of class Tetris():