import math
import random
from os import listdir
from exhaustive_search import ExhaustiveSearch
from randomized_search import RandomSearch

from graph_generator import GraphGenerator


nvertices=[i for i in range(10,301)]

nvertices.extend([400,500,600,700,800])

e = ExhaustiveSearch()
r = RandomSearch()

dir = "graph/"

for n in nvertices:
    m= GraphGenerator(n)
    m.generate_graph(dir)

list = sorted(listdir(dir))
temp = {}
temp_random = {}



f = open("res_random.txt", "w")
f2 = open("res.txt", "w")

f3 = open("compare.txt", "w")
f4 = open ("graphs_exh_tries.txt", "w")
f5 = open ("graphs_rand_tries.txt", "w")
f6 = open ("graphs_exh_time.txt", "w")
f7 = open ("graphs_rand_time.txt", "w")
f8 = open ("graphs_exh_OPnum.txt", "w")
f9 = open ("graphs_rand_OPnum.txt", "w")
f10 = open ("graphs_exh_res.txt", "w")
f11 = open ("graphs_rand_res.txt", "w")
for file in list:
    print(file)
    if file .__contains__("SW"):
        res, time, j, n_edges = e.special_graph_search(dir+file)
        res2, time2, j2, number_of_tries = r.special_graph_search(dir+file)
        temp[file] = (res, time, j, n_edges)
        temp_random[file] = (res2, time2, j2, number_of_tries)
    else:
        res, time, j, n_edges = e.exh_search(dir+file)
        res2, time2, j2, number_of_tries = r.rand_search(dir+file)
        temp[file] = (res, time, j, n_edges)
        temp_random[file] = (res2, time2, j2, number_of_tries)
        if file.__contains__("75"):
            f4.write(f"{n_edges},")
            f5.write(f"{number_of_tries},")
            f6.write(f"{time},")
            f7.write(f"{time2},")
            f8.write(f"{j},")
            f9.write(f"{j2},")
            f10.write(f"{res},")
            f11.write(f"{res2},")
  
        
index_temp = sorted(temp.items())
index_temp_random = sorted(temp_random.items())

for i in range(len(index_temp_random)):
    format_float = "{:.2f}".format(index_temp_random[i][1][0]/index_temp[i][1][0])
    f2.write(f"{index_temp[i][0]} : Maximum Matching {index_temp[i][1][0]}  in {index_temp[i][1][1]} seconds; Number of operations: {index_temp[i][1][2]}, Tested configurations: {index_temp[i][1][3]}\n")
    f.write(f"{index_temp_random[i][0]} : Maximum Matching {index_temp_random[i][1][0]}  in {index_temp_random[i][1][1]} seconds; Number of operations: {index_temp_random[i][1][2]}; Number of tested solutions: {index_temp_random[i][1][3]}\n")
    f3.write(f"{index_temp[i][0]} : Maximum matching accuracy "+format_float+f"; Time difference: {abs(index_temp[i][1][1]-index_temp_random[i][1][1])}\n" )
 