# write your code here
import random
import re


def coord_to_n(x: int, y: int):
    return (3 - y) * 3 + (x - 1)


def coordIntCheck(coord):
    for n in coord:
        if not n.isdigit():
            print('You should enter numbers!')
            return False
    return True


def coordRangeCheck(coord):
    for n in coord:
        if not 0 < int(n) < 4:
            print('Coordinates should be from 1 to 3!')
            return False
    return True


class Tictac:
    board = []
    cells = ''
    coord = ''
    series = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    players = {}

    def setCells(self):
        self.cells = list('_' * 9)

    def boardlineText(self):
        return [['0', '1', '2'],
                ['3', '4', '5'],
                ['6', '7', '8'],
                ['0', '3', '6'],
                ['1', '4', '7'],
                ['2', '5', '8'],
                ['0', '4', '8'],
                ['2', '4', '6']
                ]

    def boardLines(self):
        return [[self.cells[int(n)] for n in i] for i in self.boardlineText()]

    def printBoard(self):
        print('-' * 9)
        for i in [self.cells[0:3], self.cells[3:6], self.cells[6:9]]:
            print('| {} {} {} |'.format(i[0], i[1], i[2]))
        print('-' * 9)

    def coordCheck(self, coord, sign, player):
        check = False
        if coordIntCheck(coord):
            if coordRangeCheck(coord):
                if not self.boardCheck(coord, player):
                    self.cells[coord_to_n(int(coord[0]), int(coord[1]))] = sign
                    self.printBoard()
                    check = True
        return check

    def boardCheck(self, coords, player):
        occupied = self.cells[coord_to_n(int(coords[0]), int(coords[1]))] in ["X", "O"]
        if occupied and player == 'user':
            print("This cell is occupied! Choose another one!")
        return occupied

    def getWinner(self, sign):
        for l in self.boardLines():
            if not any(n for n in l if n != sign):
                return True

    def randomMove(self, mark):
        xValue = random.randint(1, 3)
        yValue = random.randint(1, 3)
        if not self.coordCheck([str(xValue), str(yValue)], mark, ''):
            self.randomMove(mark)

    def mediumMove(self, mark):
        if not self.twoInARow(mark):
            self.randomMove(mark)


    def hardMove(self, mark):



    def twoInARow(self, mark):
        test = False
        for i in self.boardlineText():
            line = ''
            for n in i:
                line += self.cells[int(n)]
            if line.count(mark) == 2:
                for n in i:
                    if self.cells == '_':
                        self.cells[int(n)] = mark
                        test = True
        return test

    def aiMove(self, level, mark):
        print("Making move level \"{}\"".format(level))
        self.aiLevels[level](self, mark)

    def userMove(self, mark):
        coord = input('Enter the coordinates: ').split()
        if self.coordCheck(coord, mark, 'user') is True:
            return
        self.userMove(mark)

    def gamePosition(self):
        winnerX = self.getWinner('X')
        winnerO = self.getWinner('O')
        finished = True
        if winnerX and winnerO:
            print("Impossible!")
        elif winnerX:
            print('X wins')
        elif winnerO:
            print('O wins')
        elif self.cells.count('_') != 0:
            finished = False
        else:
            print("Draw")
        return finished

    def setPlayers(self, players):
        X, O = players
        self.players = {
            'X': X,
            'O': O
        }

    def start(self):
        for mark in self.series:
            player = self.players[mark]
            if player == 'user':
                self.userMove(mark)
            else:
                self.aiMove(player, mark)

            finished = self.gamePosition()
            if finished:
                break

    def run(self):
        cmd = input('Input command:').split()
        if len(cmd) == 3 and all(n for n in cmd if n in ['start', 'exit', 'user', 'easy', 'medium']):
            if cmd[0] == 'start':
                self.setPlayers(cmd[1:3])
                self.start()
        else:
            print("Bad parameters!")

    aiLevels = {
        'easy': randomMove,
        'medium': mediumMove
    }


t = Tictac()
t.setCells()
t.run()