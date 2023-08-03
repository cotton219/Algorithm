import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        
        String dna = br.readLine().trim();
        
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int g = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        
        Map<Character, Integer> dictPart = new HashMap<>();
        dictPart.put('A', 0);
        dictPart.put('C', 0);
        dictPart.put('G', 0);
        dictPart.put('T', 0);
        
        int start = 0, end = p - 1;
        int cnt = 0;
        String word = dna.substring(start, end);

        for (char w : word.toCharArray()) {
            dictPart.put(w, dictPart.get(w) + 1);
        }

        while (end < s) {
            dictPart.put(dna.charAt(end), dictPart.get(dna.charAt(end)) + 1);
            
            if (dictPart.get('A') >= a && dictPart.get('C') >= c &&
                dictPart.get('G') >= g && dictPart.get('T') >= t) {
                cnt++;
            }

            dictPart.put(dna.charAt(start), dictPart.get(dna.charAt(start)) - 1);
            start++;
            end++;
        }

        System.out.println(cnt);
    }
}