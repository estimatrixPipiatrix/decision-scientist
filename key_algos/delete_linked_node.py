# given a linked list, return the head of the same linked list
# but with k-th node from the end of the linked list removed.
# for example, given the linked list 3 -> 2 -> 5 -> 1 -> 4 and
# k = 3, remove the 5 node and, thus, return the linked list
# 3 -> 2 -> 1 -> 4

class linked_list:
    def __init__(self):
        self.head = None

class node:
    def __init__(self,value):
        self.value = value
        self.next = None

linked_lst = linked_list()
node1 = node(3)
node2 = node(2)
node3 = node(5)
node4 = node(1)
node5 = node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
linked_lst.head = node1

k = 3
def remove_node(k,linked_lst):
    count = 1
    curr = linked_lst.head
    while count < (k-1):
        curr = curr.next
        count += 1
    curr.next = curr.next.next
    return linked_lst

lst = remove_node(k,linked_lst)
