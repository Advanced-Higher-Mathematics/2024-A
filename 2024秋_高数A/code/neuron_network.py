import matplotlib.pyplot as plt
import networkx as nx

# 创建神经网络的图形
G = nx.DiGraph()

# 定义每层的节点
input_layer = ['Input 1', 'Input 2', 'Input 3']
hidden_layer = ['Hidden 1', 'Hidden 2']
output_layer = ['Output 1']

# 添加节点到图中
G.add_nodes_from(input_layer + hidden_layer + output_layer)

# 添加连接（权重）
edges = [('Input 1', 'Hidden 1'), ('Input 1', 'Hidden 2'),
         ('Input 2', 'Hidden 1'), ('Input 2', 'Hidden 2'),
         ('Input 3', 'Hidden 1'), ('Input 3', 'Hidden 2'),
         ('Hidden 1', 'Output 1'), ('Hidden 2', 'Output 1')]

G.add_edges_from(edges)

# 设置布局
pos = {
    'Input 1': (0, 2),
    'Input 2': (0, 1),
    'Input 3': (0, 0),
    'Hidden 1': (1, 1.5),
    'Hidden 2': (1, 0.5),
    'Output 1': (2, 1)
}

# 绘制节点
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')

# 绘制连接
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=20)

# 显示图形
plt.title('Simple Neural Network')
plt.show()
