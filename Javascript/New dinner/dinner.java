
public static boolean isPerfect(int number) {
        if (number <= 1) return false;
        int sum = 1;
        for (int index = 2; index * index <= number; index++) {
            if (number % index == 0) {
                sum += index;
                if (index * index != number) sum += number / index;
            }
        }
        return sum == number;
    }
for (int index = 1; index <= 1000; index++) {
            if (isPerfect(index)) 
		System.out.print(index + " ");
        }

public static boolean isArmstrong(int number) {
	int realNumber = number;
	int sum = 0;
    	int digits = 0;
    	int checker = number;
   	if (checker == 0) {
        	digits = 1;
    	} else {
        	while (checker != 0) {
            		checker = checker / 10;
            		digits++;
        }
    } 	for (; num > 0; num /= 10) {
    		int digit = num % 10;
    		sum += Math.pow(digit, digits);
}        }
        return sum == realNumber;
    }

for (int index = 1; index <= 1000; index++) {
            if (isArmstrong(index)) 
		System.out.print(index + " ");
        }


public static boolean isStrong(int num) {
        int original = num, sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += factorial(digit);
            num /= 10;
        }
        return sum == original;
    }

int numberOne = 
int numberTwo = 
int greater = Math.max(numberOne, numberTwo);
int lcm = greater;
for (int index = greater; index <= numberOne * numberTwo; index += greater) {
	if (index % numberOne == 0 && index % numberTwo == 0) {
		lcm = index;
                break;



int checker = 1;
int result = 1;

for(checker = 1; checker <= numberCheck; checker++){
	 result = result * checker;
}
System.out.print("factorial is " +  result);
	}

}

public static boolean isLeapYear(int number){

boolean check = true;
		if (number % 4 == 0){
			check = true;
		}
		if (number % 100 == 0){
			check = true;
		}
		if (number % 400 == 0){
			check = true;
		}
		else{
			check = false;
		}
	return check;
	
}	}
