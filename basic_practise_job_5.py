def age():
    age_input = int(input('Please enter the number of your age: '))

    if age_input < 18:
        print('You are a minor!')
    elif 18 <= age_input <= 64:
        print('You are an adult!')
    else:
        print('Your a senior!')

age()

