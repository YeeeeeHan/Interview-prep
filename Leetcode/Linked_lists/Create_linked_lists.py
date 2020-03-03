class Node:
	def __init__(self,data=None):
		self.val=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head = None

# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		newNode = Node(data)
		if self.head is None:
			self.head = Node(data)
		else:
			last_node = self.head
			while last_node.next is not None:
				last_node = last_node.next
			last_node.next = newNode


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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Print_dep_unsorted_linkedlist_hash(head): # O(N)
	duplicates = []
	hash = {}
	ptr = head
	while (ptr is not None):
		if hash.get(ptr.val, False):
			duplicates.append(ptr.val)
		else:
			hash[ptr.val] = 1
		ptr = ptr.next
	print(duplicates)


def Print_dep_unsorted_linkedlist_2pointer(head):
	duplicates = set()
	current = head
	while current is not None:
		runner = current
		while runner.next is not None:			# work with temp.next, so that can do temp.next.next
			if runner.next.val == current.val:
				duplicates.add(runner.next.val)
			runner = runner.next
		current = current.next
	print(duplicates)



# Does not work for 0,0,1,1,1,2,2,3,3,4
def Remove_dup_unsorted_linkedlist_2pointer(head): # O(N*N)
	current = head
	while current is not None:
		print(f"current.val: {current.val}")
		runner = current
		while runner.next is not None:			# work with temp.next, so that can do temp.next.next
			print(f"runner: {runner.val}")
			if runner.next.val == current.val:
				print(f"found: {current.val}")
				if runner.next.next is not None:
					runner.next = runner.next.next
				else:
					runner.next = None
					break
			runner = runner.next
		current = current.next


def Remove_sorted_linkedlist_2pointer(head):
	current = head
	while head is not None:
		print(f"head.val:{head.val}")

		head = head.next




if __name__ == '__main__':
	arr = [0,0,1,1,1,2,2,3,3,4]
	root = linked_list()
	root.arrayToLinkedList(arr)
	root.printLinkedList()
	Remove_dup_unsorted_linkedlist_2pointer(root.head)
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
