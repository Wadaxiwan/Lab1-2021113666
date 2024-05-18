import networkx as nx
import matplotlib.pyplot as plt

class GraphHandler:
    def __init__(self):
        self.G = None

    def create_graph(self, input_text):
        self.G = nx.DiGraph()
        words = input_text.split()

        for i, word in enumerate(words):
            self.G.add_node(word)

        for i in range(len(words) - 1):
            if self.G.has_edge(words[i], words[i + 1]):
                # If the edge already exists, increase its weight by 1
                self.G[words[i]][words[i + 1]]['weight'] += 1
            else:
                # If the edge doesn't exist, create it with weight 1
                self.G.add_edge(words[i], words[i + 1], weight=1)

    def show_graph(self):
        plt.figure(figsize=(16, 10))
        pos = nx.spring_layout(self.G)
        weights = [self.G[u][v]['weight'] for u, v in self.G.edges()]
        nx.draw(self.G, pos, with_labels=True, arrows=True, node_size=1800, node_color='skyblue', font_size=18, font_weight='bold', width=weights)
        edge_labels = {(u, v): d['weight'] for u, v, d in self.G.edges(data=True)}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_size=18)
        plt.savefig('image/graph.png')
        plt.close()