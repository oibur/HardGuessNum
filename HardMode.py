import random
import time

def main():
    comp_guess, comp_guesses, comp_low, comp_high, comp_num = 0, 1, 1, 10000, random.randint(1, 10000)
    human_guess, human_guesses, human_low, human_high = 0, 1, 0, 10000
    human_num = int(input('Can you human_guess the computer\'s number before it guesses yours?\nEnter a number between 1 and 10,000 for the computer to guess: '))

    while True:
        human_guess = int(input(f'Attempt {human_guesses}, Guess a number between {human_low} and {human_high}: '))
        time.sleep(.5)

        if human_guess > comp_num:
            human_high = human_guess
            human_guesses += 1
            print(f'Sorry, {human_guess} is too high')
            time.sleep(.5)

        elif human_guess < comp_num:
            human_low = human_guess
            human_guesses += 1
            print(f'Sorry, {human_guess} is too low')
            time.sleep(.5)

        elif human_guess == comp_num:
            print(f'You win. It took {human_guesses} attempts for you to guess the computer\'s number was {comp_num}')
            time.sleep(.5)
            break


        #easy difficulty:
        #comp_guess = random.randint(comp_low, comp_high)
        #hard difficulty:
        comp_guess = comp_low + int((comp_high - comp_low) / 2)
        print(f'Attempt {comp_guesses}, between {comp_low} and {comp_high}, the computer guesses: {comp_guess}')
        time.sleep(.5)

        if comp_guess > human_num:
            comp_high = comp_guess
            comp_guesses += 1
            print(f'{comp_guess} was too high')
            time.sleep(.5)

        elif comp_guess < human_num:
            comp_low = comp_guess
            comp_guesses += 1
            print(f'{comp_guess} was too low')
            time.sleep(.5)

        elif comp_guess == human_num:
            print(f'You lose. It took the computer {comp_guesses} tries to guess your number was {human_num}')
            time.sleep(.5)

if __name__ == '__main__':
    main()