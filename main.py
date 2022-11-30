import math
import random
from os import listdir
from exhaustive_search import ExhaustiveSearch
from randomized_search import RandomSearch

from graph_generator import GraphGenerator


nvertices=[i for i in range(10,101)]

e = ExhaustiveSearch()
r = RandomSearch()

for n in nvertices:
    m= GraphGenerator(n)
    m.generate_graph("graph/")

list = listdir("graph/")
temp = {}
temp_random = {}

f = open("res_random.txt", "w")
f2 = open("res.txt", "w")

for file in list:
    res, time, j, n_edges = e.exh_search("graph/"+file)
    res2, time2, j2, = r.rand_search("graph/"+file)
    temp[file] = (res, time, j, n_edges)
    temp_random[file] = (res2, time2, j2)
    
index_temp = sorted(temp.items())
index_temp_random = sorted(temp_random.items())

for item in index_temp:
    print(item[0])
    f2.write(f"{item[0]} : Maximum Matching {item[1][0]}  in {item[1][1]} seconds; Number of operations: {item[1][2]}, Number of edges: {item[1][3]}\n")

for item in index_temp_random:
    f.write(f"{item[0]} : Maximum Matching {item[1][0]}  in {item[1][1]} seconds; Number of operations: {item[1][2]}\n")