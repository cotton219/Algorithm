import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, min, max;
	static int x;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		min = 1000001;
		max = -1000001;
		
		while(st.hasMoreTokens()) {
			x = Integer.parseInt(st.nextToken());
			if (min > x) {
				min = x;
			}
			if (max < x) {
				max = x;
			}
		}
		
		System.out.println(min + " " + max);
	}

}