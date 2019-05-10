#!/usr/bin/env python3
# #coding=utf-8

# The python file will implement some algorithms about the graph according to the book
# 大话数据结构, please refer to the book chapter 7


#############################################################################################
#################################图的邻接矩阵表示法 ###########################################
class Vertex:
    def __init__(self, data, index):
        self.data = data
        self.index_pos = index

# 图:邻接矩阵表示法
class Matrix_Graph:
    # when we initialize a Matrix_Graph, we should give the vertex number and edge number
    def __init__(self):
        self.vertex_num = 0
        self.edge_num = 0
        # the wight of the edge cannot exceed the INFINITY
        self.INFINITY = 65535
        # the graph has a Vertex list
        self.vertex_list = []
        # the graph has a edge list, it is two dimension matrix
        self.edge_list = []
        # if the vertex is traversed, the value of the pos should be set to 1
        self.visited_list = []
        # the queue used in breadth-first-search
        self.queue_list = []
        # used in Kruskal algorithm to keep the sorted edges
        self.sorted_edges_list = []

    # get the index based on the data
    def GetVertexIndex(self,data):
        j = 0
        for j in self.vertex_list:
            if j.data == data:
                break
        return j.index_pos
    # 建立无向图方法
    def CreateMGraph(self):
        a_input = input("Please input the vertex number and edge number:\n")
        self.vertex_num, self.edge_num = eval(a_input)
        # init the vertex list
        self.vertex_list = []
        # init the edge list
        self.edge_list = [[self.INFINITY for y in range(self.vertex_num)] for x in range(self.vertex_num)]

        for i in range(self.vertex_num):
            input_data = input("Please input the vertex's data\n")
            vertex_data = Vertex(input_data, i)
            self.vertex_list.append(vertex_data)
            self.visited_list.append(0)

        for i in range(self.edge_num):
            a, b, weight = eval(input("Please input the edge's vertex pos and weight value\n"))
            i = self.GetVertexIndex(a)
            j = self.GetVertexIndex(b)
            self.edge_list[i][j] = self.edge_list[j][i] = weight

    # print the Matrix Graph
    def PrintMGraph(self):
        print("The Graph vertex values are :")
        for i in self.vertex_list:
            print(i.data)
        print("\n")
        print("The Graph edge matrix are:")
        for row in range(self.vertex_num):
            print("{} ".format(self.edge_list[row]))

    # Depth_First_Search for Matrix_Graph
    # DFS is to traverse all the adjacent vertexes of the vertex i
    def DFS(self,i):
        # mark the vertex has been traversed
        self.visited_list[i] = 1
        # print the data of the vertex, meaning the vertex is traversed.
        print("{} ".format(self.vertex_list[i].data))
        for j in range(self.vertex_num):
            # less than INFINITY means the j is adjacent to i
            if self.edge_list[i][j] < self.INFINITY and  self.visited_list[j] == 0:
                self.DFS(j)

    def TraverseMGraph_by_DFS(self):
        print("Begin to traverse the matrix graph by depth first search algorithm")
        for i in range(self.vertex_num):
            self.visited_list[i] = 0
        for i in range(self.vertex_num):
            if self.visited_list[i] == 0:
                self.DFS(i)

    # Breadth_First_Search for Matrix_Graph
    def TraverseMGraph_by_BFS(self):
        print("Begin to traverse the matrix graph by breadth first search algorithm")
        for i in range(self.vertex_num):
            self.visited_list[i] = 0

        for i in range(self.vertex_num):
            if self.visited_list[i] == 0:
                self.visited_list[i] = 1
                # access the vertex
                print(self.vertex_list[i].data)
                # make the vertex into the tail of the queue
                self.queue_list.append(self.vertex_list[i])
                # if the queue is not empty
                while len(self.queue_list) > 0:
                    #make the vertex out of the queue from header
                    pop_vertex = self.queue_list.pop(0)
                    m = self.GetVertexIndex(pop_vertex.data)

                    for j in range(self.vertex_num):
                        # less than INFINITY means the j is adjacent to i
                        # if j is adjacent to m and j is not visited
                        if self.edge_list[m][j] < self.INFINITY and  self.visited_list[j] == 0:
                            self.visited_list[j] = 1
                            # access the vertex j
                            print(self.vertex_list[j].data)
                            self.queue_list.append(self.vertex_list[j])

    # Minimum Spinning Tree by Prim algorithm
    # the minimum spinning tree is consisted of a set of the arcs
    def mini_spin_tree_by_prim(self):
        print("Find the mininum spinning tree by Prim algorithm")
        min = i = j = k = 0
        adjvex_list = []
        lowcost_list = []
        # lowcost[0] = 0 means the first arc in the spinning tree is found, one of its vertex's index pos is 0
        lowcost_list.append(0)
        # adjvex[0] = 0 means the
        adjvex_list.append(0)

        # lowcost[] now is the edges of vertex 0, noted i starts from 1
        for i in range(1,self.vertex_num):
            lowcost_list.append(self.edge_list[0][i])
            adjvex_list.append(0)

        for i in range(1, self.vertex_num):
            min = self.INFINITY
            j = 1
            k = 0
            while j < self.vertex_num:
                if lowcost_list[j] !=0 and lowcost_list[j] < min:
                    min = lowcost_list[j]
                    k = j
                j = j+1
            # print one edge
            print("{},{}".format(adjvex_list[k],k))
            lowcost_list[k] = 0
            for j in range(1, self.vertex_num):
                if lowcost_list[j] != 0 and self.edge_list[k][j] <lowcost_list[j]:
                    lowcost_list[j] = self.edge_list[k][j]
                    adjvex_list[j] = k

    # Minimum Spinning Tree by Kruskal algorithm
    def mini_spin_tree_by_kruskal(self):
        print("Find the mininum spinning tree by Kruskal algorithm")
        parent_list = []
        for m in range(self.vertex_num):
            # parent_list[n] = m means the root of vertex n is m in the subtree
            # "-1" means there is no root now, or you can think the vertex n is the root of itself
            parent_list.append(-1)
        for j in range(self.edge_num):
            tuple_edge = self.sorted_edges_list[j]
            # 寻找头顶点所在当前子树的root
            m = self.kruskal_find_parent(parent_list, tuple_edge[0])
            # 寻找尾顶点所在当前子树的root
            n = self.kruskal_find_parent(parent_list, tuple_edge[1])
            # 如果root不一样,说明这条边的两个顶点在不同的子树,可以合并
            # 如果两个顶点在同一个子树, 那么这条边的加入加会构成环,不能形成生成树
            if m != n:
                # union the subtree
                # 合并子树,这里是让尾顶点所在子树成为头顶点所在子树的root
                parent_list[m] = n
                # 合并子树, 让头顶点所在子树成为尾顶点所在子树的root也是可以的
                #parent_list[n] = m
                print("({},{}) {}".format(tuple_edge[0],tuple_edge[1],tuple_edge[2]))

    # Generate the kruskal edge list, each items is tuple(begin, end, weight) and sorted by
    # weight from small to big
    def kruskal_generate_edges(self):
        # we should sort the edge by wight, so first loop should be edge_num times
        for j in range(self.edge_num):
            min = self.INFINITY
            for m in range(self.vertex_num):
                for n in range(self.vertex_num):
                    if self.edge_list[m][n] < min and self.edge_list[m][n] > 0:
                        min = self.edge_list[m][n]
                        min_start = m
                        min_end = n
            tuple_edge = min_start,min_end,min
            self.sorted_edges_list.append(tuple_edge)
            # we have found the edge with the minimum weight, so we should not consider this edge and the
            # mirror edge next time
            self.edge_list[min_start][min_end] = self.INFINITY
            self.edge_list[min_end][min_start] = self.INFINITY

    # find the parent vertex
    def kruskal_find_parent(self, parent, f):
        while parent[f] != -1 :
            f = parent[f]
        return f


##############################################################################################
##############################################################################################


##############################################################################################
#####################################图的邻接表表示法#########################################

# vertex structure
class ADL_Vertex:
    def __init__(self,data):
        self.data = data
        # vertex should keep a list to trace its edges
        self.edge_list = []

# edge structure
class ADL_Edge:
    def __init__(self,vertex_pos,edge_weight):
        # The second vertex position of this edge
        self.vertex_pos = vertex_pos
        # The weight value of this edge
        self.edge_weight = edge_weight

class ADL_Graph:
    def __init__(self):
        self.vertex_num = 0
        self.edge_num = 0
        # the graph's vertexes list
        self.vertex_list = []

    def CreateADLGraph(self):
        input_text = input("Please input the vertex number and the edge number:\n")
        self.vertex_num,self.edge_num = eval(input_text)
        for i in range(self.vertex_num):
            input_data = input("Please input the vertex's data\n")
            adl_vertex = ADL_Vertex(input_data)
            self.vertex_list.append(adl_vertex)
        for i in range(self.edge_num):
            input_text = input("Please input the edge's start vertex position and end vertex position and weight:\n")
            start,end,weight = eval(input_text)
            if start >= 0 and start <self.vertex_num and end >= 0 and end < self.vertex_num:
                # 一条边对应有两个边表结构
                adl_edge = ADL_Edge(end,weight)
                self.vertex_list[start].edge_list.insert(0,adl_edge)
                adl_edge = ADL_Edge(start,weight)
                self.vertex_list[end].edge_list.insert(0,adl_edge)


    def PrintADLGraph(self):
        print("The Graph vertex values are :")
        for i in self.vertex_list:
            print(i.data)
        print("The Graph edge structures are:")
        for i in self.vertex_list:
            if len(i.edge_list) > 0:
                print("The vertex pos {} has the edge:".format(i.data))
                for j in i.edge_list:
                    print("The edge's end vertex position is {}, the edge's weight is {}".format(j.vertex_pos, j.edge_weight))

##############################################################################################
#####################################有向图十字链表表示法######################################
class Orth_Graph:
    def __init__(self):
        self.vertex_num = 0
        self.arc_num = 0
        # the graph's vertexes list
        self.vertex_list = []
        # the graph's arc list
        self.arc_list = []

    class Orth_Vertex:
        def __init__(self, data):
            self.data = data
            # the index of the arc to this vertex
            self.firstin_arc_index = -1
            # the index of the arc from this vertex
            self.firstout_arc_index = -1

    class Orth_Arc:
        def __init__(self, head, tail, weight):
            # the index of the vertex that is the head of the arc
            self.head = head
            # the index of the vertex that is the tail of the arc
            self.tail = tail
            # the weight value of the arc
            self.weight = weight
            # the index of the next arc that has the same head with the arc
            self.headlink_index = -1
            # the index of the next arc that has the same tail with the arc
            self.taillink_index = -1

    def CreateOrthGraph(self):
        input_text = input("Please input the vertex number and the arc number:\n")
        self.vertex_num, self.arc_num = eval(input_text)
        for i in range(self.vertex_num):
            input_data = input("Please input the vertex's data\n")
            orth_vertex = self.Orth_Vertex(input_data)
            self.vertex_list.append(orth_vertex)
        for i in range(self.arc_num):
            input_data = input("Please input the arc's start vertex, end vertex and the weight\n")
            start,end,weight = eval(input_data)
            # generate the arc instance
            orth_arc = self.Orth_Arc(start, end, weight)
            # add the arc instance to the graph's arc list
            self.arc_list.append(orth_arc)
            # keep the arc index
            current_arc_index = len(self.arc_list) - 1

            # the vertex's first out link is empty
            if self.vertex_list[start].firstout_arc_index == -1:
                self.vertex_list[start].firstout_arc_index = current_arc_index
            else:
                # go through to the end of list
                next_out_arc_index = self.vertex_list[start].firstout_arc_index
                while self.arc_list[next_out_arc_index].headlink_index != -1:
                    next_out_arc_index = self.arc_list[next_out_arc_index].headlink_index
                self.arc_list[next_out_arc_index].headlink_index = current_arc_index

            # the vertex's first in link is empty
            if self.vertex_list[end].firstin_arc_index == -1:
                self.vertex_list[end].firstin_arc_index = current_arc_index
            else:
                # go through to the end of list
                next_in_arc_index = self.vertex_list[end].firstin_arc_index
                while self.arc_list[next_in_arc_index].taillink_index != -1:
                    next_in_arc_index = self.arc_list[next_in_arc_index].taillink_index
                self.arc_list[next_in_arc_index].taillink_index = current_arc_index

    def PrintOrthGraph(self):
        print("The Orth Graph's vertex values are:")
        for i in self.vertex_list:
            print("The vertex data is {}, the vertex firstin_arc_index is {}, the vertex firstout_arc_index is {} ".format(i.data, i.firstin_arc_index, i.firstout_arc_index))
        print("The Orth Graph's arc are:")
        for j in self.arc_list:
            print("The arc from {} to {}, the headlink index is {}, the tailink _index is {}".format(j.head, j.tail, j.headlink_index, j.taillink_index))

        for i in self.vertex_list:
            print("The vertex {} out arcs are:".format(i.data))
            out_arc_index = i.firstout_arc_index
            while out_arc_index != -1:
                out_arc = self.arc_list[out_arc_index]
                print("The arc from {} to {}, the weight is {}".format(out_arc.head, out_arc.tail,out_arc.weight))
                out_arc_index = out_arc.headlink_index
            print("The vertex {} in arcs are:".format(i.data))
            in_arc_index = i.firstin_arc_index
            while in_arc_index != -1:
                in_arc = self.arc_list[in_arc_index]
                print("The arc from {} to {}, the weigh is {}".format(in_arc.head, in_arc.tail, in_arc.weight))
                in_arc_index = in_arc.taillink_index


##############################################################################################

if __name__ == '__main__':
    ######################
    #图的邻接矩阵测试代码###
    '''
    MG = Matrix_Graph()
    MG.CreateMGraph()
    MG.PrintMGraph()
    MG.TraverseMGraph_by_DFS()
    MG.TraverseMGraph_by_BFS()
    '''
    ######################
    #图的邻接表表示法测试代码
    '''
    ADL_G = ADL_Graph()
    ADL_G.CreateADLGraph()
    ADL_G.PrintADLGraph()
    '''
    ######################
    #图的十字链表表表示法测试代码
    '''
    Orth_G = Orth_Graph()
    Orth_G.CreateOrthGraph()
    Orth_G.PrintOrthGraph()
    '''
    ######################

    ######################
    #最小生成树的测试代码
    MG = Matrix_Graph()
    MG.vertex_num = 9
    MG.edge_num = 15
    MG.vertex_list = [Vertex(j,j) for j in range(8)]
    MG.edge_list = [[0,10,65535,65535,65535,11,65535,65535,65535], \
                    [10,0,18,65535,65535,65535,16,65535,12], \
                    [65535,18,0,22,65535,65535,65535,65535,8], \
                    [65535,65535,22,0,20,65535,24,16,21], \
                    [65535,65535,65535,20,0,26,65535,7,65535], \
                    [11,65535,65535,65535,26,0,17,65535,65535], \
                    [65535,16,65535,24,65535,17,0,19,65535], \
                    [65535,65535,65535,16,7,65535,19,0,65535], \
                    [65535,12,8,21,65535,65535,65535,65535,0]]
    MG.PrintMGraph()
    MG.mini_spin_tree_by_prim()
    MG.kruskal_generate_edges()
    for _ in MG.sorted_edges_list:
        print("Start {} End {} Weight {}".format(_[0], _[1], _[2]))
    MG.mini_spin_tree_by_kruskal()
    ######################