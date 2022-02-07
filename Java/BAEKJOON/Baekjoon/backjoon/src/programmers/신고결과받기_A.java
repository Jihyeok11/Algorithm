package programmers;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class �Ű����ޱ�_A {
	public int[] solution(String[] id_list, String[] report, int k) {
		int[] answer = new int[id_list.length];
		HashMap<String, Set<String>> reporterArr = new HashMap<String, Set<String>>();
		HashMap<String, Integer> singoArr = new HashMap<String, Integer>();

		// �ʱ�ȭ
		for (String id : id_list) {
			singoArr.put(id, 0);
			reporterArr.put(id, new HashSet<String>());
		}
		// �Ű�� �����
		for (String cur : report) {
			StringTokenizer st = new StringTokenizer(cur, " ");
			String reporter = st.nextToken();
			String singo = st.nextToken();
			if (reporterArr.get(reporter).add(singo)) {
				singoArr.put(singo, singoArr.get(singo) + 1);
			}
		}
		// �Ű��� ���
		for (String cur : report) {
			StringTokenizer st = new StringTokenizer(cur, " ");
			String reporter = st.nextToken();
			String singo = st.nextToken();
			// ������ �Ű��� ����� �Ű���� Ƚ���� K�̻��� ����̸� ����
			if (singoArr.get(singo) < k)
				reporterArr.get(reporter).remove(singo);
		}
		for (int i = 0; i < id_list.length; i++) {
			answer[i] = reporterArr.get(id_list[i]).size();
		}
		return answer;
	}
}