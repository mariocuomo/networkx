import networkx as nx
import numpy as np


def greedy_path(G, source, target, heuristic=None, weight='weight'):
    if source not in G:
        msg = f"Source {source} is not in G"
        raise nx.NodeNotFound(msg)
    
    #path using greedy strategy
    path = []
    current_node=source

    while True:
        #if I arrived to the targer, return the path
        if current_node == target:
            path.append(current_node)
            return path

        #add the node to the path
        path.append(current_node)

        #take the list of neighbors ( G[current_node] ) and filter it by getting only those not already visited avoiding loops ( (filter(lambda x: x not in path, listOfNode)))
        listOfNode=list(G[current_node])
        listOfNode=list(filter(lambda x: x not in path, listOfNode))

        #if the list is empty then the path does not exist.
        #if it is not empty apply the heuristic function to all the elements to detect most attractive as current_node for the next iteration
        if len(listOfNode)==0:
            msg = f"Node {target} not reachable from {source}"
            raise nx.NetworkXNoPath(msg)
        index_of_min = np.argmin ((list(map(lambda x: heuristic(x, target), listOfNode))))
        current_node = listOfNode[index_of_min]




