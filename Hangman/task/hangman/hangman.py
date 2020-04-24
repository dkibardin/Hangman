from random import choice
import string

riddle = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")
answer = choice(riddle)
hint = "-" * (len(answer))
letter_set = set(answer)
tries = 8
user_guesses = []


def ft_check_input(char):
    user_guesses.append(char)
    if len(char) != 1:
        return "You should print a single letter"
    elif char not in string.ascii_lowercase:
        return "It is not an ASCII lowercase letter"
    elif user_guesses.count(char) > 1:
        return "You already typed this letter"
    return 0


def ft_game():
    global answer, hint, tries
    while tries > 0:
        print(f'\n{hint}')
        if "-" not in hint:
            print("""You guessed the word!
You survived!""")
            break
        char = input('Input a letter: ')
        if ft_check_input(char) != 0:
            print(ft_check_input(char))
            continue
        if char in letter_set:
            counter = 0
            for n in answer:
                if char == n:
                    hint = list(hint)
                    hint[counter] = n
                    hint = "".join(hint)
                counter += 1
        else:
            print("No such letter in the word")
            tries -= 1
    else:
        print("You are hanged!")


def ft_menu():
    while True:
        menu = input('Type "play" to play the game, "exit" to quit: ')
        if menu == "play":
            ft_game()
        elif menu == "exit":
            break
        else:
            continue


ft_menu()
