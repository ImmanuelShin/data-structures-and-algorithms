from code_challenges.linked_list.linked_list import Linked_List as LinkedList

def zip_lists(list1, list2):
    if not list2.head:
        return list1
    if not list1.head:
        return list2
    
    list = LinkedList()
    head = list1.head
    node1 = head.next
    node2 = list2.head
    prev = head
    while node1 and node2:
        prev.next = node2
        node2 = node2.next
        prev.next.next = node1
        node1 = node1.next
        prev = prev.next.next
    prev.next = node1 or node2
    list.head = head
    return list
