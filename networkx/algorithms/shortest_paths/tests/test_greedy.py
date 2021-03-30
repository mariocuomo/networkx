import networkx as nx

def heuristic(x, target):
        d = {
        'AQ': 18,
        'AN': 31,
        'BA': 22,
        'BO': 47,
        'FI': 40,
        'GE': 58,
        'MI': 65,
        'NA': 0,
        'PG': 19,
        'PI': 44,
        'RM': 18,
        'TO': 71
        }
        return d[x]


graph = nx.Graph()
points = ['AQ', 'AN', 'BA', 'BO', 'FI', 'GE', 'MI', 'NA', 'PG', 'PI', 'RM', 'TO']
edges = [
        ('AQ', 'AN', 19), ('AQ', 'PG', 17), ('AQ', 'RM', 11), ('AN', 'BA', 46), 
        ('AN', 'BO', 21), ('AN', 'PG', 16),('BA','RM',45), ('BO','FI',10), 
        ('BO','MI',21), ('FI','GE',22), ('FI','PG',15), ('FI','PI',9), 
        ('FI','RM',28), ('GE', 'MI', 14), ('GE', 'PG', 16), ('MI', 'TO', 14), ('NA', 'RM', 22), 
        ('PG','RM',17), ('PI','RM',37)]

graph.add_nodes_from(points)
graph.add_weighted_edges_from(edges)

print(greedy_path(graph, 'MI', 'NA', heuristic, 'weight'))