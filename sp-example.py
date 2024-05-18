import networkx as nx
import matplotlib.pyplot as plt

# 创建一个有向图
G = nx.DiGraph()

# 添加节点和边
edges = [
    ('A', 'B', 1),
    ('A', 'C', 2),
    ('B', 'D', 1),
    ('C', 'D', 1),
    ('C', 'E', 3),
    ('D', 'E', 1)
]
G.add_weighted_edges_from(edges)

# 指定起点和终点
source = 'A'
target = 'E'

# 计算最短路径
shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')

# 绘制图形
pos = nx.spring_layout(G)  # 布局算法来计算节点位置
plt.figure()

# 绘制所有节点和边
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=16)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# 绘制最短路径
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# 显示图形
plt.title(f'Shortest Path from {source} to {target}')
plt.show()
