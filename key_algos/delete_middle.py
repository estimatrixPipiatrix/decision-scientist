# give only the middle node in a linked list, write a code that
# will effectively delete that node from the list
from linked_list_alt import list_head

lh = list_head()
lh.insert(0,'Mon')
lh.insert(1,'Tue')
lh.insert(2,'Wed')
lh.insert(3,'Thu')
lh.insert(4,'Fri')
lh.print_list()

node = lh.head.next.next
# the following code only has access to the 'Wed' node defined 
# in the line above

while node.next != None:
    node.data_val = node.next.data_val
    node.next_data_val = None
    prev_node = node
    node = node.next
prev_node.next = None
