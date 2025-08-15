import random
def guess_number_log():
    
    number = random.randint(1,10)
    print(number)
    guesses = 0
    while True:
        guess = int(input('Please guess a number from 1 to 10:\n'))
        guesses +=1
        if not 1 <= guess <=10:
            
            print('Remember, only enter a number from 1 to 10.\n')
            continue
       
        if guess == number:
            print('Fantastic, you guessed correctly!\n')
            print(f'You had total of {guesses} guesses.\n')
            break
        elif guess < number:
            print('Your number was too low!')
            
        else:
            print('Your number was too high')
        
    
        
    
guess_number_log()
