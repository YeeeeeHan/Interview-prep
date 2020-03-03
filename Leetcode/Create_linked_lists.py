class Node:
	def __init__(self,data=None):
		self.val=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head = Node()

# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		if self.head.val is None:
			self.head.val = data
		else:
			temp = Node(data)
			cur = self.head
			while cur.next is not None:
				cur = cur.next
			cur.next = temp


	def arrayToLinkedList(self,arr):
		for i in range(len(arr)):
			root.append(arr[i])



	# Returns the length (integer) of the linked list.
	def length(self):
		cur = self.head
		total = 0
		while cur.next is not None:
			total += 1
			cur = cur.next
		return total

	# Prints out the linked list in traditional Python list format.
	def printLinkedList(self):
		elems=[]
		cur_node = self.head
		while cur_node is not None:
			elems.append(cur_node.val)
			cur_node=cur_node.next
		print(elems)

	# Returns the value of the node at 'index'.
	def get(self,index):
		if index >= self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx == index: return cur_node.data
			cur_idx += 1

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Erase' Index out of range!")
			return
		cur_idx = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_idx == index:
				last_node.next = cur_node.next
				return
			cur_idx += 1





if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 6]
	root = linked_list()
	root.arrayToLinkedList(arr)
	root.printLinkedList()







#     def append(self, item):  # O(n*n) complexity
#         temp = Node(item)
#         curr = self.head
#         ptr = curr
#         while ptr.next is not None:
#             ptr = ptr.next
#         ptr.next = temp
#
#         # ptr = root  # duplicate pointers
#         # while cur.next is not None:  # if not at the end
#         #     ptr = ptr.next  # traverse
#         # ptr.next = temp  # at the end, add temp to the end
#
#
#     # def insertToHead()
#
#
#
#
#
# def printLinkedlist(root):
#     if root is None:
#         print(None)
#
#     else:
#         ptr = root
#     while ptr is not None:
#         print(ptr.val)
#         ptr = ptr.next
#     return 0
#
#
#
# # def insertToHead(root, item):
#
#
#
#
#

#
