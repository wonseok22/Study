 package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_SWEA_1970_쉬운거스름돈_D2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine().trim());
		for (int testCase = 1; testCase <= TC; testCase++) {
			int[] cash = {50000,10000,5000,1000,500,100,50,10};
			int[] change = new int[8];
			int price = Integer.parseInt(br.readLine().trim());
			for (int i = 0; i < change.length; i++) {
				change[i] += price / cash[i];
				price %= cash[i];
			}
			System.out.println("#" + testCase);
			for (int i : change) {
				System.out.print(i + " ");
			}
			System.out.println();
		}
	}
}
