package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_SWEA_1989_초심자의회문검사_D2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= TC; testCase++) {
			String s = br.readLine().trim();
			int start = 0;
			int end = s.length()-1;
			int answer = 1;
			while (start <= end) {
				
				if (s.charAt(start++) != s.charAt(end--)) {
					answer = 0;
					break;
				}
			}
			
			System.out.println("#" + testCase + " " + answer);
		}
	}
}
