
string_given = 'word'
reversed_string = ""

for check in string_given :
    reversed_string = check + reversed_string

print(reversed_string)


num = int(input("Enter an integer: "))

sign = -1 if num < 0 else 1
num *= sign  

reversed_num = int(str(num)[::-1]) * sign

print("Reversed number:", reversed_num)

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
	if number % 2 == 0:
		even_sum += number
print(even_sum)

numbers = '324576'
odd_sum = 0
for number in numbers:
	if number % 2 != 0:
		odd_sum += number
print(odd_sum)


#for count in range(1,100):
	#if count % 2 != 1:


word = '67876'
word_check = len(word)
for check in range(word_check // 2):
	if word[check] == word[word_check - 1 - check]:
		check = word
print(check)
           










