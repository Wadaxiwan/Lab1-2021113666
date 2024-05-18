'''没有检查过'''
import networkx as nx
import matplotlib.pyplot as plt

class GraphHandler:
    def __init__(self):
        self.G = nx.DiGraph()

    def create_graph(self, input_text):
        words = input_text.split()
        
        for i in range(len(words) - 1):
            if self.G.has_edge(words[i], words[i + 1]):
                # If the edge already exists, increase its weight by 1
                self.G[words[i]][words[i + 1]]['weight'] += 1
            else:
                # If the edge doesn't exist, create it with weight 1
                self.G.add_edge(words[i], words[i + 1], weight=1)

    def show_graph(self, shortest_path=None):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.G)
        weights = [self.G[u][v]['weight'] for u, v in self.G.edges()]

        nx.draw(self.G, pos, with_labels=True, arrows=True, node_size=800, node_color='skyblue', font_size=10, font_weight='bold', width=weights)
        edge_labels = {(u, v): d['weight'] for u, v, d in self.G.edges(data=True)}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_size=8)

        if shortest_path:
            path_edges = list(zip(shortest_path, shortest_path[1:]))
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='r', width=2)

        plt.show()

    def get_shortest_path(self, source, target):
        return nx.shortest_path(self.G, source=source, target=target, weight='weight')


if __name__ == "__main__":
    handler = GraphHandler()
    input_text = "This is a simple example to demonstrate the shortest path in a directed graph"
    handler.create_graph(input_text)

    # Example: Find the shortest path from 'This' to 'graph'
    source = 'This'
    target = 'graph'
    try:
        shortest_path = handler.get_shortest_path(source, target)
        print(f"Shortest path from {source} to {target}: {shortest_path}")
        handler.show_graph(shortest_path=shortest_path)
    except nx.NetworkXNoPath:
        print(f"No path found between {source} and {target}")
