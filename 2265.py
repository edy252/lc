# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # Child Nodes pass up (sum including itself, num including itself, valid nodes n)
        def dfs(node):
            this_sum = node.val
            this_n = 1
            valid_nodes = 0

            if node.left:
                left = dfs(node.left)
                this_sum += left[0]
                this_n += left[1]
                valid_nodes += left[2]
            if node.right:
                right = dfs(node.right)
                this_sum += right[0]
                this_n += right[1]
                valid_nodes += right[2]

            this_ans = int(this_sum / this_n)
            if this_ans == node.val:
                valid_nodes += 1

            return (this_sum, this_n, valid_nodes)

        ans = dfs(root)

        return ans[2]