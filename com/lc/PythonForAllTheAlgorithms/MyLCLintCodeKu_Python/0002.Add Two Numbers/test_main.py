from Solution import Solution


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这个使用from Solution import Solution引入
# main方法
if __name__ == '__main__':
    slt = Solution()
    lostnode1 = ListNode(243)
    lostnode2 = ListNode(564)
    temp = slt.addTwoNumbers(lostnode1, lostnode2)
    print(temp.val, temp.next.val, temp.next.next.val)
