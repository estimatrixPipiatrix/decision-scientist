class node:
    def __init__(self,data_val):
        self.data_val = data_val
        self.next = None
        self.prev = None

class list_head:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,index,data_val):
        n = node(data_val)
        if index==0:
            if self.head == None:
                self.tail = n
            n.next = self.head
            self.head = n
            n.prev = None
        else:
            current = self.head
            cur_ind = 0
            while (current.next != None and \
                   cur_ind != index-1):
                current = current.next
                cur_ind += 1
            if cur_ind != index-1:
                print('no node at previous index')
            else:
                n.next = current.next
                n.prev = current
                if current.next != None:
                    current.next.prev = n
                current.next = n
                if n.next == None:
                    self.tail = n

    def delete(self,index):
        if index == 0:
            if self.head.next == None:
                self.tail = None
            else:
                self.head.next.prev = None
            self.head = self.head.next
        else:
            current = self.head
            cur_ind = 0
            while (cur_ind != index-1) and \
                  (current.next != None):
                current = current.next
                cur_ind += 1
            if current.next == None:
                print('nothing to delete!')
                return
            if current.next.next != None:
                current.next.next.prev = current
                current.next = current.next.next

    def insert_tail(self,data_val):
        n = node(data_val)
        n.next = None
        n.prev = self.tail
        if self.tail != None:
            self.tail.next = n
            self.tail = n

    def delete_tail(self):
        if self.tail == None:
            print('nothing to delete!')
            return
        if self.tail.prev != None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.tail = None
            self.head = None

    def print(self,index,which_end='head'):
        if which_end == 'head':
            current = self.head
            cur_ind = 0
            while (cur_ind != index) and \
                  (current.next != None):
                current = current.next
                cur_ind += 1
            if (cur_ind != index):
                print('nothing to print!')
            else:
                print(current.data_val)
        elif which_end == 'tail':
            current = self.tail
            cur_ind = 0
            while (cur_ind != index) and \
                  (current.prev != None):
                current = current.prev
                cur_ind += 1
            if (cur_ind != index):
                print('nothing to print!')
            else:
                print(current.data_val)
        else:
            print('invalid first argument')

    def search(self,data_val,which_end='head'):
        if which_end=='head':
            current = self.head
            cur_ind = 0
            while (current != None):
                if current.data_val==data_val:
                    return cur_ind
                current = current.next
                cur_ind += 1
            print('value not found')
        elif which_end=='tail':
            current = self.tail
            cur_ind = 0
            while (current != None):
                if current.data_val==data_val:
                    return cur_ind
                current = current.prev
                cur_ind += 1
            print('value not found')
        else:
            print('invalid first argument')

    def print_list(self,which_end='head'):
        if which_end=='head':
            current = lh.head
            if current == None:
                print('nothing to print!')
                return
            while current.next != None:
                print(current.data_val)
                current = current.next
            print(current.data_val)
        elif which_end=='tail':
            current = lh.tail
            if current == None:
                print('nothing to print!')
                return
            while current.prev != None:
                print(current.data_val)
                current = current.prev
            print(current.data_val)
        else:
            print('invalid argument')

lh = list_head()
lh.insert(0,'Mon')
lh.insert(1,'Wed')
lh.insert(1,'Tue')
lh.insert(3,'Thu')
