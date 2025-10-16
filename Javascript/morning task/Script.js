
let stringGiven = 'word';
let reversedString = '';
for (let i = 0; i < stringGiven.length; i++) {
    reversedString = stringGiven[i] + reversedString;
}
console.log(reversedString);



let word = 'AveCeLa';
let count = 0;
for (let i = 0; i < word.length; i++) {
    let counter = word[i];
    if (counter >= 'A' && counter <= 'Z') {
        count++;
    }
}
console.log(count);



let number = 12345;
let reversed = 0;

for (; number !== 0; number = Math.floor(number / 10)) {
    let digit = number % 10;
    reversed = reversed * 10 + digit;
}

console.log("Reversed:", reversed);





count = 0;
for (let i = 0; i < word.length; i++) {
    let counter = word[i];
    if (counter >= 'a' && counter <= 'z') {
        count++;
    }
}
console.log(count);




let numbers = "54654";
let length = numbers.length;
let lastChar = numbers[numbers.length - 1];
console.log("Length:", length, ", Last Char:", lastChar);



const vowels = "aeiou";
word = "malagedone";
let firstVowelIndex = -1;
for (let i = 0; i < word.length; i++) {
    if (vowels.includes(word[i])) {
        firstVowelIndex = i;
        break;
    }
}
console.log("First vowel index:", firstVowelIndex);



let sum = 0;
for (let i = 0; i < 100; i++) {
    sum += i;
}
let average = sum / 100;
console.log(average);



numbers = '324576';
let evenSum = 0;
for (let i = 0; i < numbers.length; i++) {
    let number = parseInt(numbers[i]);
    if (number % 2 === 0) {
        evenSum += number;
    }
}
console.log(evenSum);



let oddSum = 0;
for (let i = 0; i < numbers.length; i++) {
    let number = parseInt(numbers[i]);
    if (number % 2 !== 0) {
        oddSum += number;
    }
}
console.log(oddSum);


 
word = "67876";
let wordLength = word.length;
let isPalindrome = true;
for (let i = 0; i < wordLength / 2; i++) {
    if (word[i] !== word[wordLength - 1 - i]) {
        isPalindrome = false;
        break;
    }
}
console.log("Is palindrome:", isPalindrome);



let base = 5;
let exponent = 4;
let power = 1;
for (let i = 0; i < exponent; i++) {
    power *= base;
}
console.log(power);



for (let number = 2; number <= 100; number++) {
    let isPrime = true;
    for (let fact = 2; fact <= Math.sqrt(number); fact++) {
        if (number % fact === 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        console.log(number + " ");
    }
}
console.log();



for (let number = 2; number <= 100; number++) {
    let factorCount = 0;
    for (let fact = 2; fact <= Math.sqrt(number); fact++) {
        if (number % fact === 0) {
            factorCount++;
        }
    }
   console.log(factorCount + " ");
}
console.log();



const binaryNumbers = ["100", "101", "1101", "111", "11111111", "110", "10010", "1000"];
for (let binary of binaryNumbers) {
    let decimalNum = parseInt(binary, 2);
    console.log(`${binary} : ${decimalNum}  `);
}
console.log();
