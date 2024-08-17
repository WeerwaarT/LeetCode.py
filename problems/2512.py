# 2512. 奖励最顶尖的 K 名学生
# https://leetcode.cn/problems/reward-top-k-students/
import collections
import heapq
from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        vocabulary = collections.defaultdict(int)
        for p in positive_feedback:
            vocabulary[p] = 3

        for n in negative_feedback:
            vocabulary[n] = -1

        heap = []
        n = len(report)
        for i in range(n):
            score = 0
            for word in report[i].split(' '):
                score += vocabulary[word]

            if len(heap) < k:
                heapq.heappush(heap, (score, -student_id[i]))
            else:
                heapq.heappushpop(heap, (score, -student_id[i]))

        top_k = []
        for _ in range(k):
            _, s_id = heapq.heappop(heap)
            top_k.append(-s_id)

        top_k.reverse()
        return top_k