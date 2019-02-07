import json
import pandas as pd 
from urllib.request import *
from pandas.io.json import json_normalize
import networkx as nx
import matplotlib.pyplot as plt
import csv


# links by book w/o commentary


DG = nx.DiGraph()
link_dict = {}

with open('links_by_book_without_commentary.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    
    next(reader)
    for i in reader:
#         print(i)
#         text_referenced = i[0]
#         referencer = i[1]
#         count = i[2]
        link_dict[i[0]] = ({'text': i[1]}, {'weight':i[2]})
        edgeData= {"weight": i[2]}
        DG.add_edge(i[1],i[0], weight=i[2])


layout = nx.spring_layout(DG)
nx.draw_spring(DG)
edgeDataLabels = {}
for a, b in DG.edges():
    print(DG.get_edge_data(a, b, {"weight":0})["weight"])
    edgeLabels[(a, b)] = str(DG.get_edge_data(a, b,["weight"]))
    # retrieve the edge data dictionary
    
nx.draw_networkx_edge_labels(DG,pos=layout, edge_labels=edgeLabels) # draw the edge labels
plt.show()
# show the plotting window



# #------ load in csv -----#

# with open("links_by_book_without_commentary.csv", mode ="r") as infile:
# 	reader = csv.reader(infile)
# 	# mydict = {(rows[1]:rows[0], "weight":rows[3]) for rows in reader}
# 	edge_lst = [(i[1], i[0], i[2])for i in reader]


# # (referencer, referenced_title, weight)

# print(edge_lst)
# # example
# # ['Niddah', 'Toratan shel Rishonim', '1']
# # ['Rashba on Chullin', 'Sanhedrin', '1']
# # ['Makkot', 'Tosefta Yevamot', '1']

# #the book referenced, the book referenced by, num references


# # instantiate directed graph instance
# # and then G.add_edge(a, b, weight = x)
# DG = nx.DiGraph()

# # can do different average degree or avg clustering coefficients

# # i took this out because it was adding some nodes twice
# # node_lst = [(i["id"], i["group"])  for i in nodes_data]

# # edge_lst = [(i["source"], i["target"], {"weight": i['value']})  for i in links_data]


# # G.add_nodes_from(node_lst)
# DG.add_edges_from(edge_lst)

# # http://holoviews.org/user_guide/Network_Graphs.html


# # elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]



# # G = nx.karate_club_graph()f
# # print("Node Degree")
# # for v in G:
# #     print('%s %s' % (v, G.degree(v)))

# # nx.draw_circular(G, with_labels=True)
# # plt.show()



# # https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/

# # networkx
# # https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python#reading-files-importing-data

# # G.add_nodes_from(nodes_data["id"])


# # https://www.clear.rice.edu/comp200/resources/howto/networkx.shtml#graph_node_edge

# # https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html#adding-attributes-to-graphs-nodes-and-edges
