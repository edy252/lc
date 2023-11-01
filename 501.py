# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        max_length = 0
        prev = None
        curr_length = 0

        def dfs_pass(node):
            nonlocal max_length, prev, curr_length
            if node is None:
                return

            dfs_pass(node.left)
            # vals.append(node.val)
            if prev is None or prev == node.val:
                curr_length += 1
            else:
                curr_length = 1
            prev = node.val
            # print(node.val)

            # Update max
            max_length = max(max_length, curr_length)

            dfs_pass(node.right)

        
        def dfs(node):
            nonlocal max_length, prev, curr_length, res
            if node is None:
                return

            dfs(node.left)
            if prev is None or prev == node.val:
                curr_length += 1
            else:
                curr_length = 1
            prev = node.val

            # print(curr_length, max_length)
            if curr_length == max_length:
                res.append(node.val)

            dfs(node.right)


        # Find max length
        dfs_pass(root)

        # Search for sequences that are length max_length
        res = []
        prev = None
        curr_length = 0
        dfs(root)

        
        return res
