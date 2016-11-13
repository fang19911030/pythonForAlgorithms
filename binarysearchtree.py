# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:51:49 2016

@author: fang2
"""

class Node(object):
    def __init__(self,key,data,left=None,right=None,parent=None):
        self.key=key
        self.data=data
        self.rightchild=right
        self.leftchild=left
        self.parent=None
    
    def isLeftChild(self):
        return self.parent and self.parent.leftchild==self
        
    def isRightChild(self):
        return self.parent and self.parent.rightchild==self
        
    def hasRightChild(self):
        return self.rightchild!=None
        
    def hasLeftChild(self):
        return self.leftchild!=None
        
    def hasBothChild(self):
        return self.leftchild!=None and self.rightchild!=None
        
    def isRoot(self):
        return self.parent==None
        
    def isLeaf(self):
        return self.leftchild==None and self.rightchild==None
        
#    def __str__(self):
#        return str(self.key), str(self.data)
        
    
class BinarySearchTree():
    def __init__(self):
        self.root=None
        self.size=0
        
    def __len__(self):
        return self.size
        
    def length(self):
        return self.size
        
    def treeInsert(self,z):
        y=None
        x=self.root
        while x!=None:
            y=x
            if z.key<x.key:
                x=x.leftchild
            else:
                x=x.rightchild
        z.parent=y
        if y==None:
            self.root=z
            self.size+=1
        elif z.key<y.key:
            y.leftchild=z
            self.size+=1
        else:
            y.rightchild=z
            self.size+=1
    def inorderTreeWalk(self,node):
        temp=node
        if temp!=None:
            self.inorderTreeWalk(temp.leftchild)
            print (temp.key)
            self.inorderTreeWalk(temp.rightchild)
    def get(self,key):
        currentnode=self.root
        if currentnode==None or key==currentnode.key:
            return currentnode
        if key<self.root.key:
            return self._get(currentnode.leftchild,key)
        else:
            return self._get(currentnode.rightchild,key)
            
#    def _get(self,currentnode,key):
#        if currentnode==None or key==currentnode.key:
#            print (currentnode)
#            return currentnode
#        elif key<self.root.key:
#            return self._get(currentnode.leftchild,key)
#        else:
#            return self._get(currentnode.rightchild,key)
            
    def _get(self,currentNode,key):
        if not currentNode:
            return None
        elif currentNode.key ==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(currentNode.leftchild,key)
        else:
            return self._get(currentNode.rightchild,key)
            
    def __getitem__(self,key):
        node=self.get(key)
        
        return node.data
        
    def treeMinimum(self,node):
        temp=node
        while temp.leftchild!=None:
            temp=temp.leftchild
        return temp
        
    def treeMaximum(self,node):
        temp=node
        while temp.rightchild!=None:
            temp=temp.rightchild
        return temp
        
    def treeSuccessor(self,node):
        temp=node
        if temp.rightchild!=None:
            return self.treeMinimum(temp.rightchild)
        y=temp.parent
        while y!=None and temp==y.right:
            temp=y
            y=y.p
        return y
        
    def _transplant(self,u,v):
        if u.parent==None:
            self.root=v
            self.size-=1
        elif u.isLeftChild():
            u.parent.leftchild=v
            self.size-=1
        else:
            u.parent.rightchild=v
            self.size-=1
        if v!=None:
            v.parent=u.parent
            
    def treeDelete(self,node):
        if not node.hasLeftChild():
            self._transplant(node,node.rightchild)
        elif not node.hasRightChild():
            self._transplant(node,node.leftchild)
        else:
            y=self.treeMinimum(node.rightchild)
            if y.parent!=node:
                self._transplant(y,y.rightchild)
                y.rightchild=node.rightchild
                y.rightchild.parent=y
            self._transplant(node,y)
            y.leftchild=node.leftchild
            y.leftchild.parent=y
            
        
        
        

            
            
            
mytree=BinarySearchTree()
node1=Node(15,2)
node2=Node(2,3)
node3=Node(18,3)
node4=Node(1,0)
node5=Node(3,0)
node6=Node(17,0)
node7=Node(19,0)
mytree.treeInsert(node1)
mytree.treeInsert(node2)
mytree.treeInsert(node3)
mytree.treeInsert(node4)
mytree.treeInsert(node5)
mytree.treeInsert(node6)
mytree.treeInsert(node7)
#print (len(mytree))
#mytree.inorderTreeWalk(node1)
print("------------------------")
#print(mytree[19])
#print (mytree.treeMinimum(node1))
mytree.treeDelete(node3)
print (len(mytree))
#mytree.inorderTreeWalk(node1)
#print (node6.data)
print (mytree[3])
#print (mytree[3])
                
                
                
                
                
                
                
                
                
                
                
        