from datetime import datetime



def hello_python():
    name = input('Please enter your name: ')
    now = datetime.now()
    present = now.strftime('%H:%M:%S')
    if name.strip():
        print('')
        print(f'Hello {name}\n')
        print(f'The time is now {present}, just in case you wondered;)\n')
    else:
        print('Did you enter your name? If not, try again.')
        

hello_python()
