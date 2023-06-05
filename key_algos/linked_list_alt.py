class node:
    def __init__(self,data_val):
        self.data_val = data_val
        self.next = None

class list_head:
    def __init__(self):
        self.head = None

    def insert(self,index,data_val):
        n = node(data_val)
        if index == 0:
            n.next = self.head
            self.head = n
        else:
            current = self.head
            cur_ind = 0
            while (cur_ind != index-1):
                current = current.next
                cur_ind += 1
            n.next = current.next
            current.next = n

    def read(self,index):
        if index == 0:
            return self.head.data_val
        else:
            current = self.head
            cur_ind = 0
            while (cur_ind != index):
                current = current.next
                cur_ind += 1
            return current.data_val

    def delete(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            cur_ind = 0
            while (cur_ind != index-1):
                current = current.next
                cur_ind += 1
            current.next = current.next.next

    def search(self,data_val):
        current = self.head
        if current.data_val == data_val:
            return 0
        else:
            cur_ind = 0
            while (current.next != None):
                current = current.next
                cur_ind += 1
                if current.data_val == data_val:
                    return cur_ind
            print ('value not found')

    def print_list(self):
        current = self.head
        while (current != None):
            print(current.data_val)
            current = current.next

    def reverse_list(self):
        if self.head == None:
            print('no elements to reverse!')
            return
        current = self.head
        prev_node = None
        next_node = current.next
        while current != None:
            current.next = prev_node
            prev_node = current
            current = next_node
            if current != None:
                next_node = current.next
            else:
                self.head = prev_node

    def print_last(self):
        current = self.head
        if current == None:
            print('nothing to print!')
            return
        while current.next != None:
            current = current.next
        print(current.data_val)

lh = list_head()
lh.insert(0,'Mon')
lh.insert(1,'Tue')
lh.insert(2,'Wed')
lh.insert(3,'Thu')
lh.print_list()
