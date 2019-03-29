# Bibliographic Networks: A Python Tutorial
**By Hannah VanWingen and Jordan Earnest**

Networks can provide significant measures to identify data driven patterns and dependencies. Though, given a data file it can be difficult to discern how one may approach creating such a network. In this tutorial, we will use a bibliographic data file downloaded from a query search in [Scopus](https://https://www.scopus.com/search/form.uri) to walk through the process of cleaning the data file, writing a python script to parse the data into nodes and edges, computing graphical measures using [NetworkX](https://https://networkx.github.io/documentation/stable/index.html), and creating an interactive network display using [HoloViews](https://http://holoviews.org). 

We tried out multiple Python libraries for ease of use and efficiency before landing on this combination. Building a network was more intuitive in NetworkX than [iGraph](https://igraph.org/redirect.html). However, it took several minutes to render our large graph and a interaction was sticky. [Pyvis](https://pyvis.readthedocs.io/en/latest/#) was easy to build a network with and can be expanded to incorporate more advanced NetworkX functionality with only a couply lines of code. However it still took a long time to render, with slow manipulation.  
Holoviews, which runs on top of the native Python visualization library Bokeh, enables NetworkX to render quickly, with versitile manipulation. The graphs are produced in HTML and JavaScript, making it easy to render in webpages.

When

- link to put things on a webpage. 
graphic without the support of a visualization library. 

Other struggles:
When running the script in a notebook, jordan had trouble getting the datashader module to import. tried switching versions of python and creating custom environments with specific versions of different packages. figured out colab bypasses those issues. enabling anyone to run it regardless of versions and environments. 

the only thing needed to make the network print in-line in colab is the following line of code:
import os
os.environ['HV_DOC_HTML'] = 'true'
and you have to tell it not to "reset run times" after each time. 
