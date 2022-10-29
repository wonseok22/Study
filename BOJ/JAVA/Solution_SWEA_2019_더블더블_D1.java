package algorithm;

import java.util.Scanner;

public class Solution_SWEA_2019_더블더블_D1 {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = 0; i <= N; i++) {
			System.out.print((int)Math.pow(2, i) +" ");
		}
	}
}
