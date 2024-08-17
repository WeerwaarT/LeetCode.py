from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push, pop, stack = 0, 0, []

        while pop < len(popped):
            if push == len(pushed):
                while stack:
                    if stack.pop() != popped[pop]:
                        return False

                    pop += 1

                return True

            if pushed[push] == popped[pop]:
                push += 1
                pop += 1
            else:
                if stack and popped[pop] == stack[-1]:
                    stack.pop()
                    pop += 1
                else:
                    stack.append(pushed[push])
                    push += 1

        return True

    def _validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        top = out = 0
        for push in pushed:
            pushed[top] = push
            while top >= 0 and pushed[top] == popped[out]:
                out += 1
                top -= 1
            top += 1
        return top == 0

    def __validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return len(st) == 0
