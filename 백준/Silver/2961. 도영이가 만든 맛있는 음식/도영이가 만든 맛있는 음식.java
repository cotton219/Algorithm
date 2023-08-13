import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int n;
    static List<int[]> stuffList;
    static int result;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        
        stuffList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int[] stuff = new int[2];
            stuff[0] = scanner.nextInt();
            stuff[1] = scanner.nextInt();
            stuffList.add(stuff);
        }

        result = (int) 1e9;
        for (int num = 1; num <= n; num++) {
            dfs(0, 0, num, new ArrayList<>());
        }

        System.out.println(result);
    }

    static void dfs(int depth, int start, int num, List<int[]> arr) {
        if (depth == num) {
            int sour = 1;
            int bitter = 0;
            for (int[] s : arr) {
                sour *= s[0];
                bitter += s[1];
            }
            if (Math.abs(sour - bitter) < result) {
                result = Math.abs(sour - bitter);
            }
            return;
        }

        for (int i = start; i < n; i++) {
            List<int[]> temp = new ArrayList<>(arr);
            temp.add(stuffList.get(i));
            dfs(depth + 1, i + 1, num, temp);
        }
    }
}