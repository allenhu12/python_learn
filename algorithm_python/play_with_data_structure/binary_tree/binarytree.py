#!/usr/bin/env python3
# #coding=utf-8

class BinaryNode:

    def __init__(self, data):
        self.data = data
        # indicate the position (list index) of the current node
        self.pos = 0
        # indicate the position of the left child or the position of the pre-node
        self.lpos = -1
        # indicate the position of the right child or the position of the post-node
        self.rpos = -1
        # indicate the attribute of the lpos, if it is 0, the lpos is the position of the left child \
        # if it is 1, the lpos is the position of the pre-node
        self.ltag = 'child'
        # indicate the attribute of the rpos, if it is 0, the rpos is the position of the right child \
        # if it is 1, the rpos is the position of the post-node
        self.rtag = 'child'
        # the parent node pos
        self.parent_node_pos = -1

class BinaryTree:

    def __init__(self,lt,max_node_num):
        self.list = lt
        self.max_node_num = max_node_num
        # if the valid node pos == max_node_num, it means the tree is full
        self.valid_node_pos = 0
        # head_node = BinaryNode('HEAD')
        # self.list.append(head_node)
        # the root_node is used to indicate the the pos of the root node, the method for the binary tree always
        # start from the root node. By default, we use pre order method to save the nodes in the list, so the position
        # of the root node is 0
        self.root_node_pos = 0
        # the pre_node is used in the traverse method to indicate the pre node
        self.pre_node_pos = -1

    # create the binary tree with pre order method
    def PreordCreateBiTree(self, prenode, left_flag, right_flag):
        ch = input()
        if ch == '#':
            # not get a position index from the list
            return
        else:
            # get a valid position index from the list
            pos = self.valid_node_pos
            new_node = BinaryNode(ch)
            print('new node {} is generated, the pos is {}'.format(ch, pos))
            new_node.pos = pos
            self.list.append(new_node)
            self.valid_node_pos += 1
            if self.valid_node_pos >= self.max_node_num:
                print("the BinaryTree is full, cannot insert a node, return")
            if prenode != None:
                if left_flag == 'true':
                    prenode.lpos = pos
                    prenode.ltag = 'child'
                    print("assign {} to {}'s left child".format(pos, prenode.data))
                elif right_flag == 'true':
                    prenode.rpos = pos
                    prenode.rtag = 'child'
                    print("assign {} to {}'s right child".format(pos, prenode.data))
                new_node.parent_node_pos = prenode.pos

            # create the left subtree recursively
            self.PreordCreateBiTree(new_node, 'true', 'false')
            # create the right subtree recursively
            self.PreordCreateBiTree(new_node, 'false', 'true')

    # Thread the binary tree with pre order method
    def PreordThreadBitree(self, prenode, cur_pos):
        list_len = len(self.list)
        if cur_pos < list_len:
            cur_node = self.list[cur_pos]
            if cur_node != None:
                if cur_node.lpos == -1:
                    cur_node.lpos = cur_pos - 1
                    cur_node.ltag ='thread'

                if prenode != None:
                    if prenode.rpos == -1:
                        prenode.rpos = cur_pos
                        prenode.rtag = 'thread'
                cur_pos += 1
                self.PreordThreadBitree(cur_node, cur_pos)

    # Traverse the binary tree with the pre order method
    def PreordTraverse(self, pos):
        cur_pos = pos
        if cur_pos != -1:
            cur_node = self.list[cur_pos]
            print(cur_node.data)
            if cur_node.ltag == 'child':
                cur_pos = cur_node.lpos
            else:
                cur_pos = cur_node.rpos
            self.PreordTraverse(cur_pos)

    def PreordTraverseByThread(self, cur_node_pos):
        while cur_node_pos != -1:
            # locate the first node
            cur_node = self.list[cur_node_pos]
            # last node
            if cur_node.rpos == -1:
                break
            print(cur_node.data)
            while cur_node.rtag == 'thread' and cur_node.rpos != -1:
                cur_node_pos = cur_node.rpos
                cur_node = self.list[cur_node_pos]
                print(cur_node.data)
            if cur_node.ltag == 'child':
                cur_node_pos = cur_node.lpos

        


    # create the binary tree with mid order method
    def MidordCreateBiTree(self):
        pass
    # create the binary tree with post order method
    def PostordCreateBiTree(self):
        pass


    # Traverse the binary tree with the mid order method
    def MidordThreadBitree(self, node):
        # MidordTraverse the left subtree
        if node.lpos >= 0 and node.ltag == 'child':
            left_child = self.list[node.lpos]
            self.MidordThreadBitree(left_child)
        # process the current node
        if node.lpos == -1:
            # current node has no left child
            node.lpos = self.pre_node_pos
            node.ltag = 'thread'
        if self.pre_node_pos != -1:
            pre_node = self.list[self.pre_node_pos]
        else:
            pre_node = None
        if pre_node != None and pre_node.rpos == -1:
            pre_node.rpos = node.pos
            pre_node.rtag = 'thread'

        # make the current node as the pre node
        self.pre_node_pos = node.pos

        # MidordTraverse the right subtree
        if node.rpos >= 0 and node.rtag == 'child':
            right_child = self.list[node.rpos]
            self.MidordThreadBitree(right_child)

    def MidOrdTraverse(self,pos):
        if pos != -1:
            cur_node = self.list[pos]
            if cur_node.ltag == 'child' and cur_node.lpos != -1:
                self.MidOrdTraverse(cur_node.lpos)
            print(cur_node.data)
            if cur_node.rtag == 'child' and cur_node.rpos != -1:
                self.MidOrdTraverse(cur_node.rpos)

    def MidOrdTraverseByThread(self, cur_node_pos):
        while cur_node_pos != -1:
            cur_node = self.list[cur_node_pos]

            # locate the first node
            while cur_node.ltag == 'child' and cur_node.lpos != -1:
                cur_node = self.list[cur_node.lpos]
            print(cur_node.data)
            while cur_node.rtag == 'thread' and cur_node.rpos != -1:
                cur_node_pos = cur_node.rpos
                cur_node = self.list[cur_node_pos]
                print(cur_node.data)
            cur_node_pos = cur_node.rpos

    def PostordThreadBiTree(self, node):
        # Postord thread the left subtree
        if node.lpos >= 0 and node.ltag == 'child':
            left_child = self.list[node.lpos]
            self.PostordThreadBiTree(left_child)

        # Postord thread the right subtree
        if node.rpos >= 0 and node.rtag == 'child':
            right_child = self.list[node.rpos]
            self.PostordThreadBiTree(right_child)

        # process the current node
        if node.lpos == -1:
            # current node has no left child
            node.lpos = self.pre_node_pos
            node.ltag = 'thread'
        if self.pre_node_pos != -1:
            pre_node = self.list[self.pre_node_pos]
        else:
            pre_node = None
        if pre_node != None and pre_node.rpos == -1:
            pre_node.rpos = node.pos
            pre_node.rtag = 'thread'

        # make the current node as the pre node
        self.pre_node_pos = node.pos

    # Traverse the binary tree by post order with recursive method
    def PostordTraverse(self, pos):
        if pos != -1:
            cur_node = self.list[pos]
            if cur_node.ltag == 'child' and cur_node.lpos != -1:
                self.PostordTraverse(cur_node.lpos)
            if cur_node.rtag == 'child' and cur_node.rpos != -1:
                self.PostordTraverse(cur_node.rpos)
            print(cur_node.data)

    # Traverse the binary tree  by post order with thread
    def PostordTraverseByThread(self, cur_node_pos):
        # pre node pos
        pre_node_pos = -1
        while cur_node_pos != -1:
            cur_node = self.list[cur_node_pos]
            # locate the first node
            while cur_node.ltag == 'child' and cur_node.lpos != -1:
                cur_node = self.list[cur_node.lpos]
                cur_node_pos = cur_node.pos
            while cur_node.rtag == 'thread' and cur_node.rpos != -1:
                print(cur_node.data)
                pre_node_pos = cur_node.pos
                cur_node = self.list[cur_node.rpos]
                cur_node_pos = cur_node.pos
            # if current node is root AND pre node pos == root node's right child, we should return
            # for post order traverse, the root node must be the last node to traverse
            # but we should should judge the the pre node pos to decide if we traverse to the last node or
            # we just pass the root node (we might pass the root node but we should not traverse)
            if cur_node_pos == 0 and (self.list[cur_node_pos].rpos == pre_node_pos or self.list[cur_node_pos].lpos == pre_node_pos):
                print(self.list[cur_node_pos].data)
                return
            while cur_node_pos != -1 and self.list[cur_node_pos].rpos == pre_node_pos:
                print(self.list[cur_node_pos].data)
                pre_node_pos = cur_node_pos
                cur_node_pos = self.list[cur_node_pos].parent_node_pos
            if cur_node_pos != -1 and self.list[cur_node_pos].rtag == 'child' and self.list[cur_node_pos].rpos != -1:
                cur_node_pos = self.list[cur_node_pos].rpos

    def PrintBiTree(self):
        for node in self.list:
            if node.parent_node_pos != -1:
                print('node {} parent node is {}'.format(node.data, self.list[node.parent_node_pos].data))
            if node.ltag == 'child' and node.lpos != -1:
                print('node {} left child is {}'.format(node.data, self.list[node.lpos].data))
            if node.ltag == 'thread' and node.lpos != -1:
                print('node {} left prenode is {}'.format(node.data, self.list[node.lpos].data))
            if node.rtag == 'child' and node.rpos != -1:
                print('node {} right child is {}'.format(node.data, self.list[node.rpos].data))
            if node.rtag == 'thread' and node.rpos != -1:
                print('node {} right postnode is {}'.format(node.data, self.list[node.rpos].data))



if __name__ == '__main__':
    lt = []
    BiTree1 = BinaryTree(lt, 10)
    BiTree1.PreordCreateBiTree(None, 'false', 'false')
    BiTree1.PrintBiTree()

    # Prefix order methods
    # ---------------------------------------------------------------------------------
    # print("\nbegin to thread the tree by prefix order\n")
    # Tree1.PreordThreadBitree(None,0)
    # Tree1.PrintBiTree()
    # int("traverse the tree with recursive method")
    # Tree1.PreordTraverse(0)
    # int("traverse the tree with thread")
    # Tree1.PreordTraverseByThread(BiTree1.root_node_pos)
    # ---------------------------------------------------------------------------------

    # Middle order methods
    # ---------------------------------------------------------------------------------
   #  print("After Mid order thread\n")
   #  BiTree1.MidordThreadBitree(BiTree1.list[BiTree1.root_node_pos])
   #  BiTree1.PrintBiTree()
   #  print("\n")
   #  print("Begin to traverse the tree by mid order\n")
   #  BiTree1.MidOrdTraverse(BiTree1.root_node_pos)
   #  print('\n')
   #  print("Begin to travese the tree by mid order with thread")
   #  BiTree1.MidOrdTraverseByThread(BiTree1.root_node_pos)
    # ---------------------------------------------------------------------------------

    # Post order methods
    #----------------------------------------------------------------------------------
    print("\n\nAfter Post order thread \n")
    BiTree1.PostordThreadBiTree(BiTree1.list[BiTree1.root_node_pos])
    BiTree1.PrintBiTree()
    print("\n")
    print("Begin to traverse the tree by post order\n")
    BiTree1.PostordTraverse(BiTree1.root_node_pos)
    print("\n")
    print("Begin to traverse the tree in post order by thread")
    BiTree1.PostordTraverseByThread(BiTree1.root_node_pos)

