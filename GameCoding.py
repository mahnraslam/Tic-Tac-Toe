class Playing:
    def __init__(self, frame, row, col):
        self.array = [[[0 for k in range(col)] for j in range(row)] for i in range(frame)]
        self.rows = row
        self.cols = col
        self.frames = frame

    def winning(self):
        def checkMultipleFrame():
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.array[0][i][j] == self.array[1][i][j] == self.array[2][i][j]!=  0:
                        return self.array[0][i][j]
            return -1

        def check_single_board(frame):
            for row in range(3):
                if self.array[frame][row][0] == self.array[frame][row][1] == self.array[frame][row][2]!=  0:
                    return f"{self.array[frame][row][0]}"
            for col in range(3):
                if self.array[frame][0][col] == self.array[frame][1][col] == self.array[frame][2][col]!=  0:
                    return f"{self.array[frame][0][col]}"
            if self.array[frame][0][0] == self.array[frame][1][1] == self.array[frame][2][2]!=  0:
                return f"{self.array[frame][0][0]}"
            elif self.array[frame][0][2] == self.array[frame][1][1] == self.array[frame][2][0]!=  0:
                return f"{self.array[frame][0][2]}"
            return -1

        for frame in range(self.frames):
            result = check_single_board(frame)
            if result != -1:
                return result
        if self.frames > 1:
            result = checkMultipleFrame()
            if result != -1:
                return result

        return -1

    def is_draw(self):
        for frame in range(self.frames):
            for row in range(3):
                for col in range(3):
                    if self.array[frame][row][col] == 0:
                        return False
        return True


    def checkFirstCorner(self, frameNum,d):
        for i in range(1, 3):
            if self.array[frameNum][0][0] == self.array[frameNum][0][i] and self.array[frameNum][0][0] not in (d, 0):
                    if i == 1 and self.array[frameNum][0][i + 1] == 0:
                        return 0, i + 1
                    elif i == 2 and self.array[frameNum][0][i - 1] == 0:
                        return 0, i - 1
                    elif self.array[frameNum][0][0] == self.array[frameNum][i][0] and self.array[frameNum][0][0] not in (d, 0):
                        if i == 1 and self.array[frameNum][i + 1][0] == 0:
                            return i + 1, 0
                        elif i == 2 and self.array[frameNum][i - 1][0] == 0:
                            return i - 1, 0

        if self.array[frameNum][0][2] == self.array[frameNum][0][1] and self.array[frameNum][0][2] not in (d, 0):
            if self.array[frameNum][0][0] == 0:
                return 0, 0
        return -1, -1

    def checkDiagonal(self, frameNum, d):

        if ((self.array[frameNum][0][0] == self.array[frameNum][1][1] and self.array[frameNum][0][0] not in (d, 0)) or
            (self.array[frameNum][2][0] == self.array[frameNum][2][1] and self.array[frameNum][2][0] not in (d, 0))):
            if self.array[frameNum][2][2] == 0:
                return 2, 2
        elif ((self.array[frameNum][0][0] == self.array[frameNum][2][2] and self.array[frameNum][0][0] not in (d, 0)) or
            (self.array[frameNum][1][0] == self.array[frameNum][1][2] and self.array[frameNum][1][0] not in (d, 0)) or
            (self.array[frameNum][2][0] == self.array[frameNum][0][2] and self.array[frameNum][2][0] not in (d, 0))):
            if self.array[frameNum][1][1] == 0:
                return 1, 1
        elif self.array[frameNum][2][2] == self.array[frameNum][1][1] and self.array[frameNum][2][2] not in (d, 0):
            if self.array[frameNum][0][0] == 0:
                return 0, 0
        elif self.array[frameNum][0][2] == self.array[frameNum][1][1] and self.array[frameNum][0][2] not in (d, 0):
            if self.array[frameNum][2][0] == 0:
                return 2, 0
        elif self.array[frameNum][2][0] == self.array[frameNum][1][1] and self.array[frameNum][2][0] not in (d, 0):
            if self.array[frameNum][0][2] == 0:
                return 0, 2
        return -1, -1

    def checkColMid(self, frameNum, d):
        for i in range(1, 3):
            if self.array[frameNum][0][1] == self.array[frameNum][i][1] and self.array[frameNum][0][1] not in (d, 0):
                if i == 1 and self.array[frameNum][i + 1][1] == 0:
                    return i + 1, 1
                elif i == 2 and self.array[frameNum][0][1] == 0:
                    return 0, 1
        if self.array[frameNum][2][1] == self.array[frameNum][1][1] and self.array[frameNum][2][1] not in (d, 0):
            if self.array[frameNum][0][1] == 0:
                return 0, 1
        return -1, -1

    def checkRowMid(self, frameNum, d):
        if self.array[frameNum][1][0] == self.array[frameNum][1][1] and self.array[frameNum][1][0] not in (d, 0):
            if self.array[frameNum][1][2] == 0:
                return 1, 2
        elif self.array[frameNum][1][1] == self.array[frameNum][1][2] and self.array[frameNum][1][1] not in (d, 0):
            if self.array[frameNum][1][0] == 0:
                return 1, 0
        return -1, -1

    def checkOtherCorner(self, frameNum, d):
        for i in range(1, -1, -1):
            if self.array[frameNum][2][2] == self.array[frameNum][2][i] and self.array[frameNum][2][2] not in (d, 0):
                if i == 1 and self.array[frameNum][2][0] == 0:
                    return 2, 0
                elif i == 0 and self.array[frameNum][2][1] == 0:
                    return 2, 1
            if self.array[frameNum][2][2] == self.array[frameNum][i][2] and self.array[frameNum][2][2] not in (d, 0):
                if i == 1 and self.array[frameNum][0][2] == 0:
                    return 0, 2
                elif i == 0 and self.array[frameNum][1][2] == 0:
                    return 1, 2
        if ((self.array[frameNum][2][0] == self.array[frameNum][2][1] and self.array[frameNum][2][0] not in (d, 0)) or
            (self.array[frameNum][0][2] == self.array[frameNum][1][2] and self.array[frameNum][0][2] not in (d, 0))):
            if self.array[frameNum][2][2] == 0:
                return 2, 2
        return -1, -1

    def checkFrames(self,d):
        for i in range(self.rows):
            for j in range(self.cols):
                # Check if frames 0 and 1 have the same mark and frame 2 is empty
                if self.array[0][i][j] == self.array[1][i][j] and self.array[1][i][j] not in (d,0) and self.array[2][i][j] == 0:
                    return 2, i, j
                # Check if frames 0 and 2 have the same mark and frame 1 is empty
                elif self.array[0][i][j] == self.array[2][i][j] and self.array[2][i][j] not in (d,0) and self.array[1][i][j] == 0:
                    return 1, i, j
                # Check if frames 1 and 2 have the same mark and frame 0 is empty
                elif self.array[1][i][j] == self.array[2][i][j]  and self.array[2][i][j] not in (d,0) and self.array[0][i][j] == 0:
                    return 0, i, j
        return -1, -1, -1

    def  checkWinningMove(self, frameNum):
        i, j = self.checkRowMid(frameNum , "O")
        if i != -1:
            return i, j
        i, j = self.checkFirstCorner(frameNum ,"O")

        if i != -1:
            return i, j
        i, j = self.checkColMid(frameNum , "O")
        if i != -1:
            return i, j
        i, j = self.checkOtherCorner(frameNum , "O")
        if i != -1:
            return i, j
        i, j = self.checkDiagonal(frameNum ,"O")
        if i != -1:
            return i, j
        i, j = self.checkColMid(frameNum , "O")
        print(i,j)
        if i != -1:
            return i, j

 

        return -1, -1  # Added return for consistency

    def  stopUserWinning(self,frameNum):
        i, j = self.checkRowMid(frameNum ,0)
        if i != -1:
            return i, j
        i, j = self.checkFirstCorner(frameNum ,0)

        if i != -1:
            return i, j
        i, j = self.checkColMid(frameNum , 0)
        if i != -1:
            return i, j
        i, j = self.checkOtherCorner(frameNum , 0)
        if i != -1:
            return i, j
        i, j = self.checkDiagonal(frameNum ,0)
        if i != -1:
            return i, j
        i, j = self.checkColMid(frameNum , 0)
        print(i,j)
        if i != -1:
            return i, j
        return -1, -1

    def blockPlayerWin(self, userF, userRow, userCol):
        if userRow == 0 and userCol == 0:
            if self.array[userF][1][1] == 0:
                return userF, 1, 1
            elif self.array[userF][2][0] == 0:
                return userF, 2, 0
            elif self.array[userF][0][2] == 0:
                return userF, 0, 2
            elif self.array[userF][1][0] == 0:
                return userF, 1, 0
            elif self.array[userF][0][1] == 0:
                return userF, 0, 1

        elif userRow == 0 and userCol == 1:
            if self.array[userF][0][0] == 0:
                return userF, 0, 0
            elif self.array[userF][1][1] == 0:
                return userF, 1, 1
            elif self.array[userF][0][2] == 0:
                return userF, 0, 2

        elif userRow == 0 and userCol == 2:
            if self.array[userF][1][1] == 0:
                return userF, 1, 1
            elif self.array[userF][2][2] == 0:
                return userF, 2, 2

        elif userRow == 1 and userCol == 0:
            if self.array[userF][0][0] == 0:
                return userF, 0, 0
            elif self.array[userF][1][1] == 0:
                return userF, 1, 1
            elif self.array[userF][2][0] == 0:
                return userF, 2, 0

        elif userRow == 1 and userCol == 1:
            if self.array[userF][0][0] == 0:
                return userF, 0, 0
            elif self.array[userF][0][2] == 0:
                return userF, 0, 2
            elif self.array[userF][2][0] == 0:
                return userF, 2, 0
            elif self.array[userF][2][2] == 0:
                return userF, 2, 2

        elif userRow == 1 and userCol == 2:
            if self.array[userF][0][2] == 0:
                return userF, 0, 2
            elif self.array[userF][1][1] == 0:
                return userF, 1, 1

        elif userRow == 2 and userCol == 0:
            if self.array[userF][0][0] == 0:
                return userF, 0, 0
            elif self.array[userF][2][2] == 0:
                return userF, 2, 2

        elif userRow == 2 and userCol == 1:
            if self.array[userF][2][0] == 0:
                return userF, 2, 0
            elif self.array[userF][2][2] == 0:
                return userF, 2, 2

        elif userRow == 2 and userCol == 2:
            if self.array[userF][0][0] == 0:
                return userF, 0, 0
            elif self.array[userF][2][0] == 0:
                return userF, 2, 0
        return -1, -1, -1

    def random(self):
        for frame in range(self.frames):
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.array[frame][r][c] == 0:
                        return frame, r, c
        return -1, -1, -1  # In case all frames are full
    def putAutomatically(self,f1,r1,c1):

        for i in range(self.frames):
            
            row, col = self.checkWinningMove(i)
            if row != -1 and self.array[i][row][col] == 0:
                return i, row, col
            
            row, col = self.stopUserWinning(i)
            if row != -1 and self.array[i][row][col] == 0:
                return i, row, col
       
        if  self.frames == 3 :
            frame, row, col = self.checkFrames("O")
            if frame != -1:
                return frame, row, col
        if  self.frames == 3 :
            frame, row, col = self.checkFrames(0)
            if frame != -1:
                return frame, row, col    
        frame, row, col = self.blockPlayerWin(f1,r1,c1)
        if frame != -1:
            return frame, row, col

        # If no strategic move is found, pick a random empty spot
        return self.random()

