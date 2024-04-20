import heapq

import asyncio

import notIf
import networkx as nx

class RoadAxisManager:

    def __init__(self,G):
        self.roadAxisQueue = []
        self.nodes_st_lists = {}
        self.roadGraph=G
    def init_from_graph(self):
        G=self.roadGeaph
        nodes=G.nodes()
        edges=G.edges()
        #details_for_node={}
        for node in G.nodes:
            node_name = G.nodes[node]
            #details_for_node[node_name]={'num_of_axis':0}
        source_node=notIf.find_source_nodes(G)
        graphs_axis=notIf.create_subgraphs_with_two_nodes(G)
        for last_node_name, graph in graphs_axis.items():
            father=list(graph.nodes())[-1]
            print(father)
            #father=nodes[father]
            print(father)
            father_graph=nx.ego_graph(G, father)
            sons = list(G.successors(father))
            checks=[]
        while sons:
            for son in sons:
                grandchildrens = list(G.successors(son))
                check_graph = father_graph.copy()
                check_graph.remove_node(son)
                checks.append((check_graph,father,son,grandchildrens))
            father_graph = nx.ego_graph(G, son)
            sons = list(G.successors(son))
        connect_son_to_father_axis, new_axis=notIf.check_fatherNode_to_grandchildren(checks)
        #לחבר את הנתונים לכל הצירים
        for new in new_axis:
            new_graph=nx.DiGraph()
            new_graph.add_nodes(new[0],new[1])
            new_graph.add_edge(edges[new[0]],edges[new[1]])
            graphs_axis[new[0]]=new_graph
        for connection in connect_son_to_father_axis:
            graphs_axis[connection[0]].add_node(connection[1])
            graphs_axis[connection[0]].add_edge(edges[connection[0]][connection[1]])
        return graphs_axis
    def build_queue_axis(self,graphs_axis):
        for graph,i in graphs_axis.values():
            axis_name="axis"+i
            axis_priority=0
            #לבנות תור עדיפויות של צירים

            for node in graph:
                node.axis=axis_name
                axis_priority=axis_priority+node.priority
            heapq.heappush(self.roadAxisQueue, (axis_priority, axis_name))
            heapq.heapify(self.roadAxisQueue)

            #######################

            self.add_axis_to_queue(axis_name)
    def add_axis_to_queue(self, axis_name):
        heapq.heappush(self.roadAxisQueue, (0, axis_name))

    def update_path_for_node(self, node, paths):
        self.nodes_st_lists[node] = paths

    def update_path_for_axis(self, axis_name, node, updated_path):
        for axis, paths in self.nodes_st_lists.items():
            if axis.startswith(axis_name):
                for i, (path, weight) in enumerate(paths):
                    if path == node:
                        self.nodes_st_lists[axis][i] = (node, updated_path)

    def change_priority_by_axis_name(self, axis_name,value):
        for priority, name in self.roadAxisQueue:
            if name == axis_name:
                priority=priority+value
    def update_priority_axis(self,node):
        self.change_priority_by_axis_name(node.axis,node.priority)
        heapq.heapify(self.roadAxisQueue)

    def green_wave(self,id_node_path):
        id_node=id_node_path[:6]
        id_path=id_node_path[6:]
        #פה צריך למצוא את הציר לפי הצומת והנתיב
        for neighbor in graph_axis[node]:
            time.sleep(weight)
            neighbor.priority=neighbor.priority+10
            #לעדכן את הציר
            node=neighbor








    #לבנות תור עדיפויות של צירים
#לעשות פעולה שמעדכנת את התור שמקהלת שם של צומת ובודקת לאיזה ציר היא שייכת

g_try=nx.DiGraph()
nodes=[1,2,3,4,5,6,7,8,9]
edges=[(1,2),(2,3),(1,4),(4,7),(2,5),(5,8),(3,6),(6,9),(4,5),(5,6),(7,8),(8,9)]
g_try.add_nodes_from(nodes)
g_try.add_edges_from(edges)
try_axis=RoadAxisManager(g_try)
print(try_axis.init_from_graph())
#father_graph = nx.ego_graph(g_try, '1')

#print(father_graph)
