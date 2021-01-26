
class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class StackList:
    def __init__(self):
        self.head=None
        self.tail=None

    def show_list(self):
        current=self.head
        while current:
            print(current.value)
            current = current.next

    def push(self,value):
        if not self.head:
            self.head=Node(value)
            self.tail=self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next


    def pop(self):
        if not self.head:
            return
        if self.head.next is None:
            self.head=None
            self.tail=None
            return
        current=self.head
        while current.next!=self.tail:
            current=current.next
        self.tail =current
        self.tail.next=None

if __name__ == "__main__":
    obj = StackList()
    obj.push(4)
    obj.push(3)
    obj.push(8)
    obj.push(20)
    obj.show_list()
    obj.pop()
    obj.pop()
    obj.show_list()
