package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_1984_중간평균값구하기_D2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine().trim());
		for (int testCase = 1; testCase <= TC; testCase++) {
			int max = 0;
			int min = Integer.MAX_VALUE;
			int sum = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 10; i++) {
				int num = Integer.parseInt(st.nextToken());
				if (max < num) max = num;
				if (min > num) min = num;
				sum += num;
			}
			sum -= max+min;
			System.out.println("#" + testCase + " " + String.format("%.0f", (double)sum / 8));
		}
	}
}
