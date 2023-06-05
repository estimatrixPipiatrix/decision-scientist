class node:
    def __init__(self,data_val):
        self.data_val = data_val
        self.next = None

class list_head:
    def __init__(self):
        self.head = None

    def append_tail(self,data_val):
        n = node(data_val)
        if self.head == None:
            self.head = n
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = n

    def append_head(self,data_val):
        n = node(data_val)
        if self.head == None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def remove_head(self):
        self.head = self.head.next

    def print_list(self):
        head = self.head
        print(head.data_val)
        current_node = head.next
        while current_node is not None:
            print(current_node.data_val)
            current_node = current_node.next

    def middle_val(self):
        head = self.head
        fast_pointer = head
        slow_pointer = head
        count = 1
        while fast_pointer.next is not None:
            fast_pointer = fast_pointer.next
            count += 1
            if (count%2==0):
                slow_pointer = slow_pointer.next
        print(count)
        print(slow_pointer.data_val)

my_list = list_head()
my_list.append_tail('Mon')
my_list.append_tail('Tue')
my_list.append_tail('Wed')
my_list.append_tail('Thu')
my_list.append_tail('Fri')
