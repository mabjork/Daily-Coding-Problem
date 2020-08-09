import math

def round_number(number, up):
    if(up == True):
        return math.ceil(number)
    else:
        return math.floor(number)

def round_numbers(numbers):
    rounded_numbers = []
    balance = 0
    for number in numbers:
        rounded_number = round(number)
        difference = number - rounded_number
        balance += difference
    print(balance)

numbers = [1.3, 2.3, 4.4]

round_numbers
        
