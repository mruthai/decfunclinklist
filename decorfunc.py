

"""Take in a list of numbers"""
new_list = [5, 20, 15, 10, 25]

# decorator that sort the created function above
def sort_my_list(*args):
    def wrapper(func):
        sort_lst = sorted(func)
        return sort_lst
    return wrapper

@sort_my_list
def add_list(one_list):
   return 

print(add_list(new_list))
###########################################################################
# LINKLIST LINKLIST LINKLIST LINKLIST LINKLIST LINKLIST LINKLIST LINKLIST #
###########################################################################
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert_before(self, value, target_value=None):
        new_node = Node(value)
        if not target_value:
            if self.head:
                new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            prev_node = None
            while current_node:
                if current_node.value == target_value:
                    prev_node.next_node = new_node
                    new_node.next_node = current_node
                    break
                prev_node = current_node
                current_node = current_node.next_node

    def remove(self, value):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.value == value:
                if not prev_node:
                    self.head = current_node.next_node
                else:
                    prev_node.next_node = current_node.next_node
                break
            prev_node = current_node
            current_node = current_node.next_node
        return False
    
    def insert_after(self, value, target_value=None):
        new_node = Node(value)
        if isinstance(value, list):
            for val in value:
                new_node = Node(val)
                if not target_value:
                    if self.head:
                        current_node = self.head
                        while current_node.next_node:
                            current_node = current_node.next_node
                        current_node.next_node = new_node
                    else:
                        self.head = new_node
        elif not target_value:
            if self.head:
                current_node = self.head
                while current_node.next_node:
                    current_node = current_node.next_node
                current_node.next_node = new_node
            else:
                self.head = new_node

        else:
            current_node = self.head
            while current_node:
                if current_node.value == target_value:
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node
                    break
                current_node = current_node.next_node
    
    def contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def print_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")

            current_node = current_node.next_node

        print('None')

my_list = LinkedList()
my_list.insert_after(add_list(new_list))
my_list.insert_before(12)
my_list.remove(5)
my_list.print_nodes()