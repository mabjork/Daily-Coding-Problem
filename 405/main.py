import math

class Node:
    def __init__(self, value, left, right):
        super().__init__()
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "Node(value=%s, left=%s, right=%s)" % (self.value, self.left.__str__() if self.left != None else None, self.right.__str__() if self.right != None else None)
    def __repr__(self):
        return "Node(value=%s, left=%s, right=%s)" % (self.value, self.left.__str__() if self.left != None else None, self.right.__str__() if self.right != None else None)

node1 = Node(1, None, None)
node2 = Node(3, None, None)
parent1 = Node(2, node1, node2)
parent2 = Node(4, None, None)
grand_parent = Node(5, parent1, parent2)

def is_bst(tree):
    if(tree.left == None and tree.right == None):
        return True
    root_is_valid = tree.value > tree.left.value and tree.value < tree.right.value
    left_is_valid = (root_is_valid and is_bst(tree.left)) if tree.left != None else True
    right_is_valid = (root_is_valid and is_bst(tree.right)) if tree.right != None else True
    return root_is_valid and left_is_valid and right_is_valid



def check_tree(node):
    if(node.left == None and node.right == None):
        return (1, node)
    elif(node.left != None and node.right == None):
        if (node.left.value <= node.value):
            (val, _) = check_tree(node.left)
            return (val + 1, node)
        else:
             return (0, node)
    elif(node.right != None and node.left == None):
        if (node.right.value >= node.value):
            (val, _) = check_tree(node.right)
            return (val + 1, node)
        else:
             return (0, node)
    else:
        (left_val, left_node) = check_tree(node.left)
        (right_val, right_node) = check_tree(node.right)
        if (node.right.value >= node.value and node.left.value <= node.value):
            return (left_val + right_val + 1, node)
        else:
            if (left_val >= right_val):
                return (left_val, left_node)
            else:
                return (right_val, right_node)

print(check_tree(grand_parent))