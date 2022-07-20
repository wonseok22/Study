package algorithm;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

class Node implements Comparable<Node>{
	public int w,x,y;
	Node(int w, int x, int y){
		this.w = w;
		this.x = x;
		this.y = y;
	}
	@Override
	public int compareTo(Node node) {
		if (this.w < node.w) {
			return -1;
		} else if (this.w > node.w) {
			return 1;
		}
		return 0;
	}
}

public class Main_SWEA_1249_보급로 {
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int[][] board;
	static int[][] distance;
	static int N;
	
	static void dijkstra() {
		PriorityQueue<Node> pq = new PriorityQueue();
		pq.add(new Node(0,0,0));
		
		while(!pq.isEmpty()) {
			Node curr = pq.poll();
			if (curr.w > distance[curr.x][curr.y]) continue;
			for (int i = 0; i < 4; i++) {
				int ax = curr.x + dx[i];
				int ay = curr.y + dy[i];
				if (0 <= ax && ax < N && 0 <= ay && ay < N) {
					int totalCost = curr.w + board[ax][ay];
					if (totalCost < distance[ax][ay]) {
						distance[ax][ay] = totalCost;
						pq.add(new Node(totalCost, ax, ay));
					}
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			N = Integer.parseInt(br.readLine());
			board = new int[N][N];
			distance = new int[N][N];
			
//			그래프 입력받음
			for (int i = 0; i < N; i++) {
				String[] s = br.readLine().split("");
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(s[j]);					
				}
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					distance[i][j] = Integer.MAX_VALUE;
				}
			}
			distance[0][0] = 0;
			dijkstra();
			System.out.println("#" + (t+1) + " " + distance[N-1][N-1]);
			
		}
	}
}
