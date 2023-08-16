

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n, e;
	static ArrayList<Integer>[] arr;
	static boolean[] visited;
	static int count;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		e = Integer.parseInt(br.readLine());
		
		arr = new ArrayList[n+1];
		for(int i = 1; i <= n; i++) {
			arr[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < e; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
            arr[b].add(a);
        }
		
		visited = new boolean[n+1];
		count = 0; 
		dfs(1);
		System.out.println(count);
		
	}
	static void dfs(int x) {
		
		visited[x] = true;
		
		for(int i : arr[x]) {
			if (!visited[i]) {
				dfs(i);
				count++;
			}
		}
		
	}

}
