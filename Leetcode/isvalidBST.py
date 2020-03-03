# Python program to check if a binary tree is bst or not

INT_MAX = float('inf')
INT_MIN = float('-inf')


# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def createTree(arr, root, i, n):
    if i<n:
        root = Node(arr[i])
        root.left= createTree(arr, root.left, 2 * i + 1, n)
        root.right = createTree(arr, root.right, 2 * i + 2, n)
    return root


def inOrderTraversal(root):
    if root != None:
        inOrderTraversal(root.left)
        print(root.val,end=" ")
        inOrderTraversal(root.right)


def inorderBSTCheck(node):
    stack, prev = [], float('-inf')

    while stack or root:          # Loop through stack/ root
        while root:                 # Loop through root
            stack.append(root)      # Append root to stack
            root = root.left        # Traverse down the left root
        root = stack.pop()        # referencing to the

        if root.val <= prev:   # if element in inorder is smaller than previous, not BST
            return False
        prev = root.val
        root = root.right

    return True

    # prev = None
    # def inorder(node):
    #     if node is None:  # If tree is empty return True
    #         Return True
    #     if inorder(node.left) is False:
    #         return False
    #     if prev is not None and prev.data > root.data:
    #         return False
    #     prev = root
    #     return inorder(root.right)



    return inorder(node)




# Returns true if the given tree is a binary search tree
# (efficient version)
def recursiveBSTCheck(node):
    # Retusn true if the given tree is a BST and its values
    # >= min and <= max
    def isBSTUtil(node, mini, maxi):
        # An empty tree is BST
        if node is None:
            return True

        # False if this node violates min/max constraint
        if node.data < mini or node.data > maxi:
            return False

        # Otherwise check the subtrees recursively
        # tightening the min or max constraint
        return (isBSTUtil(node.left, mini, node.data - 1) and
                isBSTUtil(node.right, node.data + 1, maxi))
    return (isBSTUtil(node, INT_MIN, INT_MAX))





if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6]
    n = len(arr)
    root = None
    root = createTree(arr, root, 0, n)
    inOrderTraversal(root)
