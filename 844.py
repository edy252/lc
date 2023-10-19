class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        for char in s:
            if char == '#':
                if len(stacks) > 0:
                    stacks.pop()
            else:
                stacks.append(char)

        stackt = []
        for char in t:
            if char == '#':
                if len(stackt) > 0:
                    stackt.pop()
            else:
                stackt.append(char)

        # print(stacks)
        # print(stackt)

        return stacks == stackt