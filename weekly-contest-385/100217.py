import collections
from typing import List


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        prime_counts = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    num = 0
                    step_x, step_y = i, j
                    while 0 <= step_x < m and 0 <= step_y < n:
                        num = num * 10 + mat[step_x][step_y]
                        if num > 10 and is_prime(num):
                            prime_counts[num] = prime_counts.get(num, 0) + 1
                        step_x += dx
                        step_y += dy

        if not prime_counts:
            return -1

        # 找出出现频率最高的素数，如果有多个，则返回最大的那个
        max_freq = max(prime_counts.values())
        max_primes = [prime for prime, count in prime_counts.items() if count == max_freq]
        return max(max_primes)


if __name__ == '__main__':
    print(Solution().mostFrequentPrime([[1, 1], [9, 9], [1, 1]]))
