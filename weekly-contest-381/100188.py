from collections import deque, defaultdict
from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0] * n
        streets = defaultdict(list)
        for i in range(2, n):
            streets[i].extend([i + 1, i - 1])

        streets[1].append(2)
        streets[n].append(n - 1)
        if x != y:
            streets[x].append(y)
            streets[y].append(x)

        for j in range(1, n + 1):
            visited = [False] * (n + 1)
            visited[j] = True
            queue = deque([j])
            steps = n
            while steps > 0:
                while len(queue):
                    temp = deque()
                    cur = queue.popleft()
                    for destination in streets[cur]:
                        if not visited[destination]:
                            temp.append(destination)
                            visited[destination] = True

                    steps -= 1
                    if steps != -1:
                        ans[n - steps - 1] += len(temp)

                queue = temp

                if not len(queue):
                    break

        return ans


if __name__ == '__main__':
    print(Solution().countOfPairs(5, 2, 4))
    # print(Solution().countOfPairs(3, 1, 3))
    # print(Solution().countOfPairs(4, 1, 1))
