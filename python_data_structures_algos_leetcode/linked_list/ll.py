class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.length -= 1
            ret = self.head
            self.head = None
            self.tail = None
            return ret
        else:
            temp = self.head
            tn = temp.next
            while tn.next is not None:
                temp = tn
                tn = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1
            return tn


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        else:
            ret = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return ret


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp
    
    def set_value(self, index, value):
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = value
            return True
        else:
            return False
        
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        tmp = self.head
        tmp = self.get(index - 1)
        new_node.next = tmp.next
        tmp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        tmp = self.get(index - 1)
        ret = tmp.next
        tmp.next = ret.next
        self.length -= 1
        ret.next = None
        return ret
    
    def reverse(self):
        if self.length <= 1:
            return False
        prev = self.tail
        self.tail = self.head
        self.head = prev

        prev = self.tail
        nnode = prev.next
        prev.next = None

        while nnode is not None:
            cur = nnode
            nnode = nnode.next
            cur.next = prev
            prev = cur
        return True


mll = LinkedList(0)

mll.append(1)
mll.append(2)
mll.append(3)
mll.set_value(2, 13)

a = mll.get(2)
print(f"index 2 value is now [{a.value}]")
mll.insert(0, 56)

print("list is now")
mll.print_list()

mll.remove(3)
print("list is now")
mll.print_list()

mll.reverse()
print("Reversed list")
mll.print_list()
