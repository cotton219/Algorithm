

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int n, m;
	static int[][] arr1;
	static int[][] arr2;
	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(System.in);
		
		n = scan.nextInt();
		m = scan.nextInt();
		
		arr1 = new int[n][m];
		arr2 = new int[n][m];
		
		for (int i =0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr1[i][j] = scan.nextInt();
			}
		}
		for (int i =0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr2[i][j] = scan.nextInt();
			}
		}
		
		for (int i =0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				System.out.print(arr1[i][j] + arr2[i][j] + " ");
			}
			System.out.println();
		
		}
		
	}

}
