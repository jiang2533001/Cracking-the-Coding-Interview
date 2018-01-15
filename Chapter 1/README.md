# Solution
### 1.1 Is Unique

__Solution 1:__ Use hash table to store each character and then check identical character exist in this hash table, since the time complexity is  `O(n)`

__Solution 2:__ Use a array of boolean value for all characters. If a character appear, then the index of character (also the ASCII) will store the true value. So to use this array to check string. The time complexity is also `O(n)`



### 1.2 Check Permutation:

__Solution:__Use hash table to store the count of each character, thus the character is the key and value is the count. Then to use this hash table to check another string, and to decrease the count if the string has the same character. If the value is negative, which means there are extra character in this string. The time complexity is `O(n)`

  