# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.new_linked_list = None
        self.curNode = None
        self.carry = 0

    def carryIncrement(self, result) -> int:
        while result >= 10:
            result = result - 10
            self.carry = self.carry + 1
        return result

    def addNums(self, num1: int, num2: int) -> int:
        result = num1 + num2 + self.carry
        self.carry = 0
        return self.carryIncrement(result)

    def setUpNewNode(self, result: int):
        newNode = ListNode(result, None)
        if self.new_linked_list is None:
            self.new_linked_list = newNode
            self.curNode = self.new_linked_list
        else:
            self.curNode.next = newNode
            self.curNode = self.curNode.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        assert l1 is not None
        assert l2 is not None

        while l1 is not None or l2 is not None:
            #   add corr. nums together, factoring in carry (if none count as 0)
            if l1 is None:
                result = self.addNums(0, l2.val)
                self.setUpNewNode(result)
                l2 = l2.next
            elif l2 is None:
                result = self.addNums(l1.val, 0)
                self.setUpNewNode(result)
                l1 = l1.next
            else:
                result = self.addNums(l1.val, l2.val)
                self.setUpNewNode(result)
                l1 = l1.next
                l2 = l2.next

        if self.carry != 0:
            self.setUpNewNode(self.carry)
            self.carry = 0

        return self.new_linked_list


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    print(s.addTwoNumbers(l1, l2))




