package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_2056_연월일달력_D1 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int TC;
		TC = Integer.parseInt(st.nextToken());
		int[] date = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		for (int testCase = 0; testCase < TC; testCase++) {
			String nums = br.readLine();
			int years = Integer.parseInt(nums.substring(0,4));
			int month = Integer.parseInt(nums.substring(4,6));
			int day = Integer.parseInt(nums.substring(6,8));
			if (0 < month  && month < 13 && 1 <= day && day <= date[month]) {
				System.out.printf("#%d %s\n", testCase+1, nums.substring(0,4) + "/" + nums.substring(4,6) + "/" + nums.substring(6,8)
				);
			} else System.out.printf("#%d -1\n", testCase+1);
		}
	}
}
