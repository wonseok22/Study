package algorithm;

import java.util.Scanner;

public class Solution_SWEA_1545_거꾸로출력해보아요_D1 {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = N; i >= 0; i--) {
			System.out.print(i + " ");
		}
	}
}
