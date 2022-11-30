import random
import time

class RandomSearch:

    def __init__(self, ):
        pass

    def rand_search(self, infile):
        start = time.time()
        print(infile)
        edges_and_vertices = []
        f = open(infile, "r")
        n_line = 0
        num_total_vertices = None
        vert_list = []
        lone_vertice_flag = False
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
            edges_and_vertices.append(tuple_base)
            n_line = n_line + 1
        for elem in vert_list:
            if elem == 0:  
                lone_vertice_flag = True
          
        if lone_vertice_flag:
            end = time.time()
            return n_line, end-start, 1
        
        max_matching, end, j = self.monte_carlo(edges_and_vertices, num_total_vertices, lone_vertice_flag)
        return max_matching, end-start, j
        # edges_and_vertices vai conter tuplos (arestas, vértice1, vertice2)

    def monte_carlo(self, edges_and_vertices, num_total_vertices, lone_vertice_flag):
        if lone_vertice_flag:
            return 
        
        number_of_tries = round(.6 * num_total_vertices)
        number_of_tries = list(range(number_of_tries))
        print(num_total_vertices)
        print(number_of_tries)

        max_matching = 0
        j = 0

        for i in range(len(number_of_tries)):
            n = random.choice(number_of_tries)
            temp = 0
            j+=1
            for edge in edges_and_vertices:
                j+=1
                if n != edge[1] and n != edge[2]:
                    temp+=1
                if temp > max_matching:
                    max_matching = temp
            number_of_tries.remove(n)
        return max_matching, time.time(), j
        pass