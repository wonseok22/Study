package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_2068_최대수구하기_D1{
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int TC;
		TC = Integer.parseInt(st.nextToken());
		for (int testCase = 0; testCase < TC; testCase++) {
			int m = 0;
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i <10; i++) {
				int num = Integer.parseInt(st.nextToken());
				if (num > m) m = num;
			}
			System.out.printf("#%d %d\n",testCase+1,m);
		}
	}
}
