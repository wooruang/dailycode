package solution

import scala.annotation.tailrec


class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def isPalindrome(head: ListNode): Boolean = {
    var current = head
    var cnt = count(head)
    for (idx <- 0 to (cnt / 2).toInt) {
      var rValue = getReverseValue(head, cnt - idx - 1)
      if (rValue != current.x) return false
      current = current.next
    }
    return true
  }

  @tailrec
  def getReverseValue(head: ListNode, index: Int, curIndex: Int = 0): Int =
    if (head == null) return -1
    else if (curIndex == index) return head.x
    else return getReverseValue(head.next, index, curIndex + 1)


  @tailrec
  def count(head: ListNode, start: Int = 0): Int =
    if (head != null) return count(head.next, start + 1)
    else return start

  def main(args: Array[String]): Unit = {
    println("Hello")

    var test1 = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))))
    println(isPalindrome(test1))
    var test2 = new ListNode(1, new ListNode(2))
    println(isPalindrome(test2))
    var test3 = new ListNode(1, new ListNode(2, new ListNode(1)))
    println(isPalindrome(test3))
  }
}