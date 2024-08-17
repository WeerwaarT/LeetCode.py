from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        stack = []
        previous_time = 0

        for log in logs:
            info = log.split(':')
            _id = int(info[0])
            time = int(info[2])

            if info[1] == "start":
                if len(stack):
                    previous_call = stack[-1]
                    times[previous_call] += time - previous_time
                stack.append(_id)
                previous_time = time
            else:
                stack.pop()
                times[_id] += time - previous_time + 1
                previous_time = time + 1

        return times

    def exclusiveTime_(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        st = []
        for log in logs:
            idx, tp, timestamp = log.split(':')
            idx, timestamp = int(idx), int(timestamp)
            if tp[0] == 's':
                if st:
                    ans[st[-1][0]] += timestamp - st[-1][1]
                    st[-1][1] = timestamp
                st.append([idx, timestamp])
            else:
                i, t = st.pop()
                ans[i] += timestamp - t + 1
                if st:
                    st[-1][1] = timestamp + 1
        return ans
