#!/usr/bin/env python3
# #coding=utf-8

class BinaryNode:
    def __init__(self, data):
        self.data = data

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

class BinaryTree:

    def __init__(self,lt,max_node_num):
        self.list = lt
        self.max_node_num = max_node_num
        # if the valid node pos == max_node_num, it means the tree is full
        self.valid_node_pos = 0
        head_node = BinaryNode('HEAD')
        self.list.append(head_node)

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

            # create the left subtree recursively
            self.PreordCreateBiTree(new_node, 'true', 'false')
            # create the right subtree recursively
            self.PreordCreateBiTree(new_node, 'false', 'true')

    # Thread the binary tree with pre order method
    def PreordThreadBitree(self, prenode, cur_pos):
        list_len = len(self.list) - 1
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


    # create the binary tree with mid order method
    def MidordCreateBiTree(self):
        pass
    # create the binary tree with post order method
    def PostordCreateBiTree(self):
        pass
    # Traverse the binary tree with the pre order method
    def PreordTraverse(self):
        head_node = self.list[0]
        cur_pos = head_node.lpos
        cur_node = self.list[cur_pos]
        while cur_pos != -1:
            print(cur_node.data)
            if cur_node.lpos == 'thread':
                cur_pos = cur_node.lpos
                cur_node = self.list[cur_pos]
                print(cur_node.data)

    # Traverse the binary tree with the mid order method
    def MidordTraverse(self):
        pass
    # Traverse the binary tree with the post order method
    def PostordTraverse(self):
        pass

    def PrintBiTree(self):
        for node in self.list:
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
    BiTree1.PreordThreadBitree(None,0)
    BiTree1.PrintBiTree()
