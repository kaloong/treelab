#! /usr/bin/python3

class Node:
	def __init__(self,data):
		self.left  = None
		self.right = None
		self.data  = data

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data, end=", ")
		inorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.data, end=", ")

def preorder(root):
	if root:
		print(root.data, end=", ")
		preorder(root.left)
		preorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("\n--- Preorder ---")
preorder(root)
print("\n--- Inorder ---")
inorder(root)
print("\n--- Postorder ---")
postorder(root)
print("\n")