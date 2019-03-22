# bibliometric_networks
Bibliometric Networks

Things tried:

pyvis.network -- took a long time to render, with slow manipulation. pros: only a couple lines of code to make the networkx functionally interactive

networkx -- took several minutes to render, very little options for manipulation. pros: easy to build network

igraph -- not intuitive for even building a network. 

Other struggles:
When running the script in a notebook, jordan had trouble getting the datashader module to import. tried switching versions of python and creating custom environments with specific versions of different packages. figured out colab bypasses those issues. enabling anyone to run it regardless of versions and environments. 

the only thing needed to make the network print in-line in colab is the following line of code:

