"""Home work 6_1"""
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

positions = {}
color_map = []

# function
def add_node(node_name, **options):
    G.add_node(node_name, **options)

def add_edges(lst, **options):
    G.add_edges_from(lst, **options)

def add_computers(dest="P", pos_x=None, pos_y=None, count=10, color="blue"):
    names = []
    for i in range(1, count+1):
        pos_x_ = i if pos_x is None else pos_x
        pos_y_ = i if pos_y is None else pos_y
        node_name=f"{dest}{i}"
        names.append(node_name)
        add_node(node_name,)
        color_map.append(color)
        positions[node_name] = (pos_x_, pos_y_)
    return names

def add_servers(type, pos_x=None, pos_y=None, count=10, color="red"):
    names = []
    for i in range(1, count+1):
        pos_x_ = i if not pos_x else pos_x
        pos_y_ = i if not pos_y else pos_y
        node_name = f"S{type}{i}"
        names.append(node_name)
        add_node(node_name,)
        color_map.append(color)
        positions[node_name] = (pos_x_, pos_y_)
    return names

def add_comutators(type, pos_x=None, pos_y=None, count=10, color="green"):
    names = []
    for i in range(1, count+1):
        pos_x_ = i if not pos_x else pos_x
        pos_y_ = i if not pos_y else pos_y
        node_name = f"{type}{i}"
        names.append(node_name)
        add_node(node_name,)
        color_map.append(color)
        positions[node_name] = (pos_x_, pos_y_)
    return names

def comutate_objects(objects_from, obj_to, weight):
    lst = [(obj_from, obj_to) for obj_from in objects_from]
    add_edges(lst, weight=weight)
    objects_from.append(obj_to)
    return [objects_from]

def group_elements(objects, pos_x=None, pos_y=None, x_from=None, y_from=None, distance=1):
    for i, el in enumerate(objects):
        if el in positions:
            pos_x_ = i * distance if pos_x is None else pos_x
            pos_y_ = i * distance if pos_y is None else pos_y
            delta_x = 0 if x_from is None else x_from
            delta_y = 0 if y_from is None else y_from
            #print(f"Changing element {el} position", positions[el], pos_x_ + delta_x, pos_y_ + delta_y)
            positions[el] = pos_x_ + delta_x, pos_y_ + delta_y
        else:
            pass
            #print("Missing position for el", el)

def comutate_servers(servers, comutator_index, pos_y=5, x_from=0, distance=2, weight=2, append=1):
    # comutating auth servers to dc comutator
    comutate_objects(servers[:1], local_comutators[comutator_index],1)
    group_elements(servers[:1], pos_y=pos_y, x_from=x_from, distance=distance)
    comutate_objects(servers[1:], local_comutators[comutator_index+1], weight)
    group_elements(servers[1:], pos_y=pos_y, x_from=x_from+45, distance=distance)

def comutate_pc(computers, router_index, pos_y=5, x_from=0, distance=2, weight=2,  append=1):
    comutate_objects(computers, net_routers[router_index], 1)
    group_elements(computers, pos_y=pos_y, distance=2, x_from=x_from)
    group_elements([net_routers[router_index]], pos_y=pos_y+append, x_from=x_from+3)

# creating objects
office_pcs = add_computers(count=15,)
factory_pcs = add_computers(dest="F",count=10, color="skyblue")

auth_servers = add_servers("A", count=2,)
mail_servers = add_servers("M", count=2, color="cyan")
web_servers = add_servers("W", count=2, color="brown")
file_servers = add_servers("F",count=2, color="yellow")

net_routers = add_comutators("R", count=5, color="greenyellow")
local_comutators = add_comutators("L", count=6, color="lime")
dc_comutators = add_comutators("D", count=3, color="green")
inet_comutator = add_comutators("INET", pos_x=30, pos_y=10, count=1, color="darkgreen")

comutate_pc(office_pcs[:5], router_index=0, pos_y=1, weight=0)
comutate_pc(office_pcs[5:10], router_index=1, pos_y=0, weight=5, x_from=10, append=2)
comutate_pc(office_pcs[10:], router_index=2, pos_y=1, weight=5, x_from=20)
comutate_pc(factory_pcs[:5], router_index=3, pos_y=1, weight=5, x_from=30)
comutate_pc(factory_pcs[5:], router_index=4, pos_y=1, weight=5, x_from=40)


# comutating servers to dc comutator
comutate_servers(auth_servers, comutator_index=4, pos_y=4, weight=5)
comutate_servers(mail_servers, comutator_index=4, pos_y=5,)
comutate_servers(file_servers, comutator_index=4, pos_y=6, x_from=2, weight=7)
comutate_servers(web_servers, comutator_index=4, pos_y=7, x_from=2, weight=5)
group_elements([local_comutators[4]], pos_y=4, x_from=4)
group_elements([local_comutators[5]], pos_y=4, x_from=40)


# comutating routers to comutators of office
comutate_objects(net_routers[:1],local_comutators[0], 5)
comutate_objects(net_routers[1:3],local_comutators[0], 9)

comutate_objects(net_routers[:1],local_comutators[1], 4)
comutate_objects(net_routers[1:3],local_comutators[1], 2)

group_elements([local_comutators[0]], pos_y=3, x_from=10)
group_elements([local_comutators[1]], pos_y=3, x_from=15)

# comutating routers to comutators of fabric
comutate_objects(net_routers[3:3],local_comutators[2], 5)
comutate_objects(net_routers[3:],local_comutators[2], 4)

comutate_objects(net_routers[3:3],local_comutators[3], 4)
comutate_objects(net_routers[3:],local_comutators[3], 1)

group_elements([local_comutators[2]], pos_y=3, x_from=30)
group_elements([local_comutators[3]], pos_y=3, x_from=40)


# comutate office and factory  with dc comutators 
comutate_objects(local_comutators, dc_comutators[0], 3)
group_elements([dc_comutators[0]], pos_y=6, x_from=10)

comutate_objects(local_comutators, dc_comutators[1], 1)
group_elements([dc_comutators[1]], pos_y=6, x_from=23)

comutate_objects(local_comutators, dc_comutators[2], 2)
group_elements([dc_comutators[2]], pos_y=6, x_from=40)

# comutate dc comutator to inet comutator
comutate_objects(dc_comutators[:1], inet_comutator[0], 1)
comutate_objects(dc_comutators[1:2], inet_comutator[0], 9)
comutate_objects(dc_comutators[2:], inet_comutator[0], 3)
if __name__ == "__main__":
    links = G.number_of_edges()
    nodes =  G.number_of_nodes()
    nx.draw_networkx(G, pos=positions, node_color=color_map, with_labels=True, node_size=500)
    plt.title(f"Corporate network, links {links}, nodes {nodes}")
    plt.show()


