class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ops = []

        m = len(target)

        j = 0
        for i in range(1, n+1):
            ops.append("Push")
            

            
            # print(i, target[j])
            if i == target[j]:
                stack.append(i)
                
                j += 1
            else:
                ops.append("Pop")

            if j == m:
                return ops



        return ops