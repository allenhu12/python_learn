class linkobject:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None


#
# 用链表实现一个队列FIFO cache
# 最先加入队列的元素将最先被淘汰
#
class fifolinklist:
    def __init__(self, capacity):
        # maximum number of the element
        self.capacity = capacity
        # element_dict is used to keep all the elements of the FIFO
        self.element_dict = {}
        # 2 guards elements
        self.header = None
        self.tailer = None
        self.element_len = 0
    def get(self,key):
        for k,v in self.element_dict.items():
            if key == k:
                return v
        return None
    def put(self, key, value):
        found = 0
        for k,v in self.element_dict.items():
            if key == k:
                self.element_dict[key].data = value
                found = 1
        if found == 0:
            if self.element_len > self.capacity:
                pass
            else:
                #在队列头添加
                new = linkobject(key, value)
                if self.header == None:
                    # no elements yet
                    self.header = self.tailer = new
                else:
                    first = self.header
                    last = self.tailer
                    new.next = first
                    new.prev = last
                    first.prev = new
                    last.next = new
                    self.header = new
                self.element_len = self.element_len + 1

    def __repr__(self):
        vals = []
        num = 0
        p = self.header
        while p.next and num < self.element_len:
            vals.append(str(p.data))
            p = p.next
            num = num + 1
        return '->'.join(vals)


if __name__ == '__main__':
    fifo = fifolinklist(5)
    fifo.put(1,1)
    fifo.put(2,2)
    print(fifo)