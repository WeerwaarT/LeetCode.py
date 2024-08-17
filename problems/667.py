from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return list(range(1, n + 1))

        left = (n + 1) // 2
        right = left
        left_side = False
        ans = [left]

        while k:
            if left_side:
                left_side = False
                left -= 1
                ans.append(left)
            else:
                left_side = True
                right += 1
                ans.append(right)

            k -= 1

        if left_side:
            ans = list(range(1, left)) + ans + list(range(right + 1, n + 1))
        else:
            ans = list(range(n, right, -1)) + ans + list(range(left - 1, 0, -1))
        return ans

    def constructArray_(self, n: int, k: int) -> List[int]:
        mid = (n - 1) // 2 + 1
        ans = [mid] + [0] * (k - 1)
        if k % 2:
            ans[1::2] = list(range(mid + 1, mid + ((k + 1) // 2)))
            ans[2:2 + k // 2 * 2:2] = list(range(mid - 1, mid - k // 2 - 1, -1))
            ans = list(range(1, mid - k // 2)) + ans + list(range(mid + k // 2 + 1, n + 1))
        else:
            ans[1::2] = list(range(mid + 1, mid + ((k + 1) // 2 + 1)))
            ans[2:2 + k // 2 * 2:2] = list(range(mid - 1, mid - k // 2, -1))
            ans = list(range(n, mid + k // 2, -1)) + ans + list(range(mid - k // 2, 0, -1))

        return ans

    def constructArray__(self, n: int, k: int) -> List[int]:
        result = [1]
        flag = True
        for i in range(k, 0, -1):
            if flag:
                result.append(result[-1] + i)
                flag = False
            else:
                result.append(result[-1] - i)
                flag = True
        for i in range(1 + k + 1, n + 1):
            result.append(i)
        return result

    def constructArray___(self, n: int, k: int) -> List[int]:
        answer = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i, j = i + 1, j - 1
        return answer


print(Solution().constructArray__(10, 9))
