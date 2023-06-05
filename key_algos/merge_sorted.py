# merge two sorted linked lists by splicing them together into
# a linked list that is itself sorted
import sys

#example input:
#List 1: 1 -> 2 -> 4
#List 2: 1 -> 3 -> 4
#output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

from linked_list import list_head,node
list_1 = list_head()
list_2 = list_head()
list_1.append_head(4)
list_1.append_head(2)
list_1.append_head(1)
list_2.append_head(5)
list_2.append_head(4)
list_2.append_head(3)
list_2.append_head(1)

def merge_lists(list_1,list_2):
    merged = list_head()
    dummy = node('null')
    merged.head = dummy
    current1 = list_1.head
    current2 = list_2.head
    while (current1 != None) and (current2 != None):
        val1 = current1.data_val
        val2 = current2.data_val
        if (val1<=val2):
            dummy.next = current1
            current1 = current1.next
        else:
            dummy.next = current2
            current2 = current2.next
        dummy = dummy.next

    if current1 != None:
        dummy.next = current1
    elif current2 != None:
        dummy.next = current2

    return merged.head.next

merged = merge_lists(list_1,list_2)
current_node =  merged
while current_node != None:
    print(current_node.data_val)
    current_node = current_node.next
