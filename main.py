from os import system
from sys import platform

CLEAR_SCREEN = 'cls' if platform == 'win32' else 'clear'
CHOICES = '''Operators:
 1. +
 2. -
 3. *
 4. /
 5. %
 0. Exit
'''
OPERATORS = {
    1: '+',
    2: '-',
    3: '*',
    4: '/',
    5: '%'
}
operator = firstNumber = secondNumber = answer = None


def chooseOperation():
    error = False
    while True:
        print_progress()
        print(CHOICES)
        if error:
            print('Error: Invalid input')
            print('Choose again: ', end='')
            error = False
        else:
            print('Choose: ', end='')
        try:
            choice = int(input())
            if choice not in range(len(OPERATORS)+1):
                raise IndexError()
            return choice
        except:
            error = True
            continue


def enterNumber(number_to_enter=''):
    error = False
    while True:
        print_progress()
        if error:
            print('Error: Invalid input')
            print(f'Enter {number_to_enter} number again: ', end='')
            error = False
        else:
            print(f'Enter {number_to_enter} number: ', end='')
        try:
            number = float(input())
            if number.is_integer():
                number = int(number)
            return number
        except:
            error = True
            continue


def calculate(operator, firstNumber, secondNumber):
    try:
        return eval(f'{firstNumber}{operator}{secondNumber}')
    except Exception as e:
        return e


def print_progress():
    system(CLEAR_SCREEN)
    if operator != None:
        print("Operator:", operator)
    if firstNumber != None:
        print('First number:', firstNumber)
    if secondNumber != None:
        print('Second number:', secondNumber)
    if answer != None:
        print('Answer: ', answer)


def main():
    global operator, firstNumber, secondNumber, answer
    while True:
        choice = chooseOperation()
        if choice == 0:
            break
        operator = OPERATORS[choice]
        firstNumber = enterNumber('First')
        secondNumber = enterNumber('Second')
        answer = calculate(operator, firstNumber, secondNumber)
        print_progress()

        input("\nPress Enter to continue...")
        operator = firstNumber = secondNumber = answer = None


if __name__ == '__main__':
    main()
    system(CLEAR_SCREEN)
    print("Arigathanks!")
