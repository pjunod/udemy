'''
Merge Two Sorted LL ( ** Interview Question)
Description

The merge method takes in another LinkedList as an input and merges it with the current LinkedList.

The elements in both lists are assumed to be in ascending order.

Parameters

other_list (LinkedList): the other LinkedList to merge with the current list



Return Value

This method does not return a value, but it modifies the current LinkedList to contain the merged list.
'''

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
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    def merge(self, other_list):
        other_head = other_list.head
        merge_list = Node(0)
        current = merge_list
        self.length = 0
        while self.head != None and other_head != None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
            self.length += 1
        
        if self.head != None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
        
        self.length += other_list.length
        self.head = merge_list.next

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""