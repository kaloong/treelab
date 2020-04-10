#! /usr/bin/python3

import unittest
from tree4 import *

class TestBST(unittest.TestCase):
    def setUp(self):
        self._bst = BST()
        for i in 25,15,50,10,22,35,70,4,12,18,24,31,44,66,90,91,92:
            self._bst.insert(i)

    #def tearDown(self):
    #	self._bst =None

    def testInsert(self):
        for i in 25,15,50,10,22,35,70,4,12,18,24,31,44,66,90,91,92:
            self.assertTrue( self._bst.insert(i) )

    def testInorder(self): 
    	self.assertEquals([4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90, 91, 92], self._bst.inorder() )

    def testPreorder(self):
    	self.assertEquals([25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90, 91, 92], self._bst.preorder() )

    def testPostorder(self):
    	self.assertEquals([4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 92, 91, 90, 70, 50, 25], self._bst.postorder() )

suite = unittest.makeSuite(TestBST)
unittest.TextTestRunner(verbosity=2).run(suite)