

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static double x;
	static int cnt, max;
	static int[] arr;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		arr = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		max = 0;
		
		for (int i = 0; i < n; i++) {
			cnt = 0;
			x = 0;
			
			for (int j = i-1; j >= 0; j--) {
				double angle = (double)(arr[i] - arr[j])/(i - j);
				if (j == i-1 || x > angle) {
					x = angle;
					cnt++;
				}
			}
			
			for (int j = i+1; j < n; j++) {
				double angle = (double)(arr[i] - arr[j])/(i - j);
				if (j == i+1 || x < angle) {
					x = angle;
					cnt++;
				}
			}
			
			max = Math.max(max, cnt);
		}
		System.out.println(max);
		
	}

}
