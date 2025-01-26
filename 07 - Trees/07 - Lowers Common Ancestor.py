"""
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q,
return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.
"""

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

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr




print(Solution().lowestCommonAncestor(array_to_tree([5,3,8,1,4,7,9,None,2]), p = TreeNode(3), q = TreeNode(8)))