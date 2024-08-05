# 460. LFU 缓存
# https://leetcode.cn/problems/lfu-cache/
import collections


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.frequencies = collections.defaultdict(int)
        self.frequency_order = collections.defaultdict(collections.Counter)
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        freq = self.frequencies[key]
        del self.frequency_order[freq][key]
        self.frequencies[key] += 1
        self.frequency_order[self.frequencies[key]].update([key])
        if not len(self.frequency_order[self.min_freq]):
            self.min_freq += 1

        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            del self.frequency_order[self.frequencies[key]][key]
            self.frequencies[key] += 1
            self.frequency_order[self.frequencies[key]][key] = 1
            if not len(self.frequency_order[self.min_freq]):
                self.min_freq += 1
        else:
            self.frequencies[key] = 1
            self.frequency_order[1][key] = 1
            self.data[key] = value
            if len(self.data) > self.capacity:
                popped_key = self.frequency_order[self.min_freq].most_common()[0][0]
                del self.frequency_order[self.min_freq][popped_key]
                del self.data[popped_key]
                del self.frequencies[popped_key]

            self.min_freq = 1


if __name__ == '__main__':
    # Assuming LFUCache class is already defined

    # List of operations
    operations = ["LFUCache", "put", "put", "get", "get", "get", "put", "put", "get", "get", "get", "get"]
    # List of arguments for each operation
    args = [[3], [2, 2], [1, 1], [2], [1], [2], [3, 3], [4, 4], [3], [2], [1], [4]]

    # Create an empty list to store results
    results = []

    # Instantiate the LFUCache
    cache = None

    for op, arg in zip(operations, args):
        if op == "LFUCache":
            cache = LFUCache(*arg)
            results.append(None)  # Constructor does not return anything
        elif op == "put":
            cache.put(*arg)
            results.append(None)  # Put does not return anything
        elif op == "get":
            ret = cache.get(*arg)
            results.append(ret)

    print(results)

# class LFUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.val_map = {}  # key to value
#         self.freq_map = collections.defaultdict(collections.OrderedDict)  # freq to keys in order
#         self.key_freq = {}  # key to freq
#         self.min_freq = 0
#
#     def get(self, key: int) -> int:
#         if key not in self.val_map:
#             return -1
#         # Increase frequency
#         self._update(key)
#         return self.val_map[key]
#
#     def put(self, key: int, value: int) -> None:
#         if not self.capacity:
#             return
#
#         if key in self.val_map:
#             self.val_map[key] = value
#             self._update(key)
#         else:
#             if len(self.val_map) == self.capacity:
#                 # Remove the least frequent key
#                 removed_key, _ = self.freq_map[self.min_freq].popitem(last=False)  # FIFO order
#                 self.val_map.pop(removed_key)
#                 self.key_freq.pop(removed_key)
#             self.val_map[key] = value
#             self.key_freq[key] = 1
#             self.freq_map[1][key] = None  # The actual value doesn't matter
#             self.min_freq = 1
#
#     def _update(self, key):
#         freq = self.key_freq[key]
#         self.key_freq[key] += 1
#         self.freq_map[freq].pop(key)
#         self.freq_map[freq + 1][key] = None
#         if not self.freq_map[freq] and freq == self.min_freq:
#             self.min_freq += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# class LFUCache:
#     def __init__(self, capacity: int):
#         self.data = {}
#         self.freq = defaultdict(OrderedDict)
#         self.cap = capacity
#         self.least = 0
#
#     def get(self, key: int) -> int:
#         if key in self.data:
#             val, cnt = self.data[key]
#             del self.freq[cnt][key]
#             if len(self.freq[cnt]) == 0 and cnt == self.least:
#                 self.least += 1
#             self.freq[cnt + 1][key] = 1
#             self.data[key] = [val, cnt + 1]
#             return val
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.data:
#             val, cnt = self.data[key]
#             del self.freq[cnt][key]
#             if len(self.freq[cnt]) == 0 and cnt == self.least:
#                 self.least += 1
#             self.freq[cnt + 1][key] = 1
#             self.data[key] = [value, cnt + 1]
#         else:
#             if len(self.data) >= self.cap:
#                 k = self.freq[self.least].popitem(last=False)[0]
#                 del self.data[k]
#             self.data[key] = [value, 1]
#             self.least = 1
#             self.freq[1][key] = 1
