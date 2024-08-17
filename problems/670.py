class Solution:
    def maximumSwap(self, num: int) -> int:
        nums1 = []
        while num:
            nums1.append(num % 10)
            num //= 10

        nums2 = sorted(nums1)
        right = len(nums1) - 1
        while right > 0 and nums1[right] == nums2[right]:
            right -= 1

        left = 0
        for i in range(right):
            if nums1[i] > nums1[left]:
                left = i

        nums1[left], nums1[right] = nums1[right], nums1[left]
        ans = 0
        for i in range(len(nums1)):
            ans += nums1[i] * pow(10, i)
        return ans
        # nums1.reverse()
        # return int(''.join(map(str, nums1)))

    def maximumSwap_(self, num: int) -> int:
        ans = num
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i):
                s[i], s[j] = s[j], s[i]
                ans = max(ans, int(''.join(s)))
                s[i], s[j] = s[j], s[i]
        return ans

    def maximumSwap__(self, num: int) -> int:
        lst = list(map(int, str(num)))
        lst1 = lst[:]
        lst1.sort()
        lst1.reverse()
        if lst == lst1:
            return num
        # 找到需要交换的数a及索引i
        i = 0
        while lst[i] == lst1[i]:
            i += 1
        a = lst[i]
        target = lst1[i]
        # 找到第二个交换的数b及索引j
        j = len(lst) - 1
        while lst[j] != target:
            j -= 1
        b = lst[j]
        lst[i] = b
        lst[j] = a
        for i in range(len(lst)):
            lst[i] = str(lst[i])
        return int(''.join(lst))


print(Solution().maximumSwap(123123))
