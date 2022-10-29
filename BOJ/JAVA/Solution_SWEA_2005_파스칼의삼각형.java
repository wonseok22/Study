package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_SWEA_2005_파스칼의삼각형 {
	private static int factorial(int n) {
	      int f;
	      for(f = 1; n > 1; n--){
	         f *= n;
	      }
	      return f;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= TC; testCase++) {
			int N = Integer.parseInt(br.readLine());
			System.out.println("#" + testCase);
			for (int i = 0; i < N; i++) {
				for (int j = 0; j <= i; j++) {
					System.out.print(factorial(i) / ( factorial(i-j) * factorial(j) ) + " ");
				}
				System.out.println();
			}
		}
	}
}
