# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
            
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
            
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # self.head, self.tail = self.tail, self.head
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
    def find_middle_node(self):
        temp = self.head
        second = self.head
        while second is not None and second.next is not None:
            temp = temp.next
            second = second.next.next
        return temp
 
 
def find_kth_from_end(self, value):
     slow = self.head
     fast = self.head
     for _ in range(value):
         if fast is None:
             return None
         else:
             fast = fast.next
     while (fast is not None):
        slow = slow.next
        fast = fast.next
     return slow

            
 
# my_linked_list = LinkedList(4)

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)

# my_linked_list = LinkedList()
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()
# print()
# my_linked_list.reverse()
# my_linked_list.print_list()

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4
                                                                                                                 