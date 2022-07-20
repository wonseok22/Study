package algorithm;
import java.util.Scanner;

public class Main_SWEA_1248_미로1_D4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for (int testCase = 1; testCase <= TC; testCase++) {
			int answer = 0;
			for (int i = 0; i < 10; i++) {
				int num = sc.nextInt();
				if (num % 2 != 0) answer += num;
			}
			System.out.println("#" + testCase + " " + answer);
		}
	}
}
