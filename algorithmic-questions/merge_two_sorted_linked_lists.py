from utils.models import LinkedListNode


def merge_two_sorted_lists(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
    temp_head = tail = LinkedListNode(data=0)

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return temp_head.next  # skip the first data node (0)


if __name__ == '__main__':
    list1 = LinkedListNode(2, next=LinkedListNode(5, next=LinkedListNode(7)))
    list2 = LinkedListNode(3, next=LinkedListNode(11))

    merged_list = merge_two_sorted_lists(list1, list2)
