from scratchpad.advent.utils.utils import Utils

class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
    
    def move(self, command):
        direction, distance = command.split(" ")
        distance = int(distance)
        if direction == "forward":
            self.move_forward(distance)
        elif direction == "down":
            self.move_down(distance)
        elif direction == "up":
            self.move_up(distance)
        else:
            print("Unrecognized direction:", direction)
    
    def move_forward(self, distance):
        self.horizontal_position += distance
    
    def move_down(self, distance):
        self.depth += distance
    
    def move_up(self, distance):
        self.depth -= distance
    
    def get_result(self):
        return self.horizontal_position * self.depth
    
    def execute_commands(self, commands):
        for command in commands:
            self.move(command)
        print(self.get_result())


class AttackSubmarine(Submarine):
    
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move_forward(self, distance):
        super().move_forward(distance)
        self.depth += self.aim * distance
    
    def move_down(self, distance):
        self.aim += distance
    
    def move_up(self, distance):
        self.aim -= distance


def main():
    file_path = r"C:\Users\rshum\Documents\CSUMB\Misc Projects\python\scratchpad\advent\002\input.txt"
    input = Utils.read_file(file_path)
    input = [line.strip().replace("\n", "") for line in input]
    
    my_sub = Submarine()
    my_sub.execute_commands(input)
    
    my_attack_sub = AttackSubmarine()
    my_attack_sub.execute_commands(input)
if __name__ == '__main__':
    main()