
from re import I

import time
class ExhaustiveSearch:

    def __init__(self):
        self.nvertices = None
        self.nedges = None
        self.edges_and_vertices = []
        pass

    def exh_search(self, infile):
        start = time.time()
        f = open(infile, "r")
        n_line = 0
        num_total_vertices = None
        vert_list = []
        for line in f:
            
            len_line = len(line) + 1

            if n_line == 0: #operaçoes a fezer na primeira passagem
                num_total_vertices = int( len_line/2)
                vert_list = [0 for i in range(num_total_vertices)]

            vertice1 = None
            vertice2 = None
            i = 0
            for char in line:
                if char == '1':
                    if vertice1 == None:
                        vertice1 = i
                        vert_list[int(i/2)] = vert_list[int(i/2)]+1
                    else:
                        vertice2 = i 
                        vert_list[int(i/2)] = vert_list[int(i/2)]+1
                elif char == '2':
                    vertice1 = i 
                    vertice2 = i 
                    vert_list[int(i/2)] = vert_list[int(i/2)]+1
                    break
                i = i + 1
            tuple_base = (n_line, int(vertice1 / 2), int(vertice2 / 2))
            self.edges_and_vertices.append(tuple_base)
            n_line = n_line + 1
        
        max_matching, end, j = self.max_matching(self.edges_and_vertices, num_total_vertices)
        self.edges_and_vertices.clear()
        return max_matching, end-start, j, num_total_vertices
        # edges_and_vertices vai conter tuplos (arestas, vértice1, vertice2)


    def special_graph_search(self, file):
        start = time.time()
        f = open(file, "r")
        n_line = 0
        for line in f:
            
            if n_line == 0 or n_line == 1:
                n_line+=1
                continue
            elif n_line == 2:
                self.nvertices = int(line)
                n_line+=1
            elif n_line == 3:
                self.nedges = int(line)
                n_line +=1
            else:
                vert1, vert2 = line.split(" ")
                n_line+=1
                self.edges_and_vertices.append((n_line-3, int(vert1), int(vert2)))
        max_matching, end, j = self.max_matching(self.edges_and_vertices, self.nvertices)
        self.edges_and_vertices.clear()
        return max_matching, end-start, j, self.nvertices
        pass

    def max_matching(self, edges_and_vertices, num_total_vertices):
        max_matching = 0
        j = 0
        for i in range(num_total_vertices):
            temp = 0
            j += 1
            for edge in edges_and_vertices:
               
                j += 1
                if i != edge[1] and i != edge[2]:
                    temp += 1
            if temp > max_matching:
                max_matching = temp
        return max_matching, time.time(), j
        pass

   