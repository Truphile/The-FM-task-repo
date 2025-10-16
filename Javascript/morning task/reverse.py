
string_given = 'word'
reversed_string = ""

for check in string_given :
    reversed_string = check + reversed_string

print(reversed_string)


word = 'AveCeLa'
count = 0
for char in word:
    if 'A' <= char <= 'Z':
        count += 1
print(count)


word = 'AveCeLa'
count = 0
for char in word:
    if 'a' <= char <= 'z':
        count += 1
print(count)



numbers = "54654"

for count in numbers:
	len(numbers) == count
	count = len(numbers),count
print(count)


vowel = 'aeiou'
word = 'malagedone'

for index in word:
	if word > vowel:
		index = 0

sum = 0
average = 1
for count in range(100):
	sum += count
	average = sum / 100
print(average)

numbers = '324576'
even_sum = 0
for number in numbers:
	if int(number) % 2 == 0:
		even_sum += int(number)
print(even_sum)

numbers = '324576'
odd_sum = 0
for number in numbers:
	if int(number) % 2 != 0:
		odd_sum += int(number)
print(odd_sum)


#for count in range(1,100):
	#if count % 2 != 1:


word = '67876'
word_check = len(word)
for check in range(word_check // 2):
	if word[check] == word[word_check - 1 - check]:
		check = word
print(check)
           

base = 5
exponent = 4
power = 1

for _ in range(base):
	power = base**exponent
print(power)
	 

for number in range(2, 101):  
	#number < 1 is not prime)
    is_prime = True  

    for facts in range(2, int(number ** 0.5) + 1): 
        if number % facts == 0:
            is_prime = False
            break 
    if is_prime:
        print(number, end=" ")

facts = 0
for number in range(2, 101):
	is_prime = True  

for facts in range(2, int(number ** 0.5) + 1):
	if number % facts == 0:
		is_prime = False
		facts+1
		break 

print(facts, end=" ")


binary_numbers = ["100","101", "1101", "111","11111111", "110","10010", "1000"]

for check in binary_numbers:
	decimal_num = int(check, 2)
	print(f"{check} : {decimal_num}", end=" ")
  
