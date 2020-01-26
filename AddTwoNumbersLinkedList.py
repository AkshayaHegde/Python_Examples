# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode(None)
        final=l3
        carryOver=0
        while l1!=None or l2!=None:
            if (l1.val if l1!=None else 0) + (l2.val if l2!=None else 0) + carryOver>=10:
                value=(l1.val if l1!=None else 0) + (l2.val if l2!=None else 0 )+ carryOver-10
                carryOver=1
            else:
                value=(l1.val if l1!=None else 0) + (l2.val if l2!=None else 0 )+ carryOver
                carryOver=0
            if l3.val==None:
                l3.val=value
                l1=l1.next if l1!=None else l1
                l2=l2.next if l2!=None else l2
            else:
                l4=ListNode(None)
                l4.val=value
                l3.next=l4
                l3=l3.next
                l1=l1.next if l1!=None else l1
                l2=l2.next if l2!=None else l2
        if carryOver==1:
            l4=ListNode(None)
            l4.val=1
            l3.next=l4
        return final
            
        