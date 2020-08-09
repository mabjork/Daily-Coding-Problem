
class Node:
    def __init__(self):
        self.ingoing_links = []
        self.outgoing_links = []
        super().__init__()

    def add_outgoing_link(self, node):
        node.ingoing_links.append(self)
        self.outgoing_links.append(node)
    
    def add_ingoing_link(self, node):
        node.outgoing_links.append(self)
        self.ingoing_links.append(node)
        

    def calculate_score(self, dampening_factor, num_sites):
        score = (1 - dampening_factor) / num_sites
        for node in self.ingoing_links:
            score += dampening_factor * node.calculate_score(dampening_factor, num_sites) / len(node.outgoing_links)
        
        return score

node1 = Node()
node2 = Node()
node3 = Node()

node3.add_ingoing_link(node1)
node3.add_ingoing_link(node2)
print(node2.outgoing_links)

print(node3.calculate_score(0.85, 3))