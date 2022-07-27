package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_SWEA_1983_조교의성적매기기_D2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] grade = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"};
		int TC = Integer.parseInt(br.readLine().trim());
		for (int testCase = 1; testCase <= TC; testCase++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			int[] score = new int[N];
			int rank = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int totalScore = Integer.parseInt(st.nextToken()) * 35 + Integer.parseInt(st.nextToken()) * 45 + Integer.parseInt(st.nextToken()) * 20;
				score[i] = totalScore;
			}
			for (int i = 0; i < score.length; i++) {
				if(score[i] > score[K-1]) rank++;
			}
			System.out.println("#" + testCase + " " + grade[rank/(N/10)]);
			
		}
	}
}
