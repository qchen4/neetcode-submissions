# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            lenQ = len(q)
            for i in range(lenQ):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    level.append(curr.val)
            if level:
                res.append(level)
        return res
                

            




        return res

       
        