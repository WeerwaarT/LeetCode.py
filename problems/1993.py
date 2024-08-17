# 1993. 树上的操作
# https://leetcode.cn/problems/operations-on-tree/
import collections
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.locks = [False] * n
        self.users = [0] * n
        self.parent = parent
        self.children = collections.defaultdict(list)
        for i, p in enumerate(parent):
            self.children[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num]:
            return False

        self.users[num] = user
        self.locks[num] = True
        return True

    def unlock(self, num: int, user: int) -> bool:
        if not self.locks[num]:
            return False

        if self.users[num] != user:
            return False

        self.locks[num] = False
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num]:
            return False

        if num not in self.children.keys():
            return False

        p = self.parent[num]
        while p > -1:
            if self.locks[p]:
                return False

            p = self.parent[p]

        queue = collections.deque([num])
        children = []
        while queue:
            cur = queue.popleft()
            self.locks[num] = self.locks[num] or self.locks[cur]
            children.extend(self.children[cur])
            queue.extend(self.children[cur])

        if not self.locks[num]:
            return False

        self.users[num] = user
        for c in children:
            self.locks[c] = False

        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

# class LockingTree:
#     def __init__(self, parent: List[int]):
#         self.parent = parent
#         self.locklist = [0] * len(parent)
#         self.childlock = [[] for _ in range(len(parent))]
#
#     def lock(self, num: int, user: int) -> bool:
#         if self.locklist[num]:
#             return False
#
#         self.locklist[num] = user
#         parent = self.parent[num]
#         while parent != -1:
#             self.childlock[parent].append(num)
#             parent = self.parent[parent]
#
#         return True
#
#     def unlock(self, num: int, user: int) -> bool:
#         if self.locklist[num] != user and user != 0:
#             return False
#
#         self.locklist[num] = 0
#         parent = self.parent[num]
#         while parent != -1:
#             self.childlock[parent].remove(num)
#             parent = self.parent[parent]
#
#         return True
#
#     def upgrade(self, num: int, user: int) -> bool:
#         if self.locklist[num]:
#             return False
#
#         if not self.childlock[num]:
#             return False
#
#         parent = self.parent[num]
#         while parent != -1:
#             if self.locklist[parent]:
#                 return False
#
#             parent = self.parent[parent]
#
#         self.lock(num, user)
#         for child in self.childlock[num].copy():
#             self.unlock(child, 0)
#
#         return True