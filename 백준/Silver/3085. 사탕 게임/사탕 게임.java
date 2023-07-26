

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int n;
	static char[][] data;
	static int answer = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		data = new char[n][n];
		
		String line="";
		for (int i = 0; i < n; i++) {
			line = br.readLine();
			data[i] = line.toCharArray();
		}
		
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n-1; j++) {
				char temp = data[i][j]; 
				data[i][j] = data[i][j+1];
				data[i][j+1] = temp;
				answer = Math.max(check(), answer);
				temp = data[i][j]; 
				data[i][j] = data[i][j+1];
				data[i][j+1] = temp;
			}
		}
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n-1; j++) {
				char temp = data[j][i]; 
				data[j][i] = data[j+1][i];
				data[j+1][i] = temp;
				answer = Math.max(check(), answer);
				temp = data[j][i]; 
				data[j][i] = data[j+1][i];
				data[j+1][i] = temp;
			}
		}
		System.out.println(answer);
		
	}
	
	private static int check() {
		for(int i = 0; i < n; i++) {
            int cnt = 1;
            for(int j = 0; j < n-1; j++) {
                if(data[i][j] == data[i][j+1]) {
                    cnt++;
                } else {
                    cnt = 1;
                }
                answer = Math.max(answer, cnt);
            }
        }

        for(int i = 0; i < n; i++) {
            int cnt = 1;
            for(int j = 0; j < n-1; j++) {
                if(data[j][i] == data[j+1][i]) {
                    cnt++;
                } else {
                    cnt = 1;
                }
                answer = Math.max(answer, cnt);
            }
        }

        return answer;
	}
	


}
