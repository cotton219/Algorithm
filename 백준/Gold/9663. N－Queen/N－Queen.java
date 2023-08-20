import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int N, ans;
	static int[] cols;
	static int[] dia;
	static int[] undia;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		ans = 0;
		
		cols = new int[N+1];
		dia = new int[2*N+1];
		undia = new int[2*N+1];
		
		dfs(1);
		
		System.out.println(ans);
	}
	private static void dfs(int row) {
		
		if(row==N+1) {
			ans++;
			return;
		}
		for(int col = 1; col <= N; col++) {
			if(!(cols[col]==1 || dia[row+col]==1 || undia[N+(row-col)+1]==1)) {
				cols[col] = 1;
				dia[row+col] = 1;
				undia[N+(row-col)+1]=1;
				dfs(row+1);
				cols[col] = 0;
				dia[row+col] = 0;
				undia[N+(row-col)+1]=0;
			}
		}
		
	}

}