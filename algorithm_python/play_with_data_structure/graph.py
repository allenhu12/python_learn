#!/usr/bin/env python3
# #coding=utf-8

# The python file will implement some algorithms about the graph according to the book
# 大话数据结构, please refer to the book chapter 7


#############################################################################################
#################################图的邻接矩阵表示法 ###########################################
class Vertex:
    def __init__(self, data):
        self.data = data

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

    # 建立无向图方法
    def CreateMGraph(self):
        a_input = input("Please input the vertex number and edge number:\n")
        self.vertex_num, self.edge_num = eval(a_input)
        # init the vertex list
        self.vertex_list = [ 0 for x in range(self.vertex_num)]
        # init the edge list
        self.edge_list = [[self.INFINITY for y in range(self.vertex_num)] for x in range(self.vertex_num)]

        for i in range(self.vertex_num):
            input_data = input("Please input the vertex's data\n")
            vertex_data = Vertex(input_data)
            self.vertex_list[i] = vertex_data.data

        for i in range(self.edge_num):
            edge_data = input("Please input the edge's vertex pos and weight value\n")
            i,j,weight = eval(edge_data)
            self.edge_list[i][j] = self.edge_list[j][i] = weight

    # print the Matrix Graph
    def PrintMGraph(self):
        print("The Graph vertex values are :")
        print(self.vertex_list)
        print("\n")
        print("The Graph edge matrix are:")
        for row in range(self.vertex_num):
            print("{} ".format(self.edge_list[row]))
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
    Orth_G = Orth_Graph()
    Orth_G.CreateOrthGraph()
    Orth_G.PrintOrthGraph()
