class EmptyValue:
    pass


class BinaryTree:
    """Binary Tree class.

    Attributes:
    - root (object): the item stored at the root, or EmptyValue
    - left (BinaryTree): the left subtree of this binary tree
    - right (BinaryTree): the right subtree of this binary tree
    """

    def __init__(self, root=EmptyValue):
        """ (BinaryTree, object) -> NoneType

        Create a new binary tree with a given root value,
        and no left or right subtrees.
        """
        self.root = root    # root value
        if self.is_empty():
            # Set left and right to nothing,
            # because this is an empty binary tree.
            self.left = None
            self.right = None
        else:
            # Set left and right to be new empty trees.
            # Note that this is different than setting them to None!
            self.left = BinaryTree()
            self.right = BinaryTree()

    def is_empty(self):
        """ (BinaryTree) -> bool
        Return True if self is empty.
        Note that only empty binary trees can have left and right
        attributes set to None.
        """
        return self.root is EmptyValue

    def preorder(self):
        """ (BinaryTree) -> list
        Return a list of the items in this tree using a *preorder* traversal.
        """
        if self.root != EmptyValue:
            print(self.root)
            print(self.preorder(self.root.left))
            print(self.preorder(self.root.right))

    def inorder(self):
        """ (BinaryTree) -> list
        Return a list of the items in this tree using an *inorder* traversal.
        """

        if self.root != EmptyValue:
            print(self.inorder(self.root.left))
            print(self.root)
            print(self.inorder(self.root.right))


    def postorder(self):
        """ (BinaryTree) -> list
        Return a list of the items in this tree using a *postorder* traversal.
        """
        if self.root != EmptyValue:
            print(self.postorder(self.root.left))
            print(self.postorder(self.root.right))
            print(self.root)
