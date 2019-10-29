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
                return v.data
        return None
    def put(self, key, value):
        found = 0
        for k,v in self.element_dict.items():
            if key == k:
                self.element_dict[key].data = value
                found = 1
        if found == 0:
            new = linkobject(key, value)
            first = self.header
            last = self.tailer
            # 超过了最大值，需要淘汰队尾元素
            if self.element_len == self.capacity:
                # remove the last element
                second_to_last = last.prev
                second_to_last.next = last.next
                self.tailer = second_to_last

                # add the new to the header
                new.next = first
                new.prev = last
                first.prev = new
                last.next = new
                self.header = new

                self.element_len = self.capacity
                self.element_dict.pop(last.key)
            else:
                #在队列头添加
                if self.header == None:
                    # no elements yet
                    self.header = self.tailer = new
                else:
                    new.next = first
                    new.prev = last
                    first.prev = new
                    last.next = new
                    self.header = new
                self.element_len = self.element_len + 1
        self.element_dict[key] = new
    def __repr__(self):
        vals = []
        num = 0
        p = self.header
        while p.next and num < self.element_len:
            vals.append(str(p.data))
            p = p.next
            num = num + 1
        return '->'.join(vals)

#
# 用链表实现一个LRU cache
# 最近使用的元素最晚被淘汰
#

class LRUcache:
    def __init__(self, capacity):
        # maximum number of the element
        self.capacity = capacity
        # element_dict is used to keep all the elements of the FIFO
        self.element_dict = {}
        # 2 guards elements
        self.header = None
        self.tailer = None
        self.element_len = 0
    def get(self, key):
        if key in self.element_dict:
            # has the key, we should put the element on the header and then return the value
            cur = self.element_dict[key]
            if cur == self.header:
                return cur.data
            prev = cur.prev
            prev.next = cur.next
            next = cur.next
            next.prev = cur.prev

            first  = self.header
            self.header = cur
            cur.next = first
            first.prev = cur
            cur.prev = self.tailer
            if cur == self.tailer:
                self.tailer = prev
            return cur.data
        else:
            return None
    def put(self, key, value):
        found = 0
        for k,v in self.element_dict.items():
            if key == k:
                self.element_dict[key].data = value
                found = 1
        if found == 0:
            new = linkobject(key, value)
            first = self.header
            last = self.tailer
            # 超过了最大值，需要淘汰队尾元素
            if self.element_len == self.capacity:
                # remove the last element
                second_to_last = last.prev
                second_to_last.next = last.next
                self.tailer = second_to_last

                # add the new to the header
                new.next = first
                new.prev = last
                first.prev = new
                last.next = new
                self.header = new

                self.element_len = self.capacity
                self.element_dict.pop(last.key)
            else:
                #在队列头添加
                if self.header == None:
                    # no elements yet
                    self.header = self.tailer = new
                else:
                    new.next = first
                    new.prev = last
                    first.prev = new
                    last.next = new
                    self.header = new
                self.element_len = self.element_len + 1
        self.element_dict[key] = new
    def __repr__(self):
        vals = []
        num = 0
        p = self.header
        while p.next and num < self.element_len:
            vals.append(str(p.data))
            p = p.next
            num = num + 1
        return '->'.join(vals)

class single_link_object:
    def __init__(self, data):
        self.data = data
        self.next = None
class single_link_list:
    def __init__(self):
        self.num = 0
        self.header = None
        self.tailer = None
    def insert(self, new):
        if self.num == 0:
            self.header = new
            self.tailer = new
        else:
            self.tailer.next = new
            self.tailer = new
        self.num = self.num + 1

    def create_instance(self, max_num):
        for j in range(max_num):
            new = single_link_object(j)
            self.insert(new)

    def revert_instance(self):
        if self.header == self.tailer:
            return
        new_list_tailer = self.tailer
        new_list_header = self.tailer
        for j in range(self.num - 1):
            p = self.header
            while p != None and p.next != None:
                if p.next.next == None:
                    new_list_tailer.next = p
                    p.next = None
                    new_list_tailer = p
                p = p.next
        self.header = new_list_header
        return

    def revert_instance2(self):
        cur = self.header
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.header = self.tailer


    def __repr__(self):
        vals = []
        num = 0
        p = self.header
        while p :
            vals.append(str(p.data))
            p = p.next
            num = num + 1
        return '->'.join(vals)

if __name__ == '__main__':
    '''
    fifo = fifolinklist(5)
    fifo.put(1,1)
    fifo.put(2,2)
    fifo.put(3,3)
    fifo.put(4,4)
    fifo.put(5,5)
    fifo.put(6,6)
    fifo.put(7,7)
    print(fifo)
    print(len(fifo.element_dict))
    get_value = fifo.get(8)
    print(get_value)
    '''

    '''
    cache = LRUcache(5)
    cache.put(1,1)
    cache.put(2,2)
    cache.put(3,3)
    print(cache)
    get_value = cache.get(1)
    print(cache)

    revert_list = single_link_list()
    revert_list.create_instance(100)
    print(revert_list)
    revert_list.revert_instance2()
    print(revert_list)
    '''
