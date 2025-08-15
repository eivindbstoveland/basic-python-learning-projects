import random
def guess_number():
    number = random.randint(1,10)
    
    while True:
        
        print(number) # just for checking that code actually works
        guess = int(input('Please guess a number between 1 and 10, and see if you got it right? \n'))
        
        if number == guess:
            print('Great, you guessed correctly!\n')
            break 
        elif guess < number:
            print('Your number was too low, try again..')
        else:
            print('Your number was too high, try again..')
        
            
        
            

guess_number()
