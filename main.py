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

f3 = open("compare.txt", "w")

for file in list:
    res, time, j, n_edges = e.exh_search("graph/"+file)
    res2, time2, j2, number_of_tries = r.rand_search("graph/"+file)
    temp[file] = (res, time, j, n_edges)
    temp_random[file] = (res2, time2, j2, number_of_tries)
    
index_temp = sorted(temp.items())
index_temp_random = sorted(temp_random.items())

for item in index_temp:
    print(item[0])
    f2.write(f"{item[0]} : Maximum Matching {item[1][0]}  in {item[1][1]} seconds; Number of operations: {item[1][2]}, Number of edges: {item[1][3]}\n")

for item in index_temp_random:
    f.write(f"{item[0]} : Maximum Matching {item[1][0]}  in {item[1][1]} seconds; Number of operations: {item[1][2]}; Number of tested solutions: {item[1][3]}\n")

for i in range(len(index_temp)):
    format_float = "{:.2f}".format(index_temp_random[i][1][0]/index_temp[i][1][0])
    f3.write(f"{index_temp[i][0]} : Maximum matching accuracy "+format_float+f"; Time difference: {abs(index_temp[i][1][1]-index_temp_random[i][1][1])}\n" )
