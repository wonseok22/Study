package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_SWEA_2070_큰놈작은놈같은놈_D1{
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int TC;
		TC = Integer.parseInt(st.nextToken());
		for (int testCase = 0; testCase < TC; testCase++) {
			int first,sec;
			char type;
			st = new StringTokenizer(br.readLine());
			first = Integer.parseInt(st.nextToken());
			sec = Integer.parseInt(st.nextToken());
			if (first > sec ) type = '>';
			else if (first < sec ) type = '<';
			else type = '=';
			System.out.printf("#%d %c\n",testCase+1,type);
		}
	}
}
