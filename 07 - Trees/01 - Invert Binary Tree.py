"""
You are given the root of a binary tree root. Invert the binary tree and return its root.
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

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)

    return root
        


root = array_to_tree([4,2,7,1,3,6,9])
res = invertTree(root)
print(tree_to_array(res))

# Time: O(n)
# Space: O(n)
