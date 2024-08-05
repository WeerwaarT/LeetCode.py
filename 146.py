# 146. LRU 缓存
# https://leetcode.cn/problems/lru-cache/
import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = collections.deque()
        self.liveness = collections.defaultdict(int)
        self.data = {}

    def get(self, key: int) -> int:
        val = self.data.get(key, -1)
        if val != -1:
            self.queue.append(key)
            self.liveness[key] += 1

        return val

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.liveness[key] += 1
        self.queue.append(key)
        while len(self.data) > self.capacity:
            cur = self.queue.popleft()
            if self.liveness[cur] == 1:
                self.data.pop(cur)

            self.liveness[cur] -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class LRUCache:
#     from collections import OrderedDict
#
#     def __init__(self, capacity: int):
#         self.d = OrderedDict()
#         self.cap = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.d:
#             return -1
#         self.d.move_to_end(key)
#         return self.d[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key not in self.d and len(self.d) == self.cap:
#             self.d.popitem(0)
#         self.d[key] = value
#         self.d.move_to_end(key)