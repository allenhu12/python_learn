class stackobject:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class stack:
    def __init__(self, max):
        self.header = stackobject(1, 'header')
        self.tailer = stackobject(1, 'tailer')
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.count = 0
        self.max_num = max
    def push(self, data):
        # push a new object into a stack
        # insert it at the header
        if self.count == self.max_num:
            print("Stack is full")
        else:
            object = stackobject(1,data)
            object.next = self.header.next
            self.header.next.prev = object
            self.header.next = object
            object.prev = self.header
            self.count = self.count+1
    def pop(self):
        if self.count == 0:
            print("Stack is empty")
        else:
            return_value = self.header.next.data
            self.header.next.next.prev = self.header
            self.header.next = self.header.next.next
            self.count = self.count-1
            return return_value
    def __repr__(self):
        vals = []
        num = 0
        p = self.header.next
        while p != self.tailer:
            vals.append(str(p.data))
            p = p.next
            num = num + 1
        return '->'.join(vals)
    def empty(self):
        while self.count > 0:
            self.pop()
    def get_pop_data(self):
        if self.count == 0:
            return None
        else:
            return self.header.next.data

def if_priority_higher(oper1, oper2):
    if oper1 in '*/' and oper2 in '+-':
        return True
    else:
        return False

def calc(a, b, op):
    if op is '+':
        return a+b
    elif op is '-':
        return a-b
    elif op is '*':
        return a*b
    elif op is '/':
        return a/b

def basic_calculator(express):
    sk_number = stack(8)
    sk_operator = stack(8)
    for c in express:
        if c in '0123456789':
            # if it is a number, always push it
            number = eval(c)
            sk_number.push(number)
        if c in '+-*/':
            if sk_operator.count == 0:
                sk_operator.push(c)
            else:
                top_oper = sk_operator.get_pop_data()
                if if_priority_higher(c, top_oper) is True:
                    #if c priority is higher than the stack top, push c
                    sk_operator.push(c)
                else:
                    while sk_operator.count > 0 and sk_number.count > 1:
                        a = sk_number.pop()
                        b = sk_number.pop()
                        oper = sk_operator.pop()
                        result = calc(b,a,oper)
                        sk_number.push(result)
                    sk_operator.push(c)
        if c is '\n':
            while sk_operator.count > 0 and sk_number.count > 1:
                a = sk_number.pop()
                b = sk_number.pop()
                oper = sk_operator.pop()
                result = calc(b,a,oper)
                sk_number.push(result)
            if sk_number.count == 1:
                last_value = sk_number.pop()
                return last_value

def detect_marks_match(express):
    sk_marks = stack(20)
    for c in express:
        if c in '[{(':
            sk_marks.push(c)
        elif c in ']})':
            top_mark = sk_marks.pop()
            if c is ']' and top_mark is '[':
                continue
            elif c is ')' and top_mark is '(':
                continue
            elif c is '}' and top_mark is '{':
                continue
            else:
                return False
    if sk_marks.count == 0:
        return True
    else:
        return False


def simulate_browers():
    sk_backward = stack(20)
    sk_forward = stack(20)
    def simulate_access(page):
        print("access:{0}".format(page))
    def simulate_backward():
        print("hit backward")
        if sk_backward.count>0:
            page = sk_backward.pop()
            sk_forward.push(page)
            access_page = sk_backward.get_pop_data()
            if access_page is not None:
                simulate_access(access_page)
            else:
                print("no more page!!")
        else:
            print("no more page!!")
    def simulate_forward():
        print("hit forward")
        if sk_forward.count>0:
            page = sk_forward.pop()
            simulate_access(page)
            sk_backward.push(page)
        else:
            print("no more page!!")
    def simulate_new_page(page):
        print("access new page:{0}".format(page))
        sk_backward.push(page)
        sk_forward.empty()
    simulate_new_page('a')
    simulate_new_page('b')
    simulate_new_page('c')
    simulate_backward()
    simulate_backward()
    simulate_forward()
    simulate_new_page('d')
    simulate_backward()
    simulate_forward()
    simulate_forward()

if __name__ == '__main__':
    '''
    sk = stack(8)
    sk.push('a')
    sk.push('b')
    print(sk)
    sk.pop()
    print(sk.get_pop_data())
    print(sk)
    sk.pop()
    print(sk)
    print(sk.get_pop_data())
    '''
    c = basic_calculator('5-8+4*4-9/3\n')
    print(c)
    c = detect_marks_match('[()}([])]')
    print(c)
    simulate_browers()
