class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        # 1. The last element in postorder is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # 2. Find index of root in inorder
        mid = inorder.index(root_val)
        
        # 3. Recursively build right subtree, then left subtree
        root.right = self.buildTree(inorder[mid + 1 :], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        
        return root