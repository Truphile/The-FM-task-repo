for even in range(1, 101):
    if even % 2 == 0:
        print("This are even numbers from 1 to 100:", even, end=" ")

for odd in range(50, 101):
    if odd % 2 != 0:
        print("This are odd numbers from 50 to 100:", odd)

for numbers in range(1, 101):
    print("This are numbers from 1 to 100:", numbers, end=" ")

for count in range(0, 21):
    square = count * count
    print("This are the square of numbers from 1 to 200:", square, end=" ")

for number in range(1, 51):
    if number % 3 == 0:
        print("This are the multiples of 3 between 1 and 50:", number)

for number in range(0, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, end=" ")

counter = 0
for count in range(1, 101):
    if count % 7 == 0:
        counter += 1
print(counter)

sum = 0
for number in range(1, 51):
    sum += number
print(sum)

product = 0
for number in range(1, 11):
    product *= number
print(product)

for character in range(ord('A'), ord('Z') + 1):
    print(chr(character), end=" ")

number = 0
multiplication = 0
for count in range(0, 13):
    multiplication = count * 4
    print(multiplication)

character = 'e'
characters = 0
words = "shallee"
for count in range(0, len(words)):
    letters = words[count]
    if letters == character:
        characters += 1
print(characters)


text = "WINDOWS"

for index in range(len(text)):
    lowercase_char = text[index].lower()
    print(lowercase_char)

text = "WINDOWS"

for index in range(len(text)):
    upper_case_char = text[index].upper()
    print(upper_case_char)

number = "45"
sum = 0

for digit in number:
    sum += int(digit)

print(sum)

number = "32"
largest_digit = number[0]

for digit in number:
    if digit > largest_digit:
        largest_digit = digit

print("Largest digit:", largest_digit)


number = "54"
smallest_digit = number[0]

for digit in number:
    if digit < smallest_digit:
        smallest_digit = digit

print(smallest_digit)
