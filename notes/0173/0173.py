# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = []
        self.preorder(self.root)
        
    def preorder(self, root):
        if not root:
            return 
        self.preorder(root.left)
        self.nodes.append(root)
        self.preorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.nodes.pop(0).val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.nodes) > 0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
