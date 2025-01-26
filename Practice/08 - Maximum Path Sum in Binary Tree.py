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
    def maxPathSum(self, root: TreeNode):
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            # Base case: if the node is None, return 0
            if not node:
                return 0

            # Recursively calculate the maximum path sum for left and right subtrees
            left = max(dfs(node.left), 0)  # If negative, return 0 (ignore that path)
            right = max(dfs(node.right), 0)

            # Calculate the maximum path sum that passes through this node
            current_path_sum = node.val + left + right

            # Update the global maximum path sum if the current path is greater
            max_sum = max(max_sum, current_path_sum)

            # Return the maximum path sum including this node and at most one child
            return node.val + max(left, right)
        dfs(root)

        return max_sum

            

    


root = array_to_tree([4, 2, 5, 1, 3])
res = print(Solution().maxPathSum(root))
