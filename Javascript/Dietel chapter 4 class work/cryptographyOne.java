import java.util.Scanner;

public class cryptographyOne{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a four digit integer: ");
		String number = input.nextLine();


        int[] userKeys = new int[4];
        for (int index = 0; index < 4; index++) {
            userKeys[index] = (Character.getNumericValue(userKey.charAt(index)) + 7) % 10;
        }

        int numberSwap = userKeys[0];
        userKeys[0] = userKeys[2];
        userKeys[2] = numberSwap;

        numberSwap = userKeys[1];
        userKeys[1] = userKeys[3];
        userKeys[3] = numberSwap;

        System.out.print("Encrypted key: ");
        for (int index = 0; index < 4; index++) {
            System.out.print(userKeys[index]);
        }
        System.out.println();

       numberSwap = userKeys[0];
        userKeys[0] = userKeys[2];
        userKeys[2] = numberSwap;

        numberSwap = userKeys[1];
        userKeys[1] = userKeys[3];
        userKeys[3] = numberSwap;

        int[] decryptedKey = new int[4];
        for (int index = 0; index < 4; i++) {
            decryptedKey[index] = (userKeys[index] - 7 + 10) % 10;
        }

        System.out.print("Decrypted key: ");
        for (int index = 0; index < 4; index++) {
            System.out.print(decryptedKey[index]);
        }
    }
}
