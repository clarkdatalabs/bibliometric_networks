import csv
import networkx as nx

G = nx.Graph()

with open('SCOPUS_complexsystems_economics.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    # each row contains information for a source
    elist = []
    for row in reader:
        # add an edge for each source and its references
        for ref in row['References']:
            print(ref)
