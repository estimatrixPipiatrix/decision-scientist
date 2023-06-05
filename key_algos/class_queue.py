class node:
    def __init__(self,data_val):
        self.data_val = data_val
        self.next = None
        self.prev = None

class queue:
    def __init__(self):
        self.last  = None
        self.first = None

    def enqueue(self,data_val):
        tmp = self.last
        n = node(data_val)
        if self.last != None:
            self.last.prev = n
        if self.first==None:
            self.first = n
        self.last = n
        n.next = tmp

    def dequeue(self):
        value = self.first.data_val
        if self.last==self.first:
            self.first = None
            self.last  = None
        else:
            self.first.prev.next = None
            self.first = self.first.prev
        return value

    def print(self):
        if self.last==None:
            print('queue is empty')
        else:
            line = [self.last.data_val]
            current = self.last.next
            while current != None:
                line.append(current.data_val)
                current = current.next
            line.reverse()
            print(line)

# example
#q = queue()
#q.enqueue('early guy')
#q.enqueue('normal guy')
#q.enqueue('late guy')
#q.enqueue('super late guy')
#q.print()
#print(q.dequeue())
#q.print()
