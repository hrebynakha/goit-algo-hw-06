"""Home work 6_2"""
import networkx as nx
import matplotlib.pyplot as plt
from hw_6_1 import G
from hw_6_1 import positions, color_map

if __name__ == "__main__":
    tree = input("Input tree that want to draw bfs or dfs(default):")
    if tree == "bfs":
        bfs_tree = nx.bfs_tree(G, source='INET1')
        nx.draw_networkx(bfs_tree, pos=positions, with_labels=True, node_color=color_map)
        plt.title("BFS tree for Corporate network")
    else:
        dfs_tree = nx.dfs_tree(G, source='INET1')
        nx.draw_networkx(dfs_tree, pos=positions, with_labels=True, node_color=color_map)
        plt.title("DFS tree for Corporate network")
    plt.show()