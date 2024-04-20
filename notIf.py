import networkx as nx
def A1(id):
    return id =="A1"
def C1(id):
    return id =="C1"
def A1OrC1(id):
    return id =="A1" or id =="C1"
def check():
    A1('ff') and func()
def func():
    print('ffffffff')
check()


def find_source_nodes(graph):
    source_nodes = [node for node in graph.nodes if graph.in_degree(node) == 0]
    return source_nodes
def create_subgraphs_with_two_nodes(graph):
    subgraphs = {}
    first_source = next(iter(graph.nodes), None)  # Get the first source node in the graph
    if first_source:
        successors = list(graph.successors(first_source))
        for child_node in successors:
            subgraph = graph.subgraph([first_source, child_node])
            last_node_name = list(subgraph.nodes)[-1]
            subgraphs[last_node_name] = subgraph
            return subgraphs
def check_fatherNode_to_grandchildren(checks):
    connect_son_to_father_axis=[]
    new_axis=[]
    for check in checks:
        G=check[0]
        father=check[1]
        son=check[2]
        grandchildren_list=check[3]
        for grandchild in grandchildren_list:
            if nx.has_path(G, father, grandchild):
                continue
            else:
                connect_son_to_father_axis.append((G, father, son))
        if grandchildren_list:
            new_axis.append((son,grandchild))
    return connect_son_to_father_axis,new_axis