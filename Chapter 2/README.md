# Chapter 2 Solution

### 2.1 Remove Dups

__Solution:__ Iterate through the entire linked list and use hash table to store the value of each node. If there exist the same key in hash table, which means this node is duplicate. The time complexity is `O(n)`

### 2.2 Return Kth to Last:

__Solution:__ Iterate through the entire linked list. If the current node is the Kth node, return it directly and print it as a head of rest of linked list. The time complexity is `O(n)`

### 2.3 Delete Middle Node:

__Solution:__ A meaningless problem

### 2.4 Partition:

__Solution:__ A confuse problem

### 2.5 Sum Lists:

__Solution:__ Iterate through these two linked lists at the same time, and sum of each node. If the sum is bigger than 10, just keep the last digit, and add 1 to the result of next calculation. The time complexity is `O(n)`

### 2.6 Palindrome:

__Solution:__ Iterate through the first half of the linked list and push each node in a stack. Then iterate through the last half of the linked list, and pop element from stack to compare with each node. If they are all the same, which means this is a palindrome. The time complexity is `O(n)`, and the space complexity is also `O(n)`.
