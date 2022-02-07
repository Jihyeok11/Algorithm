package programmers;

public class ¾ç±Ã´ëÈ¸ {
	static int N;
	static int[] Info;
	static int[] answer = new int[11];
	static int max = Integer.MIN_VALUE;
	static boolean isPossible;

	public int[] solution(int n, int[] info) {
		N = n;
		Info = info;
		combi(new int[11], 0, 0, 0, 0);
		if (!isPossible) {
			answer = new int[1];
			answer[0] = -1;
			return answer;
		}
		return answer;
	}

	static void combi(int[] res, int idx, int cnt, int a, int b) {
		if (idx == 11) {
			if (cnt < N) {
				res[10] = N- cnt;
			}
			if (a < b) {
				int score = b - a;
				if (max < score) {
					isPossible = true;
					System.arraycopy(res, 0, answer, 0, 11);
					max = score;
				} else if (max == score) {
					if (!change(answer, res)) {
						return;
					}
				}
			}
			return;
		}

		int a_point = 0;
		res[idx] = 0;
		a_point = Info[idx] > 0 ? 10 - idx : 0;
		combi(res, idx + 1, cnt, a + a_point, b);

		int b_point = 10 - idx;
		int tmp_cnt = Info[idx] + 1;
		if ((cnt + tmp_cnt) <= N) {
			res[idx] = tmp_cnt;
			combi(res, idx + 1, cnt + tmp_cnt, a, b + b_point);
		}
	}

	static boolean change(int[] time, int[] sec) {
		for (int i = 10; i >= 0; --i) {
			if (time[i] < sec[i]) {
				return true;
			} else if (time[i] > sec[i])
				return false;
		}
		return false;
	}
}
