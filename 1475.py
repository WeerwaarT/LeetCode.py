from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for index, price in enumerate(prices):
            result.append(price)
            for i in range(index + 1, len(prices)):
                if prices[i] <= price:
                    result[index] -= prices[i]
                    break

        return result

    def _finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        st = [0]
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while len(st) > 1 and st[-1] > p:
                st.pop()
            ans[i] = p - st[-1]
            st.append(p)
        return ans


A = Solution()
print(A.finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))
