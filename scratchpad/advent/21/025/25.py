from scratchpad.advent.utils.utils import Utils
from pprint import pprint

class Cucumber:
    def __init__(self, type):
        if not self.isValidCucumber(type):
            print("Incorrect type:", type)
            raise ValueError(f'Incorrect cucumber type: {type}')
        
        self.can_move = False
        self.moved = False
        self.type = type
    
    def isValidCucumber(self, type):
        return type == "v" or type == ">"
    
    def __str__(self):
        return self.type

class Game():
    def __init__(self, initial_board):
        self.board = initial_board
        self.step_count = 0
    
    def display_board(self):
        for row_index, row in enumerate(self.board):
            print(row_index, end = " ")
            for col_index, col in enumerate(row):
                cell = self.board[row_index][col_index]
                print(cell,end="")
            print("")
                    
    def step(self):
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if isinstance(col, Cucumber) and not col.moved and col.type == ">" :
                    east = (col_index + 1) % len(row)
                    if self.board[row_index][east] == ".":
                        col.can_move = True
                    else:
                        col.can_move = False
                        
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if isinstance(col, Cucumber) and not col.moved and col.type == ">" :
                    if col.can_move:
                        east = (col_index + 1) % len(row)
                        moved_cucumber = Cucumber(">")
                        self.board[row_index][east] = moved_cucumber
                        self.board[row_index][col_index] = "."
                        moved_cucumber.moved = True
        
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if isinstance(col, Cucumber) and not col.moved and col.type == "v":
                    south = (row_index + 1) % len(self.board)
                    if self.board[south][col_index] == ".":
                        col.can_move = True
                    else: 
                        col.can_move = False
                        
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if isinstance(col, Cucumber) and not col.moved and col.type == "v":
                    if col.can_move:
                        south = (row_index + 1) % len(self.board)
                        moved_cucumber = Cucumber("v")
                        self.board[south][col_index] = moved_cucumber
                        self.board[row_index][col_index] = "."
                        moved_cucumber.moved = True
                        
        cucumber_moved = self.cucumberMoved()
        self.reset_cucumbers()
        self.step_count += 1
        return cucumber_moved
    
    def reset_cucumbers(self):
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if isinstance(col, Cucumber):
                    col.moved = False
    
    def show_all_moves(self, hide = False):
        cucumber_moved = True
        while cucumber_moved:
            cucumber_moved = self.step()
            if not hide:
                print(f"Step: {self.step_count}")
                self.display_board()
                print("")
        return self.step_count
    
    def cucumberMoved(self):
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if isinstance(col, Cucumber):
                    if col.moved:
                        return True
        return False
    
    @staticmethod
    def format_board(board):
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                cell = board[row_index][col_index].strip()
                type = cell if cell != "." else None
                if type:
                    board[row_index][col_index] = Cucumber(type)
        return board
    
def main():
    file_path = r"C:\Users\rshum\Documents\CSUMB\Misc Projects\python\scratchpad\advent\025\input.txt"
    input = Utils.read_file(file_path)
    input = [[*line.strip().replace("\n", "")] for line in input]

    board = Game.format_board(input)

    my_game = Game(board)
    num = my_game.show_all_moves(hide=True) 
    print(num)   
    
    

if __name__ == '__main__':
    main()