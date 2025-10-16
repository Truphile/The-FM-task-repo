public class TaskBreakFast {
    public static void main(String[] args) {
        
        String stringGiven = "word";
        String reversedString = "";

        for (int i = 0; i < stringGiven.length(); i++) {
            reversedString = stringGiven.charAt(i) + reversedString;
        }
        System.out.println(reversedString);


        
        String word = "AveCeLa";
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                count++;
            }
        }
        System.out.println(count);

	
	
	int number = 12345;
        int reversed = 0;

        for (; number != 0; number /= 10) {
            int digit = number % 10;
            reversed = reversed * 10 + digit;
        }

        System.out.print(reversed);

        
        count = 0;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c >= 'a' && c <= 'z') {
                count++;
            }
        }
        System.out.println(count);


        
        String numbers = "54654";
        int length = numbers.length();
        int countNum = 0;
        for (int i = 0; i < numbers.length(); i++) {
            countNum++;
        }
        System.out.println("Length: " + length + ", Count: " + countNum);


       
        String vowels = "aeiou";
        word = "malagedone";
        int index = -1;
        for (int i = 0; i < word.length(); i++) {
            if (vowels.indexOf(word.charAt(i)) >= 0) {
                index = i;
                break;
            }
        }
        System.out.println("First vowel index: " + index);


        
        int sum = 0;
        double average = 0;
        for (int i = 0; i < 100; i++) {
            sum += i;
        }
        average = (double) sum / 100;
        System.out.println(average);


        
        numbers = "324576";
        int evenSum = 0;
        for (int i = 0; i < numbers.length(); i++) {
            int num = numbers.charAt(i) - '0';
            if (num % 2 == 0) {
                evenSum += num;
            }
        }
        System.out.println(evenSum);


        
        int oddSum = 0;
        for (int i = 0; i < numbers.length(); i++) {
            int num = numbers.charAt(i) - '0';
            if (num % 2 != 0) {
                oddSum += num;
            }
        }
        System.out.println(oddSum);


        
        word = "67876";
        int wordCheck = word.length();
        boolean isPalindrome = true;
        for (int i = 0; i < wordCheck / 2; i++) {
            if (word.charAt(i) != word.charAt(wordCheck - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }
        System.out.println("Is palindrome: " + isPalindrome);


        
        int base = 5;
        int exponent = 4;
        int power = 1;
        for (int i = 0; i < exponent; i++) {
            power *= base;
        }
        System.out.println(power);


        
        for (int number = 2; number <= 100; number++) {
            boolean isPrime = true;
            for (int fact = 2; fact <= Math.sqrt(number); fact++) {
                if (number % fact == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(number + " ");
            }
        }
        System.out.println();


        
        for (int number = 2; number <= 100; number++) {
            int facts = 0;
            for (int fact = 2; fact <= Math.sqrt(number); fact++) {
                if (number % fact == 0) {
                    facts++;
                }
            }
            System.out.print(facts + " ");
        }


         
        String[] binaryNumbers = {"100", "101", "1101", "111", "11111111", "110", "10010", "1000"};
        for (String binary : binaryNumbers) {
            int decimalNum = Integer.parseInt(binary, 2);
            System.out.print(binary + " : " + decimalNum + "  ");
        }
      
	System.out.println();


	  
    }
}
