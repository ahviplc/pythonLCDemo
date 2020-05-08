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
    listnode1 = ListNode(2)
    listnode1.next = ListNode(4)
    listnode1.next.next = ListNode(3)
    listnode2 = ListNode(5)
    listnode2.next = ListNode(6)
    listnode2.next.next = ListNode(4)
    temp = slt.addTwoNumbers(listnode1, listnode2)
    print(temp.val, temp.next.val, temp.next.next.val)  # 7 0 8
