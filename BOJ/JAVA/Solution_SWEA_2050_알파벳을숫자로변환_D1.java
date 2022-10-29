package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_2050_알파벳을숫자로변환_D1 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		for (int i = 0; i < S.length(); i++) {
			System.out.print((S.charAt(i)-'A'+1) + " ");
		}

	}
}
