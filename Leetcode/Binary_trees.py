import heapq as h
from math import log
import heapq


first = lambda h: 2**h - 1      # H stands for level height
last = lambda h: first(h + 1)
level = lambda heap, h: heap[first(h):last(h)]
prepare = lambda e, field: str(e).center(field)


# h.heapify(mylist)
# print(mylist)

def hprint(heap, width=None):
    if width is None:
        width = max(len(str(e)) for e in heap)
    height = int(log(len(heap), 2)) + 1
    gap = ' ' * width
    for h in range(height):
        below = 2 ** (height - h - 1)
        field = (2 * below - 1) * width
        print(gap.join(prepare(e, field) for e in level(heap, h)))


def inorderTraversal(arr, node):
    if node < len(arr):
        inorderTraversal(arr, 2*node+1)
        print(arr[node])
        inorderTraversal(arr, 2*node+2)

def preorderTraversal(arr,node):
    if node < len(arr):
        print(arr[node])
        preorderTraversal(arr, 2*node+1)
        preorderTraversal(arr, 2*node+2)


def postorderTraversal(arr,node):
    if node < len(arr):
        postorderTraversal(arr, 2*node+1)
        postorderTraversal(arr, 2*node+2)
        print(arr[node])


def isValidBST(arr,node):
    while(node<len(arr)):
        if arr[node] > arr[2*node+1]:
            return False
        if arr[node] < arr[2*node+2]:
            return False
        node+=1
    return True



if __name__ == '__main__':

    arr = list(map(int,'4,2,1,3,6,5,7'.strip().split(',')))
    arr=[]

    print(f'hprint:')


    print(isValidBST(arr,0))




