import java.util.Scanner;

public class Main {
	static int n;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); 
		n = scan.nextInt();
		
		for (int i = 0; i < 2*n-1; i++) {
			for (int j = 0; j < Math.abs(n-i-1); j++) {
				System.out.print(" ");
			}
			for (int j = 0; j < 2*n-1 - 2*Math.abs(n-i-1); j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

}
