# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1359 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(-1)
        tmp = p
        a,b = l1,l2
        while a and b:
            if min(a.val,b.val)==a.val:
                tmp.next = a
                tmp = tmp.next
                a = a.next
            else:
                tmp.next = b
                tmp = tmp.next
                b = b.next
        if a:
            tmp.next = a
        else:
            tmp.next = b

        return p.next
# leetcode submit region end(Prohibit modification and deletion)
