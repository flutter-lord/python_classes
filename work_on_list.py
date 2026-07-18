import random
NUMBER_OF_CHAR = 100

def get_char():
    all_character = []
    for i in range(NUMBER_OF_CHAR):
        char = chr(random.randint(ord("a"), ord("z")))
        all_character.append(char)
    return all_character

def print_all():
    for j in range(NUMBER_OF_CHAR):
        if j % 10 == 0 and j != 0:
            print("")
        print(get_char()[j], end= " ")

def count_char():
    for k in range(26):
        character = chr(ord("a") + k)
        count = get_char().count(character)
        if k % 10 == 0 and k != 0:
            print("")
        print(f"{count} {character}\'s", end= ", ")

def main():
    print_all()
    print("")
    count_char()

main()