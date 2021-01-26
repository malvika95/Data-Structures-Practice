
class Stack :
    def __init__(self):
        self.max_length = 5
        self.top=-1
        self.arr = [None] * self.max_length

    def push(self,value):
        if self.top == self.max_length-1:
            print("Stack overflow")
        else:
            self.top=self.top+1
            self.arr[self.top]=value

    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            self.top=self.top-1

    def show_stack(self):
        for i in range(self.top+1):
            print(self.arr[i])

if __name__ =="__main__":
    stack_obj = Stack()
    stack_obj.push(8)
    stack_obj.push(11)
    stack_obj.push(21)
    stack_obj.push(32)
    stack_obj.push(12)
    stack_obj.pop()
    stack_obj.pop()
    stack_obj.pop()
    stack_obj.pop()
    stack_obj.pop()
    stack_obj.pop()
    stack_obj.show_stack()
