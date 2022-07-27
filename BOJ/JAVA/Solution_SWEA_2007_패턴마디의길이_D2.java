package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.function.IntPredicate;

public class Solution_SWEA_2007_패턴마디의길이_D2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= TC; testCase++) {
			String s = br.readLine();
            char c = s.charAt(0);
             
            for (int i = 1; i < 30; i++) {
                if(s.charAt(i) == c) {
                    boolean flag = true;
                    for (int j = i + 1; j < i * 2; j++) {
                        if(s.charAt(j) != s.charAt(j - i)) {
                            flag = false;
                        }
                    }
                    if(flag) {
                        System.out.println("#" + testCase + " " + i);
                        break;
                    }
                }
            }
		}
	}
}
