package algorithm;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;
import java.io.*;

public class Main_BOJ_4963_섬의개수 {
	
//	좌표의 쌍
	static class Node {
		int x,y;
		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
//	bfs로 이동 가능한 섬 탐색
	static int[][] bfs(int x, int y, int[][] board) {
		int[] dx = {-1,1,0,0,-1,1,-1,1};
		int[] dy = {0,0,-1,1,1,-1,-1,1};

		Queue<Node> q = new LinkedList<Node>();
		q.add(new Node(x,y));
		board[x][y] = 0;
		while (!q.isEmpty()) {
			Node curr = q.poll();
			for (int i = 0; i < 8; i++) {
				int ax = curr.x + dx[i];
				int ay = curr.y + dy[i];
				if (0 <= ax && ax < board.length && 0 <= ay && ay < board[0].length && board[ax][ay] == 1) {
					q.add(new Node(ax,ay));
					board[ax][ay] = 0;
				}
			}
		}
		return board;
	}
	
	public static void main(String[] args) throws Exception {
		int w,h,answer;
		int[][] board;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			answer = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			h = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			
//			종료조건
			if (w == 0 && h == 0) return;
			
			board = new int[w][h];
			for (int i = 0; i < w; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < h; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
//			bfs 실행
			for (int i = 0; i < w; i++) {
				for (int j = 0; j < h; j++) {
					if (board[i][j] == 1) {
						board = bfs(i,j, board);
						answer++;
					}
				}
			}
			System.out.println(answer);
		}
	}
}
