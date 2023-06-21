
# creating nodes
class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# creating the linked_list
class linked_list:
    def __init__(self):
        self.head = None

    def traverse(self):  # traversing the whole list
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->>", end=" ")
                n = n.ref

    def add_begin(self, data):  # adding new node to the beginning of the linked list
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_last(self, data):  # adding new_node to the end of the list
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def after_node(self, data, x):  # adding nodes after the nodes
        n= self.head
        while n is not None:
                if n.data == x:
                    break
                n = n.ref
        if n is None:
            print("node is not present in a ll")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def before_node(self, data, x):  # adding nodes before nodeaa
        if self.head  == None:
            print("linked list is empty")
            return
        if self.head.data == x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n is None:
                print(" Items not present in the ll")
            else:
                new_node = node(data)
                new_node.ref = n.ref
                n.ref = new_node

l1 = linked_list()
l1.add_last(10)
l1.add_last(20)
l1.add_begin("sajan")
l1.before_node(500, 10)
l1.traverse()


# deleteing  the node t beginning
class node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linked_list:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def traverse(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def delete_first(self):
        if self.head is None:
            print("The list is empty")
        else:
            self.head = self.head.ref

    def delete_last(self):
        if self.head is None:
            print("The list is empty")
        elif self.head.ref is None:
            self.head = None

        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("The linked list is empty")
        elif self.head.data == x:
            self.head == self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("No item in the ll")

            else:
                n.ref = n.ref.ref


ll = linked_list()
ll.add_begin(23)
ll.add_begin(27)
ll.add_begin(40)
ll.add_begin(50)
# ll.delete_first()
# ll.delete_last()
ll.delete_by_value(100)
ll.traverse()


