package algorithm;

import java.util.Scanner;

public class Solution_SWEA_1933_간단한N의약수_D1 {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = 1; i <= N; i++) {
			if (N % i == 0) {
				System.out.print(i + " ");
			}
		}
	}
}
