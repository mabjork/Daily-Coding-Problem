
class Node():
    def __init__(self, pn, nn, node_id):
        self.node_id = node_id
        self.prev_node = pn
        self.next_node = nn
        if (pn != None):
            pn.setNext(self)
        if (nn != None):
            nn.setPrev(self)

    def __str__(self):
        return self.node_id

    def __repr__(self):
        return self.node_id

    def remove(self):
        if(self.prev_node != None):
            print("Prev", self.prev_node)
            print("Next", self.next_node)
            self.prev_node.next_node = self.next_node
        if(self.next_node != None):
            self.next_node.prev_node = self.prev_node

    def setNext(self, node):
        self.next_node = node

    def setPrev(self, node):
        self.prev_node = node

    def isFirst(self):
        return self.prev_node == None

    def isLast(self):
        return self.next_node == None


node1 = Node(None, None, "Node1")
node2 = Node(node1, None, "Node2")
node3 = Node(node2, None, "Node3")
node4 = Node(node3, None, "Node4")

def removeKthLastNode(first_node, k):
    nodes_map = {0: first_node}
    current_node = first_node
    node_num = 1
    while True:
        node_num += 1
        current_node = current_node.next_node
        nodes_map[node_num] = current_node        
        if (current_node.isLast()):
            break

    nodes_map[node_num - k].remove()
    return nodes_map[0]

print(removeKthLastNode(node1, 1))
print(node2.next_node)
    

    
