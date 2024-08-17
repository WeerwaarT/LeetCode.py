# 1761. 一个图中连通三元组的最小度数
# https://leetcode.cn/problems/minimum-degree-of-a-connected-trio-in-a-graph/
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        ##统计所有节点的度数
        ##找出所有三元组(a,b,c)
        ##连通三元组的度数为a,b,c的度数之和-6
        degree=[0]*(n+1)
        g=defaultdict(set)
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            if u>v:g[u].add(v)
            else:g[v].add(u)
        ans=inf
        for i in range(n+1):
            if len(g[i])<2:continue
            for j in g[i]:
                d=degree[i]+degree[j]-6
                if d>ans:continue
                for k in g[i]&g[j]:
                    ans=min(ans,degree[k]+d)
        return ans if ans!=inf else -1