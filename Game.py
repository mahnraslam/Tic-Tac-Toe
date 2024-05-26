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
                    if self.array[0][i][j] == self.array[1][i][j] == self.array[2][i][j] != 0:
                        return self.array[0][i][j]
            return -1

        def check_single_board(frame):
            for row in range(3):
                if self.array[frame][row][0] == self.array[frame][row][1] == self.array[frame][row][2] != 0:
                    return f"{self.array[frame][row][0]}"
            for col in range(3):
                if self.array[frame][0][col] == self.array[frame][1][col] == self.array[frame][2][col] != 0:
                    return f"{self.array[frame][0][col]}"
            if self.array[frame][0][0] == self.array[frame][1][1] == self.array[frame][2][2] != 0:
                return f"{self.array[frame][0][0]}"
            elif self.array[frame][0][2] == self.array[frame][1][1] == self.array[frame][2][0] != 0:
                return f"{self.array[frame][0][2]}"
            return -1

        for frame in range(self.frames):
            result = check_single_board(frame)
            if result != -1:
                return result

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

    def checkFirstCorner(self, frameNum):
        for i in range(1, 3):
            if self.array[frameNum][0][0] == self.array[frameNum][0][i] != 0:
                if i == 1  and self.array[frameNum][0][i+1] == 0 :
                    return 0, i + 1
                elif i==2 and   self.array[frameNum][0][i-1]==0:
                    return 0, i - 1
            elif self.array[frameNum][0][0] == self.array[frameNum][i][0] != 0:
                if i == 1 and  self.array[frameNum][i+1][0]==0:
                    return i + 1, 0
                elif i==2 and self.array[frameNum][i-1][0]==0:
                    return i - 1, 0

        if ((self.array[frameNum][0][2] == self.array[frameNum][0][1] != 0 or
             self.array[frameNum][2][0] == self.array[frameNum][2][1] != 0) and self.array[frameNum][0][0] != 0):
            if  self.array[frameNum][0][0]==0 : 
                return 0, 0
        return -1, -1

    def checkDiagonal(self, frameNum):
        if self.array[frameNum][0][0] == self.array[frameNum][1][1] != 0 :
            if self.array[frameNum][2][2]==0:
                return 2, 2
        elif self.array[frameNum][0][0] == self.array[frameNum][2][2] != 0 or self.array[frameNum][1][0] == self.array[frameNum][1][2] != 0:
            if self.array[frameNum][1][1]==0:
                return 1, 1
        elif self.array[frameNum][2][2] == self.array[frameNum][1][1] != 0:
            if self.array[frameNum][0][0]==0:
                return 0, 0
        return -1, -1

    def checkColMid(self, frameNum):
        for i in range(1, 3):
            if self.array[frameNum][0][1] == self.array[frameNum][i][1] != 0:
                if i == 1 and self.array[frameNum][i+1][1]==0:
                    return i + 1, 1
                else:
                    return 1, 1
        if self.array[frameNum][2][1] == self.array[frameNum][1][1] != 0:
            if self.array[frameNum][0][1]==0:
                return 0, 1 
        return -1, -1

    def checkRowMid(self, frameNum):
        if self.array[frameNum][1][0] == self.array[frameNum][1][1] != 0:
            if self.array[frameNum][1][2]==0:
                return 1, 2
        elif self.array[frameNum][1][1] == self.array[frameNum][1][2] != 0:
            if self.array[frameNum][1][0]==0:
                return 1, 0
        return -1, -1

    def checkOtherCorner(self, frameNum):
        i = 2
        while i >= 0:
            if self.array[frameNum][2][2] == self.array[frameNum][2][i] != 0:
                if i == 1 and  self.array[frameNum][2][0]==0:
                    return 2, 0
                elif i==2 and  self.array[frameNum][2][1]==0:
                    return 2, 1
            elif self.array[frameNum][2][2] == self.array[frameNum][i][2] != 0:
                if i == 1 and  self.array[frameNum][0][2]==0:
                    return 0, 2
                elif self.array[frameNum][1][2]==0:
                    return 1, 2
            i -= 1
        if self.array[frameNum][2][0] == self.array[frameNum][2][1] != 0 or self.array[frameNum][0][2] == self.array[frameNum][1][2] != 0:
            if self.array[frameNum][2][2]==0:
                return 2, 2
        return -1, -1

    def putInFrame(self, frameNum):
        i, j = self.checkRowMid(frameNum)
        if i != -1:
            return i, j
        i, j = self.checkFirstCorner(frameNum)
        if i != -1:
            return i, j
        i, j = self.checkColMid(frameNum)
        if i != -1:
            return i, j
        i, j = self.checkOtherCorner(frameNum)
        if i != -1:
            return i, j
        i, j = self.checkDiagonal(frameNum)
        if i != -1:
            return i, j
        return -1, -1  # Added return for consistency
    def putAutomatically(self):
        for i in range(3):
            row, col = self.putInFrame(i)
            if row != -1 and self.array[i][row][col] == 0:
                return i, row, col
        return self.random()

    def random(self):
        for frame in range(self.frames):
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.array[frame][r][c] == 0:
                        return frame, r, c
        return -1, -1, -1  # In case all frames are full
 