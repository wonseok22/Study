package algorithm;

import java.util.Scanner;

public class Solution_SWEA_1936_1대1가위바위보_D1 {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		if (a == 3 && b == 1) System.out.println("B");
		else if (a == 1 && b == 3) System.out.println("A");
		else if ( a > b ) System.out.println("A");
		else System.out.println("B");
	}
}
