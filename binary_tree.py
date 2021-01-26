from collections import defaultdict
class Node:
    def __init__(self,value):
        self.value=value
        self.left_child= None
        self.right_child=None

class Tree:
    def __init__(self):
        self.head=None
        self.depth_count=defaultdict(list)
        self.queue=[]
        self.stack=[]
        self.vertical_order = defaultdict(list)
        # self.traversal =[]


    # def create_tree(self,value):
        # if not self.head:
        #     self.head=Node(value)
        # current=self.head
        # while current.left_child is not None:
        #     current=current.left_child
        # insert_left_child = Node(value)
        # current.left_child = insert_left_child
        # while current.right_child is not None:
        #     current=current.right_child
        # insert_right_child = Node(value)
        # current.right_child = insert_right_child

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left_child)
        print(node.value)
        self.inorder(node.right_child)

    def pre_order(self, node):
        if not node:
            return
        print(node.value)
        self.pre_order(node.left_child)
        self.pre_order(node.right_child)

    def post_order(self,node,count):
        if not node:
            return 0
        count_left=self.post_order(node.left_child,count)
        count_right=self.post_order(node.right_child,count)
        # print(node.value)
        return count_left+count_right+1

    def sum_post_order(self, node):
        if not node:
            return 0
        sum_left=self.sum_post_order(node.left_child)
        sum_right=self.sum_post_order(node.right_child)
        # print(node.value)
        return sum_left+sum_right+node.value

    def height_post_order(self,node):
        if not node:
            return 0
        height_left = self.height_post_order(node.left_child)
        height_right = self.height_post_order(node.right_child)
        return max(height_left,height_right)+1

    def find_node(self,node,value):
        if not node:
            return
        if node.value == value:
            print("Found value "+str(value))
            return
        self.find_node(node.left_child,value)
        self.find_node(node.right_child,value)

    def find_node_with_depth(self,node,value,depth):
        if not node:
            return
        if node.value == value:
            print("Found value "+str(value)+" at depth "+str(depth))
            return
        self.find_node_with_depth(node.left_child,value,depth+1)
        self.find_node_with_depth(node.right_child,value,depth+1)

    def tree_levels(self,node,depth):
        if not node:
            return
        self.depth_count[depth].append(node.value)
        self.tree_levels(node.left_child,depth+1)
        self.tree_levels(node.right_child,depth+1)

    def leaf_nodes(self,node):
        if not node:
            return None
        left_child_node=self.leaf_nodes(node.left_child)
        right_child_node=self.leaf_nodes(node.right_child)
        if (not left_child_node) and (not right_child_node):
            print(node.value)
        return True

    def level_order_traversal(self):
        if len(self.queue) == 0:
            return
        element = self.queue.pop(0)
        print(element.value)
        if element.left_child:
            self.queue.append(element.left_child)
        if element.right_child:
            self.queue.append(element.right_child)
        self.level_order_traversal()

    def vertical_order_traversal(self,node,depth):
        if not node:
            return
        self.vertical_order[depth].append(node.value)
        self.vertical_order_traversal(node.left_child,depth-1)
        self.vertical_order_traversal(node.right_child,depth+1)

    def depth_first_traversal(self):
        if len(self.stack) == 0:
            return
        element = self.stack.pop()
        print(element.value)
        if element.left_child:
            self.stack.append(element.left_child)
        if element.right_child:
            self.stack.append(element.right_child)
        self.depth_first_traversal()

    def stack_inorder(self):
        if not self.stack:
            return
        while self.stack:
            element = self.stack[-1]
            if element.left_child:
                self.stack.append(element.left_child)
            if element.right_child:
                self.stack.append(element.right_child)

    def root_to_leaf_traversal(self,node,traversal):
        if not node:
            return
        traversal.append(node.value)
        if not node.left_child and not node.right_child :
            print(traversal)
        self.root_to_leaf_traversal(node.left_child,traversal)
        self.root_to_leaf_traversal(node.right_child,traversal)
        traversal.pop()

    # def show_tree(self):
        # if not self.head.left_child and not self.head.right_child:
        #     print(self.head.value)
        # print("head")
        # print(self.head.value)
        # current=self.head
        # print("left child")
        # while current.left_child is not None:
        #     current=current.left_child
        #     print(current.value)
        # print("right child")
        # current=self.head
        # while current.right_child is not None:
        #     current=current.right_child
        #     print(current.value)


if __name__ == "__main__":
    tree_obj = Tree()
    root = Node(5)
    tree_obj.head = root
    tree_obj.head.left_child = Node(7)
    tree_obj.head.left_child.left_child = Node(1)
    tree_obj.head.right_child = Node(9)
    tree_obj.head.right_child.left_child = Node(4)
    tree_obj.head.right_child.right_child = Node(2)
    tree_obj.head.left_child.right_child = Node(3)
    tree_obj.inorder(tree_obj.head)
    print("preorder \n")
    tree_obj.pre_order(tree_obj.head)
    count = tree_obj.post_order(tree_obj.head,0)
    print("Count of nodes "+str(count))
    sum = tree_obj.sum_post_order(tree_obj.head)
    print("sum of nodes " + str(sum))
    height = tree_obj.height_post_order(tree_obj.head)
    print("Height of tree "+ str(height))
    tree_obj.find_node(tree_obj.head,1)
    # tree_obj.find_node_with_depth(tree_obj.head,9,0)
    # tree_obj.tree_levels(tree_obj.head,0)
    # print(list(tree_obj.depth_count.values()))
    tree_obj.leaf_nodes(tree_obj.head)
    print("level_order_traversal")
    tree_obj.queue.append(tree_obj.head)
    tree_obj.level_order_traversal()
    print("depth first traversal")
    tree_obj.stack.append(tree_obj.head)
    tree_obj.depth_first_traversal()
    print("root to tree traversal")
    tree_obj.root_to_leaf_traversal(tree_obj.head,[])
    print("vertical order traversal")
    tree_obj.vertical_order_traversal(tree_obj.head,0)
    print(tree_obj.vertical_order.values())
