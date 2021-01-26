class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None

    def show_list(self):
        current=self.head
        while current:
            print(current.value)
            current = current.next

    def recursive_show_list(self,Node):
        if Node is None:
            return
        print(Node.value)
        self.recursive_show_list(Node.next)

    def recursive_show_reverse_list(self,Node):
        if Node is None:
            return
        self.recursive_show_reverse_list(Node.next)
        print(Node.value)

    def recursive_length_list(self,Node):
        if Node is None:
            return 0
        return self.recursive_length_list(Node.next)+1

    def insert_list(self,value):
        if not self.head:
            self.head=Node(value)
            return
        current=self.head
        while current.next is not None:
            current=current.next
        insert_node=Node(value)
        current.next=insert_node

    def delete_list(self,value):
        if not self.head:
            return
        if self.head.next is None:
            if self.head.value == value:
                self.head=None
                return
        current = self.head
        while current.next and current.next.value != value :
            current = current.next
        if current.next:
            current.next = current.next.next

    def reverse(self):
        self.head = self.reverse_list(self.head)

    def reverse_list(self, current):
        if current is None:
            return current
        current.next = self.reverse_list(current.next)
        return current



if __name__== "__main__":
    list_obj=LinkedList()
    list_obj.insert_list(3)
    list_obj.insert_list(7)
    list_obj.insert_list(8)
    list_obj.insert_list(9)
    print("List after inserting")
    list_obj.recursive_show_list(list_obj.head)
    # list_obj.reverse()
    # print("List after reversal")
    # list_obj.recursive_show_reverse_list(list_obj.head)
    print("Length of list")
    n = list_obj.recursive_length_list(list_obj.head)
    print(n)
    # list_obj.show_list()
    # list_obj.recursive_show_list(list_obj.head)
