import heapq as h
from math import log
import heapq


class Node:
    # Constructor to create a new node
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



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

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6]
    n = len(arr)
    root = None
    root = createTree(arr, root, 0, n)
    inOrderTraversal(root)





