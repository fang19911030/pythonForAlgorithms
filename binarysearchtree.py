# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:03:50 2016

@author: pengcheng
"""

class BSTNode:
    
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key=key
        self.value=value
        self.parent=parent
        self.left=left
        self.right=right
        
class MyBST:
    
    def __init__(self):
        self.root=None
        
    def find_recursive(self,node,key):
        
        if None==node or key ==node.key:
            return node
        elif key<node.key:
            return self.find_recursive(node.left,key)
        else: 
            return self.find_recursive(node.right,key)
            
    def find_interative(self, node, key):
        current_node=node
        while current_node:
            if key==current_node.key:
                return current_node
            elif key<current_node.key:
                current_node=current_node.left
            else:
                current_node=current_node.right
        return None
        
        
            
    def search(self,key):
        
        return self.find_recursive(self.root,key)
        
    def insert(self, key, value):
        if None ==self.root:
            self.root=BSTNode(key,value)
            return True
            
        current_node=self.root
        while current_node:
            if key==current_node.key:
                print ("The key does exist!")
                return False
                
            elif key<current_node.key:
                if current_node.left:
                    current_node=current_node.left
                else:
                    current_node.left=BSTNode(key,value,current_node)
                    return True
            else:
                if current_node.right:
                    current_node=current_node.right
                else:
                    current_node.right=BSTNode(key,value,current_node)
                    return True
            
    def replace_node(self, node, new_node):
        
        if node ==self.root:
            self.root=new_node
            return
            
        parent=node.parent 
        if parent.left and parent.left==node:
            parent.left=new_node
        elif parent.right and parent.right==node:
            parent.right=new_node
        else:
            print ("Incorrect parent-children relation!")
            raise RuntimeError
            
            
    def remove_node(self,node):
        if node.left and node.right:
            successor=node.right
            while successor.left:
                successor = successor.left
                
            node.key=successor.key
            node.value=successor.value
            
            self.remove_node(successor)
        elif node.left:
            self.replace_node(node,node.left)
        elif node.right:
            self.replace_node(node,node.right)
        else:
            self.replace_node(node, None)
    def delete(self,key):
        node=self.search(key)
        if node:
            self.remove_node(node)
            
            
def traverse_in_order(node, callback_function):
        
    if node is None:
        return
            
    traverse_in_order(node.left,callback_function)
    callback_function(node)
    traverse_in_order(node.right,callback_function)
    
def sort_by_BST(values):
    result=[]
    bst=MyBST()
    
    for v in values:
         bst.insert(v,0)
            
        
    traverse_in_order(bst.root,lambda n: result.append(n.key))
    return result
a=[2,3,1,4,6,5,8,7,9]
bst=MyBST()
for value in a:
    bst.insert(value,0)
    
print(bst.search(4))
print (sort_by_BST([2,4,3,5,1,7,6,8,9]))