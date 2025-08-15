def odd_or_even():
    number = int(input('Please enter any number for me to check: '))
    if number % 2 == 0:
        print('The number entered is an even number.')
    else:
        print('The number entered is an odd number.')

odd_or_even()