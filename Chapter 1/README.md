# Solution
### 1.1 Is Unique

__Solution 1:__ Use hash table to store each character and then check identical character exist in this hash table, since the time complexity is is `O(n)`

__Solution 2:__ Use a array of boolean value for all characters. If a character appear, then the index of character (also the ASCII) will store the true value. So to use this array to check string.