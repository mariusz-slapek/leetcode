# Not good solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ls_iterator = 0
        l1_sum = 0 
        l2_sum = 0
        
        while l1 != None:
            l1_sum = l1_sum + l1.val * 10**ls_iterator 
            l1 = l1.next
            ls_iterator = ls_iterator + 1 
        ls_iterator = 0
        while l2 != None:
            l2_sum = l2_sum + l2.val * 10**ls_iterator 
            l2 = l2.next
            ls_iterator = ls_iterator + 1
            
        sum_ls = l1_sum + l2_sum

        output = ListNode()
        save = output
        for i in range(len(str(sum_ls))):
            output.val = int(str(sum_ls)[-1 - i])
            if(i != len(str(sum_ls)) -1):
                output.next = ListNode()
                output = output.next
        
        
        return save

# Better solution

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        output = ListNode(0)
        save = output
        carry = 0
        
        
        while l1 or l2 or carry:
            v_l1 = l1.val if l1 else 0
            v_l2 = l2.val if l2 else 0
            
            carry, val = divmod(v_l1 + v_l2 + carry, 10)
            
            output.next = ListNode(val) 
            output = output.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        
        return save.next
