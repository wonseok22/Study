package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_1976_사각덧셈_D2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine().trim());
		for (int testCase = 1; testCase <= TC; testCase++) {
			int hour = 0;
			int min = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			hour += Integer.parseInt(st.nextToken());
			min += Integer.parseInt(st.nextToken());
			hour += Integer.parseInt(st.nextToken());
			min += Integer.parseInt(st.nextToken());
			hour += min / 60;
			min %= 60;
			if (hour > 12) {
				hour -= ((hour-1)/12) * 12;
			}
			System.out.println("#" + testCase + " " + hour + " " + min);
		}
	}
}
