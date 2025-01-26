"""
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree.
The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1  # Start processing nodes from the second element in the array
    
    while i < len(arr):
        current = queue.pop(0)
        
        # Process the left child
        if arr[i] is not None:  # If the left child exists
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        # Process the right child (only if it's within bounds)
        if i < len(arr) and arr[i] is not None:  # If the right child exists
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root


def tree_to_array(root: TreeNode):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # Return height
        def dfs(curr: Optional[TreeNode]):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
    



root = array_to_tree([1,None,2,3,4,5])
res = Solution().diameterOfBinaryTree(root)
print(res)