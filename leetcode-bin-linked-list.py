from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def getDecimalValue(self, head: Optional[ListNode]) -> int:
    n = head
    bv = 0
    while n != None:
      bv = bv * 2 + n.val
      n = n.next
    return bv