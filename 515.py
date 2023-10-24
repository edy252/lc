# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = [(root, 0)]

        # row: val
        maxval = collections.defaultdict(lambda: float('-inf'))

        while q:
            node, row = q.pop(0)

            maxval[row] = max(maxval[row], node.val)

            if node.left:
                q.append((node.left, row+1))
            if node.right:
                q.append((node.right, row+1))

        return maxval.values()
