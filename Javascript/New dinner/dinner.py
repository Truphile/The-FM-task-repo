number_one = int(input("Enter a number: ")):
number_two = int(input("Enter a number: ")):


gcd = 1
for index in range(1, min(number_one, number_two) + 1):
    if number_one % index == 0 and number_two % index == 0:
        gcd = index

print(gcd)

def is_perfect(number):
    if number <= 1:
        return False
    sum_divisors = 1
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            sum_divisors += index
            if index * index != num:
                sum_divisors += num // index
    return sum_divisors == num

print([index for index in range(1, 1001) if is_perfect(index)])


def is_armstrong(number):
    number_str = str(number)
    digits = len(number_str)
    sum_powers = sum(int(check) ** digits for check in number_str)
    return sum_powers == num

print([index for index in range(1, 1001) if is_armstrong(index)])


def get_factorial(number):
    if number < 0:
        return "invalid number"
    elif number == 0:
        return 1
    else:
        checker = 1
        for index in range(1, number + 1):
            checker *= index
        return checker


def factorial(digit):
    if digit == 0 or digit == 1:
        return 1
    result = 1
    for i in range(1, digit + 1):
        result *= i
    return result

def is_strong(number):
    num_as_string = str(number)
    sum_of_factorials = 0
    for digit in num_as_string:
        digit_value = int(digit)
        digit_factorial = factorial(digit_value)
        sum_of_factorials += digit_factorial
    if sum_of_factorials == number:
        return True
    else:
        return False


number_one = int(input("Enter a number: ")):
number_two = int(input("Enter a number: ")):

greater = max(number_one, number_two)
lcm = greater

for index in range(greater, number_one * number_two + 1, greater):
    if index % number_one == 0 and index % number_two == 0:
        lcm = index
        break

print(lcm)

def is_leap_year(number):
    if number % 4 == 0:
        if number % 100 == 0:
            if number % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_year(number):
    return (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0)

for year in range(1900, 2026):
    if is_leap_year(year):
        print(year)
