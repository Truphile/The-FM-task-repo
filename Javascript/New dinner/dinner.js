const prompt = require('prompt-sync')();

let numberOne = parseInt(prompt("Enter a number: "));
let numberTwo = parseInt(prompt("Enter a number: "));

let gcd = 1;
for (let index = 1; index <= Math.min(numberOne, numberTwo); index++) {
    if (numberOne % index === 0 && numberTwo % index === 0) {
        gcd = index;
    }
}
console.log(gcd);

function isPerfect(number) {
    if (number <= 1) return false;
    let sumDivisors = 1;
    for (let index = 2; index <= Math.sqrt(number); index++) {
        if (number % index === 0) {
            sumDivisors += index;
            if (index * index !== number) sumDivisors += number / index;
        }
    }
    return sumDivisors === number;
}



function factorial(digit) {
    if (digit === 0 || digit === 1) return 1;
    let result = 1;
    for (let index = 1; index <= digit; i++) 
	result *= index;
    return result;
}

function getFactorial(number) {
    if (number < 0) return "invalid number";
    if (number === 0) return 1;
    let checker = 1;
    for (let index = 1; index <= number; index++) 
	checker *= index;
    return checker;
}

numberOne = parseInt(prompt("Enter a number: "));
numberTwo = parseInt(prompt("Enter a number: "));

let greater = Math.max(numberOne, numberTwo);
let lcm = greater;
for (let index = greater; index <= numberOne * numberTwo; index += greater) {
    if (index % numberOne === 0 && index % numberTwo === 0) {
        lcm = index;
        break;
    }
}
console.log(lcm);