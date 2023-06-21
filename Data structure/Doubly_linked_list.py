# Doubly linke list practice

class node:  # creating new nodes
    def __init__(self, data) -> None:
        self.pref = None
        self.data = data
        self.nref = None


class Doubly_linked_list:  # creating dobly linked list
    def __init__(self):
        self.head = None

    def forward_traverse(self):  # forward traversing
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def backward_traverse(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref

            while n is not None:
                print(n.data)
                n = n.pref

    def add_begin(self, data):  # adding nodes to the beginnnig of th LL
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def after_node(self, data, x):  # to add the node after the node
        if self.head is None:
            print("The Linked list is empty")

        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Items  in linked list is not present")
            else:
                new_node = node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("The list is empty")

        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Given items doesnt present in th DLL")
            else:
                new_node = node(data)
                if n.pref is None:
                    new_node.nref = self.head
                    self.head.pref = new_node
                    self.head = new_node
                else:
                    new_node.nref = n
                    new_node.pref = n.pref
                    n.pref.nref = new_node
                    n.pref = new_node

    def delete_begin(self):  # deleteing the node from the beginning of dll
        if self.head is None:
            print("The Dll is empty")
        else:
            if self.head.nref is None:
                self.head = None
                print("The ddl is empty now ")
            else:
                self.head = self.head.nref
                self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("The list is empty")
        else:
            if self.head.nref is None:
                self.head = None
                print("The list is empty now")
            else:
                n = self.head
                while n.nref is not None:
                    n = n.nref
                n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:  # checking for empty list
            print("Hey, The list is empty")
            return
        if self.head.nref is None:  # checking for single node in dll
            if self.head.data == x:
                self.head = None
            else:
                print("Given value is not present in DLL")
            return

        if self.head.data == x:  # deleting the first  node
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None: # loop runs if multiple nodes are presenta
            if n.data == x:
                break
            n = n.nref
        if n.nref is not None:  # deletes the middle node  of the list
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x: # deletes te last Node
                n.pref.nref = None
            else: # prints message if given value is not present in the list
                print("The given item is not present")


dll = Doubly_linked_list()
dll.add_begin(12)
dll.add_begin(13)
dll.add_begin(14)
# dll.add_begin(15)
# dll.add_last(100)
# dll.add_last(200)
# dll.after_node(70, 100)
# dll.after_node(80, 200)
# dll.add_before(70, 1000)
# dll.delete_begin()
# dll.delete_end()
dll.delete_by_value(18)
dll.forward_traverse()

