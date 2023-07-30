

import java.util.Scanner;

public class Main {
	static int[][] arr;
	static int m, r, c;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		arr = new int[9][9];
		m = -100001;
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				arr[i][j] = scan.nextInt();
				if (m < arr[i][j]) {
					m = arr[i][j];
					r = i+1;
					c = j+1;
				}
			}
		}
		
		System.out.println(m);
		System.out.println(r + " " + c);
	}

}
