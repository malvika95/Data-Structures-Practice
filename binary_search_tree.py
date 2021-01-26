from collections import defaultdict
class Node:
    def __init__(self,value):
        self.value=value
        self.left_child= None
        self.right_child=None

class Tree:
    def __init__(self):
        self.head=None
        self.prev = -1
        self.check = True
        self.traversePath = []


    def check_bst(self,node):
        if not node:
            return
        self.check_bst(node.left_child)
        if node.value <= self.prev:
            self.check = False
        self.prev = node.value
        self.check_bst(node.right_child)

    def search_bst(self,node,value):
        if not node:
            return
        if value == node.value :
            print("Found element")
        elif value < node.value :
            self.search_bst(node.left_child,value)
        else :
            self.search_bst(node.right_child,value)

    def bst_traversal(self,node,value):
        if not node:
            return
        self.traversePath.append(node.value)
        if value == node.value :
            print(self.traversePath)
        elif value < node.value :
            self.bst_traversal(node.left_child,value)
        else :
            self.bst_traversal(node.right_child,value)


    def insert_bst(self,node,value):
        if not node:
            return Node(value)
        if node.value ==value:
            return node
        elif value < node.value :
            node.left_child = self.insert_bst(node.left_child,value)
        else :
            node.right_child = self.insert_bst(node.right_child,value)
        return node

    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left_child)
        print(node.value)
        self.inorder(node.right_child)





if __name__ == "__main__":
    tree_obj = Tree()
    tree_obj2=Tree()
    root = Node(5)
    tree_obj.head = root
    tree_obj.head.left_child = Node(2)
    tree_obj.head.left_child.left_child = Node(1)
    tree_obj.head.right_child = Node(7)
    tree_obj.head.left_child.right_child = Node(4)
    tree_obj.head.right_child.right_child = Node(10)
    # tree_obj.check_bst(tree_obj.head)
    # if not tree_obj.check:
    #     print("Not a BST!!!")
    # else :
    #     print("BST!!!!")
    # tree_obj.search_bst(tree_obj.head,10)
    # tree_obj2.head= tree_obj2.insert_bst(tree_obj2.head,3)
    # # tree_obj2.inorder(tree_obj2.head)
    # tree_obj2.insert_bst(tree_obj2.head,9)
    # # tree_obj2.inorder(tree_obj2.head)
    # tree_obj2.insert_bst(tree_obj2.head,3)
    # tree_obj2.inorder(tree_obj2.head)
    tree_obj.bst_traversal(tree_obj.head,4)
    # print(tree_obj.traversePath)
    # print(tree_obj.traversePath)
