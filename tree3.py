#! /usr/bin/python3

class Node:
	def __init__(self, data, left=None, right=None):
		self.left = left
		self.right = right
		self.data = data

class BST:
	def __init__(self):
		self.root = None

	def insert( self, x):
		if not self.root :
			self.root = Node(x)
			print("root : %d"%x)
		else:
			self._insert(x, self.root)

	""" insert helper """
	def _insert( self, x, root):
		if x < root.data:
			"""If root.left doesnt have anything is true """
			if not root.left:
				root.left=Node(x)
				print("left : %d"%x)
			else:
				self._insert(x, root.left)
		else:
			if not root.right:
				root.right = Node(x)
				print("right: %d"%x)
			else:
				self._insert(x, root.right)

	def inorder(self):
		self._inorder(self.root)

	""" inorder helper """
	def _inorder(self, root):
		if root:
			if root.left:
				self._inorder( root.left)
			print("%d"%root.data, end=", ")
			if root.right:
				self._inorder( root.right)

	def preorder(self):
		self._preorder( self.root)

	""" preorder helper """
	def _preorder( self, root):
		if root:
			print("%d"%root.data, end=", ")
			if root.left:
				self._preorder( root.left)
			if root.right:
				self._preorder( root.right)

	""" postorder helper """
	def postorder(self):
		self._postorder( self.root)

	def _postorder(self, root):
		if root:
			if root.left:
				self._postorder( root.left )
			if root.right:
				self._postorder( root.right )
			print("%d"%root.data, end=", ")

	def find(self, x):
		if not self.root:
			return False
		else:
			return self._find( x, self.root )

	def _find(self, x, root):
		
		if not root:
			return False
		elif x == root.data:
			return True
		elif x < root.data:
			return self._find(x , root.left)
		else:
			return self._find(x, root.right)

def inorder(root):
	if root.left :
		inorder(root.left)
	print("%d"%root.data, end=", ")
	if root.right:
		inorder(root.right)


def preorder(root):
	print("%d"%root.data, end=", ")
	if root.left:
		preorder(root.left)	
	if root.right:
		preorder(root.right)


def postorder(root):
	if root.left:
		postorder(root.left)
	if root.right:
		postorder(root.right)
	print("%d"%root.data, end=", ")

def get_height(root):
	if not root:
		return 0
	else:
		return 1+max( get_height( root.left), get_height(root.right))

bst = BST()
for i in 25,15,50,10,22,35,70,4,12,18,24,31,44,66,90,91,92:
	bst.insert(i)

inorder(bst.root)

print("\n")
preorder(bst.root)
print("\n")
postorder(bst.root)
print("\n")
print("Tree height is %d"%get_height(bst.root) )
print("\n")

bst.inorder()
print("\n")
bst.preorder()
print("\n")
bst.postorder()
print("\n")

print("{:>7} {}".format(  str(bst.find(25) ), bst.find(5) ) )
print("{0}".format(  bst.find(25) ) )
print("%s"%bst.find(25) )
