for even in range(1, 101):
    if even % 2 == 0:
        print(even, end=" ")

for odd in range(50, 101):
    if odd % 2 != 0:
        print(odd, end=" ")

for numbers in range(1, 101):
    print(numbers, end=" ")

for count in range(0, 21):
    square = count * count
    print(square, end=" ")

for number in range(1, 51):
    if number % 3 == 0:
        print(number, end=" ")

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
    print(multiplication, end=" ")

character = 'e'
characters = 0
words = "shallee"
for count in range(0, len(words)):
    letters = words[count]
    if letters == character:
        characters += 1
print(characters, end=" ")


text = "WINDOWS"

for index in range(len(text)):
    lowercase_char = text[index].lower()
    print(lowercase_char, end=" ")

text = "WINDOWS"

for index in range(len(text)):
    upper_case_char = text[index].upper()
    print(upper_case_char, end=" ")

number = "45"
sum = 0

for digit in number:
    sum += int(digit)

print(sum)

word = "aeroplane"

"""
vowels = aeiou
"""
check_a = 0 
check_e = 0
check_i = 0
check_o = 0
check_u = 0

for check in word.lower():
	if check == "a":
		check_a += 1
	if check == "e":
		check_e += 1
	if check == "i":
		check_i += 1
	if check == "o":
		check_o += 1
	if check == "u":
		check_u += 1
checker = check_a + check_e + check_i + check_o + check_u

print("Number of vowels: ", checker, end=" ")

word = "Makwochukwu"

for checker in word:
	print(checker, end=" ")


number = "32"
largest_digit = number[0]

for digit in number:
    if digit > largest_digit:
        largest_digit = digit

print("Largest digit:", largest_digit, end=" ")


number = "54"
smallest_digit = number[0]

for digit in number:
    if digit < smallest_digit:
        smallest_digit = digit

print("Smallest digit:", smallest_digit, end=" ")
