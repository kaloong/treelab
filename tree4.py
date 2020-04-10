#! /usr/bin/python3
# pylint: disable=too-few-public-methods, missing-docstring, mixed-indentation, trailing-whitespace
import sys

sys.setrecursionlimit(10**6)

class Node(object):  
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class BST(object):
	def __init__(self):
		self.root = None
		self._order_result = []

	def insert(self, val):
		#''' If self.root has something is not True'''
		if not self.root:
			self.root = Node(val)
		else:
			#'''root has something is True try next level'''
			self._insert(val, self.root)
		return True

	def _insert(self, val, root):
		'''
		On next level 
		Check where should go, 
		Check left or right branch?
			Check if branch has anthing
		   		if any, 
		   		else go to next level else 
		'''
		if val < root.data:
			#''' Left branch '''
			if not root.left:
				root.left = Node(val)
			else:
				self._insert(val, root.left)
		else:
			#''' Right branch '''
			if not root.right:
				root.right = Node(val)
			else:
				self._insert(val, root.right)

	def inorder(self):
		#'''If BST root has something is True'''
		if self.root:
			self._order_result = []
			#self._order_result *= 0 #fastest clear but didn't work
			self._inorder(self.root)
		else:
			#print("Nothing to print from inorder\n")
			return "Nothing to print from inorder\n"
		return self._order_result

	def _inorder(self, root):
		'''
		Take root, and recursively check
		Start from Left Root then Right
		'''
		#''' If root.left has something is True'''
		if root.left:
			self._inorder(root.left)
		#print("{}".format(root.data), end=", ")
		self._order_result.append(root.data)
		if root.right:
			self._inorder(root.right)

	def preorder(self):
		#''' if BST root has something is True'''
		if self.root:
			self._order_result = []
			#self._order_result *= 0 #fastest clear but didn't work?
			self._preorder(self.root)
		else:
			return "Nothing to print from  preorder\n"
		return self._order_result

	def _preorder(self, root):
		#''' if root left has something is True'''
		#print("{}".format(root.data), end=", ")
		self._order_result.append(root.data)
		if root.left:
			self._preorder(root.left)
		if root.right:
			self._preorder(root.right)

	def postorder(self):
		#''' if BST root has something is True'''
		if self.root:
			self._order_result = []
			#self._order_result *= 0 #fastest clear nut didn't work
			self._postorder(self.root)
		else:
			return "Nothing to print from postorder\n"
		return self._order_result

	def _postorder(self, root):
		#'''if root.left has something is True'''
		if root.left:
			self._postorder(root.left)
		if root.right:
			self._postorder(root.right)
		self._order_result.append(root.data)
		#print("{}".format(root.data), end=", ")


def main():

	bst = BST()
	in_ = bst.inorder()
	pre_ = bst.preorder()
	post_ = bst.postorder()

	for i in 25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90, 91, 92:
		bst.insert(i)
	in_ = bst.inorder()
	pre_ = bst.preorder()
	post_ = bst.postorder()
	print(in_)
	print(pre_)
	print(post_)
	
if __name__ == '__main__':
	main()
