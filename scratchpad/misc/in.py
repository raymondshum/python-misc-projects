import random

PATH = "NONEXIST"

def wordSearch(word):
    with open(PATH) as file:
        lines = file.readlines()

    for line in lines:
        if word in line:
            return True
    
    return False

def print_result(result):
    conditional = "exists" if result else "doesn't exist"
    print(f"the word {conditional}")

def main():
    nonexistent_word = 'aacn'
    existing_word = 'aacr'
    result = wordSearch(nonexistent_word)
    print_result(result)
    result = wordSearch(existing_word)
    print_result(result)

if __name__ == '__main__':
    main()