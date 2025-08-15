def highest_number():
    user_input = input('Please enter 3 digits: \n').split()
    numbers_list = [int(number) for number in user_input]
    peak_number = (max(numbers_list))
    print(f'The highest number entered was {peak_number}.\n')


highest_number()
