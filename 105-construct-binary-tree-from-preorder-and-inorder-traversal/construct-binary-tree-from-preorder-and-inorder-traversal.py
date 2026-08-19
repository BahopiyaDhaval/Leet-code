class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # 1. First element in preorder is root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. Find index of root in inorder
        mid = inorder.index(root_val)
        
        # 3. Recursively build subtrees
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root