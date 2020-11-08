from time import sleep

mapping = {}

def printBoard(board):
    print()
    print("----------------------- Board ----------------------------")
    print()
    print()
    for i in range(3):
        print("                     ", end="")
        for j in range(3):
            print(" " + str(board[i][j]) + " ", end="")
            if j != 2:
                print("|", end="")
        print()
        if i != 2:
            print("                      _+_+_ ")
    print()
    print()
    print("----------------------------------------------------------")

def manhattan(board):
    total = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != -1:
                orow, ocol = mapping[board[i][j]]
                total += abs(orow-i) + abs(ocol-j)
    return total

def canGoUp(emptyrow):
    return emptyrow > 0

def canGoDown(emptyrow):
    return emptyrow < 2

def canGoLeft(emptycol):
    return emptycol > 0

def canGoRight(emptycol):
    return emptycol < 2

def getMovablePositions(emptyrow, emptycol):
    positions = []
    if canGoUp(emptyrow):
        positions.append((emptyrow-1, emptycol))
    if canGoDown(emptyrow):
        positions.append((emptyrow+1, emptycol))
    if canGoLeft(emptycol):
        positions.append((emptyrow, emptycol-1))
    if canGoRight(emptycol):
        positions.append((emptyrow, emptycol+1))
    return positions

def solve(board, emptyrow, emptycol):
    count = 0
    while manhattan(board) != 0 and count < 101:
        positions = getMovablePositions(emptyrow, emptycol)
        minManhattan = 20000000
        minMove = (-1,-1)
        for (i, j) in positions:
            board[i][j], board[emptyrow][emptycol] = board[emptyrow][emptycol], board[i][j]
            dist = manhattan(board)
            if dist <= minManhattan:
                minManhattan = dist
                minMove = (i, j)
            board[i][j], board[emptyrow][emptycol] = board[emptyrow][emptycol], board[i][j]
        if minMove == (-1,-1):
            print("Impossible")
            break
        #else:
            # printBoard(board)
            # sleep(5)
        
        board[minMove[0]][minMove[1]], board[emptyrow][emptycol] = board[emptyrow][emptycol], board[minMove[0]][minMove[1]]
        emptyrow, emptycol = minMove[0], minMove[1]
        count += 1

    if count < 101:
        print("----------------- Your required configuration has been reached!!! -----------------")
        printBoard(board)
    else:
        print()
        print("----------------- Sorry, This is not possible -----------------")
        

def start():
    board = [[0 for i in range(3)] for j in range(3)]
    print()
    print()
    printBoard(board)
    empty = int(input("Enter which position must be empty at the beginning : ")) - 1
    board[empty // 3][empty % 3] = -1
    print("Enter the board configuration : ")
    for i in range(3):
        for j in range(3):
            if board[i][j] != -1:
                board[i][j] = int(input("Position " + str(i*3 + j + 1) + " contains value : "))
    print()
    print("Initial Configuration of the board is : ")
    printBoard(board)
    print()
    print("Please give the final configuration of the matrix : ")
    #final = int(input("Which position should be empty(final) : "))
    for i in range(1, 9):
        pos = int(input("Position of " + str(i) + " (final) : ")) - 1
        mapping[i] = (pos // 3, pos % 3)
    solve(board, empty // 3, empty % 3)


start()
