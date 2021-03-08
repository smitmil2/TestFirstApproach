def is_fizz(num):
    return num % 3 == 0

def is_buzz(num):
    return num % 5 == 0

def fizzbuzz(num):
    if is_fizz(num) and is_buzz(num):
        return 'FizzBuzz'
    elif is_fizz(num):
        return 'Fizz'
    elif is_buzz(num):
        return 'Buzz'
    else:
        return num


for i in range(1, 101):
    print(fizzbuzz(i))
