package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_BOJ_1099_알수없는문장 {
	private static int diff(String s1, String s2) {
		int cnt = 0;
		for (int i = 0; i < s1.length(); i++) {
			if (s1.charAt(i) != s2.charAt(i)) cnt ++;
		}
		return cnt;
	}
	private static boolean compareAlpabet(String s1, String s2) {
		if (s1.length() != s2.length()) return false;
		int[] check = new int[26];
		for (int k = 0; k < s1.length(); k++) {
			check[s1.charAt(k) - 'a']++;
			check[s2.charAt(k) - 'a']--;
		}
		for (int k = 0; k < check.length; k++) {
			if (check[k] != 0) return false; 
		}
		return true;
		
	}
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 입력 받기
		String s = br.readLine();
		int N = Integer.parseInt(br.readLine());
		int[] dp = new int[s.length()+1];
		Arrays.fill(dp, Integer.MAX_VALUE-51); // 최대 다른 문자의 개수가 50개이므로 오버플로우 방지를 위해 int의 MAX값에서 -51을 빼줌
		String[] words = new String[N];
		String[] splitWords;
		for (int i = 0; i < N; i++) {
			words[i] = br.readLine();
		}
		
		// 주어진 문장의 길이만큼 1 ~ length까지 자르며 각 단어별로 최솟값을 찾음
		dp[0] = 0;
		for (int i = 1; i <= s.length(); i++) {
			splitWords = new String[i]; // 1부터 idx만큼 자른 단어들을 담을 array
			// 길이 1부터 길이 i까지 자른 단어들을 splitWords array에 삽입
			for (int j = 0; j < i; j++) { 
				splitWords[j] = s.substring(j, i);
			}
			
			// 자른 단어들과 같은 알파벳으로 구성된 단어가 입력받은 단어들 중에 있는지 확인하고
			// 각 자릿수를 비교하여 몇 개의 알파벳이 다른지 찾는다
			// 다른 자릿수의 개수로 최소 비용 배열인 dp를 MIN 값으로 초기화한다.
			for (int j = 0; j < splitWords.length; j++) {
				for (int j2 = 0; j2 < N; j2++) {
					// splitWords[j] : 자른 문자
					// words[j2] : 주어진 문자
					// 알파벳 구성이 다르다면 실행 x
					if (!compareAlpabet(splitWords[j], words[j2])) continue;
					
					// 몇 개의 자릿수가 다른지 카운트
					int diffCnt = diff(splitWords[j],words[j2]);
					
					// 가장 처음 찾은 단어일 경우 이전에 찾은 단어가 없기 때문에 diffCnt와 비교해야함
					if (j == 0) {
						dp[i] = Math.min(diffCnt, dp[i]);
						continue;
					}
					
					// 자르기 시작한 인덱스 j까지의 최솟값에 현재 비교한 문자의 다른 자릿수를 더한 것과 현재 문자까지의 최솟값을 갱신
					dp[i] = Math.min(dp[i], diffCnt + dp[j]);
				}
			}
		}
		
		// 초깃값 그대로라면 만들 수 없는 문장이므로 -1 출력, 아니라면 dp[s.length()] 출력
		if (dp[s.length()] != Integer.MAX_VALUE-51) {
			System.out.println(dp[s.length()]);
		} else {			
			System.out.println(-1);
		}
		
	}

}
