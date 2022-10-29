package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_SWEA_1986_지그재그숫자_D2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= TC; testCase++) {
			int answer = 0;
			int N = Integer.parseInt(br.readLine());
			for (int i = 1; i <= N; i++) {
				if (i%2 == 0) answer -= i;
				else answer += i;
			}
			System.out.println("#" + testCase + " " + answer);
		}
	}
}
