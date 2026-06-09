import random

def guess_the_number(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You\'re a genius.')
            return True
    else:
        print('Hey bozo! I said 1~10.')
        return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number between 1 and 10: '))
            if guess_the_number(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
