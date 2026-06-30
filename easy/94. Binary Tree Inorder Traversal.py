"""
94. Binary Tree Inorder Traversal
Solved

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ## Recursion 1
        # if not root:
        #     return []
        # res = []

        # left_child = self.inorderTraversal(root.left)
        # if left_child:
        #     res.extend(left_child)
        # res.append(root.val)

        # right_child = self.inorderTraversal(root.right)
        # if right_child:
        #     res.extend(right_child)
        # return res

        ## Recursion 2

        # res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        
        # dfs(root)
        # return res

        ## Iteration

        res = []
        stack = []

        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


s = Solution()
print(s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3))))) # [1,3,2]
print(s.inorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, None, TreeNode(9)))))) # [4,2,6,5,7,1,3,9,8]
print(s.inorderTraversal(None)) # []
