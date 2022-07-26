package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_2029_몫과나머지출력하기_D1 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int TC, a, b;
		TC = Integer.parseInt(st.nextToken());
		for (int testCase = 0; testCase < TC; testCase++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			System.out.printf("#%d %d %d\n",testCase + 1, a / b, a % b);
		}
	}
}
