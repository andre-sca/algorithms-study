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
    def closestValueInTree(self, root: TreeNode, target: float):
        self.closestValue = root.val

        def dfs(node: TreeNode):
            if not node:
                return 0
            
            if abs(target - node.val) < abs(target - self.closestValue):
                self.closestValue = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.closestValue
            

    


root = array_to_tree([4, 2, 5, 1, 3])
res = print(Solution().closestValueInTree(root, 2.5))
