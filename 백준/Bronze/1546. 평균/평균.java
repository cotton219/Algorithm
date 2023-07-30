
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {	
	static int n;
	static double sum, max;
	static double[] arr;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		arr = new double[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Double.parseDouble(st.nextToken());
		}
		
		Arrays.sort(arr);
		max = arr[n-1];
		sum = 0;
		for(int i = 0; i<n; i++) {
			sum += ((arr[i]/max)*100);
		}
			
		System.out.println(sum/n);
	}
}
