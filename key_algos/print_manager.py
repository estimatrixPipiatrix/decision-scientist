from class_queue import queue

class print_manager():
    def __init__(self):
        self.queue = queue()

    def add_doc(self,document):
        self.queue.enqueue(document)

    def print_doc(self):
        document = self.queue.first.data_val
        print(document)
        self.queue.dequeue()

pm = print_manager()
doc1 = 'hello world!'
doc2 = 'hello again!'
doc3 = 'salvete omnes'
pm.add_doc(doc1)
pm.add_doc(doc2)
pm.add_doc(doc3)
pm.print_doc()
