package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_SWEA_2058_자릿수더하기_D1 {
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int answer = 0;
		while(N > 0) {
			answer += N % 10;
			N /= 10;
		}
		System.out.printf("%d\n",answer);
	}
}
