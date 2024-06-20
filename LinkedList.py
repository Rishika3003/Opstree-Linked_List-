# Write a program that can perform sorting and search operations on numbers represented as linked lists. The program should support the following operations:

# Take numbers as input
# Program should store numbers as LinkedList
# The program should print the numbers by traversing the linked lists.
# Can perform below operations without using python built in sort function
# Sorting: Sort the numbers represented by linked lists in ascending and descending order.
# Search: Search for a specific number in the list of numbers represented by linked lists.
# Print the output of the sorting operation as a list of linked lists.
# Print the result of the search operation, indicate that the number is present or not.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert(self, a):
        new_node = Node(a)
        new_node.next = self.head
        self.head = new_node
      
    def swap(self, ptr1, ptr2):
        ptr1.data, ptr2.data = ptr2.data, ptr1.data
        
    def sorting(self, ascending=True):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            while cur.next:
                if (ascending and cur.data > cur.next.data) or (not ascending and cur.data < cur.next.data):
                    self.swap(cur, cur.next)
                    swapped = True
                cur = cur.next
                
    def search(self, a):
        cur = self.head
        while cur is not None:
            if cur.data == a:
                return True
            cur = cur.next
        return False    
        
    def printL(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


if __name__=="__main__":
    numbers = [10, 20, 60, 50, 5]
    
    llist = LinkedList()
    for number in numbers:
        llist.insert(number)
    
    print("Original List:")
    llist.printL()

    search_number = 20
    if llist.search(search_number):
        print(f'{search_number}:= Present')
    else:
        print(f'{search_number}:= Not Present')

    llist.sorting(ascending=True)
    print("Sorted Linked List in Ascending Order:")
    llist.printL()
    llist.sorting(ascending=False)
    print("Sorted List in Descending Order:")
    llist.printL()


    
    
    
    
