public class DinnerTask{
	public static void main(String[] args){
	
	for(int even = 1; even <= 100; even++){
		if (even % 2 == 0){
		System.out.print("This are even numbers from 1 to 100: " + even + " ");
	}
}
	for(int odd = 50; odd <= 100; odd++){
		if(odd % 2 != 0){
		System.out.println("This are odd numbers from 50 to 100: " + odd + " ");
	}
}
	for(int numbers = 1; numbers <= 100; numbers++){
		System.out.print("This are numbers from 1 to 100: " + numbers + " ");
	}

	for(int count = 0; count <= 20; count++){
		int square = count * count;
		System.out.print("This are the square of numbers from 1 to 200: " + square + " ");
}
	for(int number = 1; number <= 50; number++){
		if (number % 3 == 0){
		System.out.println("This are the multiples of 3 between 1 and 50: " + number + " ");
	}
}
	for (int number = 0; number <= 100; number++){
		if (number % 3 == 0 && number % 5 == 0){
		System.out.print(number + " ");
		}
	}
	int counter = 0;
	for(int count = 1; count <= 100; count++){
		if (count % 7 == 0){
		counter++;
	}	
}
	System.out.println(counter);
	
	int sum = 0;
	for(int number = 1; number <= 50; number++){
		sum += number;
	}
	System.out.print(sum);

	int product = 0;
	for(int number = 1; number <= 10; number++){
		product *= number;
	}
	System.out.println (product);

	for(char character = 'A'; character <= 'Z'; character++){
	System.out.print(character + " ");
	}
	

	int number = 0;
	int multiplication = 0;
	for(int count = 0; count <= 12; count++){
	multiplication = count * 4;
	System.out.println(multiplication);
	}
	

	char character = 'e';
	int characters = 0;
	String words = "shallee";
	
	for(int count = 0; count < words.length(); count++){
	char letters = words.charAt(count);
	if (letters == character){
		characters++;
	}
	
}	System.out.print(characters);


	 String text = "WINDOWS";

        for (int index = 0; index < text.length(); index++) {
            char lowercaseChar = Character.toLowerCase(text.charAt(index));
            System.out.println(lowercaseChar);
        }

 	String text = "WINDOWS";

        for (int index = 0; index < text.length(); index++) {
            char upperCaseChar = Character.toUpperCase(text.charAt(index));
            System.out.println(upperCaseChar);
        }
	
	String number = "45";
        int sum = 0;

       for int i = 0; i < number.length(); i++) {
            sum += Character.getNumericValue(number.charAt(i));
        }

        System.out.println(sum);

	String word = "aeroplane";

	int check_a = 0; int check_e = 0; 
	int check_i = 0; int check_o = 0; 
	int check_u = 0;

	for (int count = 0; count < word.length(); count++) {
	char check = Character.toLowerCase(word.charAt(count));
		if (check == 'a'){
			check_a += 1;
		}
		if (check == 'e'){
			check_e += 1;
		}
		if (check == 'i'){
			check_i += 1;
		}
		if (check == 'o'){
			check_o += 1;
		}
		if (check == 'u'){
			check_u += 1;
		}
	}
	int checker = check_a + check_e + check_i + check_o + check_u;

	System.out.print(checker);

	String word = "Makwochukwu";

	for (int i = 0; i < word.length(); i++) {
		char checker = word.charAt(i);
		System.out.print(checker);
		}

	 String number = "32";
        char largestDigit = number.charAt(0);

        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) > largestDigit) {
                largestDigit = number.charAt(i);
            }
        }

        System.out.println("Largest digit: " + largestDigit);
    }


	String number = "54";
        char smallestDigit = number.charAt(0);

        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) < smallestDigit) {
                smallestDigit = number.charAt(i);
            }
        }

        System.out.println(smallestDigit);
    }















































}	
}