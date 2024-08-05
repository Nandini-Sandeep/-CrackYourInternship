class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialising variables
        dummy = ListNode()
        node = dummy
        pvs = None
        while list1 or list2:
            if not list1:
                node.next = list2
                break
            if not list2:
                node.next = list1
                break
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        return dummy.next
