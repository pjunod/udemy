# BST nodes have left and right attributes in addition to value
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if temp.value == new_node.value:
                return False
            if temp.value < new_node.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
    
    
    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        
        


mybst = BinarySearchTree()

mybst.insert(27)
print(mybst.root.value)

mybst.insert(39)
print(mybst.root.right.value)
mybst.insert(15)
print(mybst.root.left.value)