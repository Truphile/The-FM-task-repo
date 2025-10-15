public class BreakfastScript{
	public static void main(String[] args){
int number = 100;
boolean check = true;
	for(int i = 2; i <= number; i++){
		if (100 % i == 0){
			check = false;
			break;
		}
if(check){	
System.out.println(number + " ");
}else{ 
System.out.print(number + " ");
		}
	}
}
}