#! /usr/bin/python3
level=0
class Node:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):
		if self.data:

			if data < self.data:
				if self.left is not None:
					print("Left branch of %d not empty, Call insert to left  of %d"%(self.data, self.left.data))
					self.left.insert(data)

				else:
					print("Left of %d is empty, insert %d to left"%(self.data,data))
					self.left = Node(data)

			elif data > self.data:
				if self.right is not None:
					print("Right branch of %d not empty, Call insert to right of %d"%(self.data,self.right.data))
					self.right.insert(data)
				else:
					print("Right of %d is empty, insert %d to right"%(self.data,data))
					self.right = Node(data)		
		else:
			self.data = data

	def print_tree(self):
		print("Print %d "%self.data, end='\n')
		if self.left:
			print("Check left of %d for leaf %d"%(self.data,self.left.data))
			self.left.print_tree()
			print("Finished checking Left of %d for leaf %d"%(self.data,self.left.data))
		if self.right:
			print("Check right of %d for left %d"%(self.data,self.right.data))
			self.right.print_tree()
			print("Finished checking right of %d for leaf %d"%(self.data,self.right.data))
	
	def print_preorder(self):
		
		print("%d"%self.data, end=", ")
		if self.left:
			self.left.print_preorder()
		if self.right:
			self.right.print_preorder()

	def print_postorder(self):
		if self.left:
			self.left.print_postorder()
		if self.right:
			self.right.print_postorder()
		print("%d"%self.data, end=", ")
		
	def print_inorder(self):
		if self.left:
			self.left.print_inorder()
		print("%d"%self.data, end=", ")
		if self.right:
			self.right.print_inorder()


def get_height( root ):
	if root is None:
		return 0
	return 1+ max( get_height(root.left), get_height( root.right) )
		

root=Node(25)
for i in 15,50,10,22,35,70,4,12,18,24,31,44,66,90,91,92:
	root.insert(i)

root.print_tree()
print("\n------------------\n")
print("\n---  Inorder   ---\n")
root.print_inorder()
print("\n---  Preorder  ---\n")
root.print_preorder()

print("\n---  Postorder ---\n")
root.print_postorder()
print("\n------------------\n")

print("Tree height is %s\n"%get_height( root) )