"""Home work 6_2"""
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from hw_6_1 import G
from hw_6_1 import positions, color_map

def update(frame):
    ax.clear()  # Clear the previous frame
    # Nodes and labels
    nx.draw_networkx_nodes(G, pos=positions, ax=ax, node_color=color_map, node_size=300)
    nx.draw_networkx_labels(G, pos=positions, ax=ax)
    # Edges for the graph and weight labels
    nx.draw_networkx_edges(G, pos=positions, ax=ax, edge_color='gray', alpha=0.7)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=labels)
    
    # Draw shortest paths up to the current frame
    for _, path in shortest_paths.items():
        ax.set_title(f"Going from {source_node}, step {frame + 1}")  # Set the title
        if len(path) > frame:  # Only draw edges for paths up to the current frame
            path_edges = [(path[i], path[i + 1]) for i in range(frame)]
            # draw current path and path to we going
            nx.draw_networkx_edges(G, pos=positions, ax=ax, edgelist=path_edges, edge_color='blue', width=2)
        

fig, ax = plt.subplots(figsize=(20, 15))

source_node = input("Input source node:")
source_node = source_node if source_node else "INET1"
shortest_paths = nx.single_source_dijkstra_path(G, source=source_node, weight='weight')
print(shortest_paths) 
# Create the animation
ani = FuncAnimation(fig, update, frames=len(max(shortest_paths.values(), key=len)), interval=1000)
plt.show()
