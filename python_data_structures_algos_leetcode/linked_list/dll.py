class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doublelinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.length = 1
        self.head = new_node
        self.tail = new_node

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
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        self.tail = temp.prev
        temp.prev = None
        self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index > self.length / 2:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index)
        if temp:
            prev = temp.prev
            prev.next = new_node
            new_node.prev = prev
            new_node.next = temp
            temp.prev = new_node
            self.length += 1
            return True
        return False
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        return True

dll = doublelinkedlist(5)

dll.print_list()
print("")
dll.append(9)
dll.append(18)

dll.print_list()
print("")
dll.set_value(2, 27)
dll.insert(1, 55)
dll.print_list()
print("")
print(dll.get(2).value)

dll.remove(1)
print("")
dll.print_list()