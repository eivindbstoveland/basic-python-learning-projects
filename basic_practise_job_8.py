import random

def guess_game():
    best_score = None
    
    
    while True:
        number = random.randint(1,10)
        guesses = 0
        print(number)
        while True:
                
                number_guess = int(input('Please guess a number between 1 and 10:\n'))
                guesses +=1
                
                if not 1 <= number_guess <= 10:                
                    print('NB! you can only use numbers between 1 and 10!\n')
                    continue
                if number_guess < number:
                    print('Your number guess was too low!\n')
                elif number_guess > number:
                    print('Your number guess was too high!\n')
                elif number_guess == number:
                    print(f'Great, you guessed the correct number in only {guesses} guess/es!\n')
                    break
        if best_score is None or guesses < best_score:
            best_score = guesses
            print(f'Best guessing score is {best_score}')
        play_again = str(input('Do you want to play again? y/n\n'))
        if play_again.lower() != 'y':
            break
        else:
            print('Lets have another go')

guess_game()
            

