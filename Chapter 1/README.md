# Solution
### 1.1 Is Unique

__Solution 1:__ Use hash table to store each character and then check identical character exist in this hash table, since the time complexity is  `O(n)`.

__Solution 2:__ Use a array of boolean value for all characters. If a character appear, then the index of character (also the ASCII) will store the true value. So to use this array to check string. The time complexity is also `O(n)`.

### 1.2 Check Permutation:

__Solution:__ Use hash table to store the count of each character, thus the character is the key and value is the count. Then to use this hash table to check another string, and to decrease the count if the string has the same character. If the value is negative, which means there are extra character in this string. The time complexity is `O(n)`.

### 1.3 URLify:

__Solution:__ Use for loop to scan the whole string and stop when the index character is equal to certain size. In this process, copy original chacater to a new string and copy '%20' to replace space character. The time complexity is `O(n)`.

### 1.4 Palinderome Permutation:

__Solution:__ Use hash table to store how many times each character appears, and then check the number of odd counts. If there are two or more odd counts, which means this string cannot be a palinderome. The time complexity is `O(n)`. 

### 1.5 One Away:

__Solution:__ Check the length of each string and choose the longer length as size of a for loop firstly. To go through these two strings and compare each character, if these two characters are different at the same index, to compare remaining characters. The time complexity is `O(n)`.
### 1.6 String Compression:

__Solution:__ Scan the whole string, and store a current character in a independent variable because it will be used to compare next character. To increase the count until the a charcter is not equal the 'current character', which means it is a new character, so we have to restart count. Focus on string concatenation situation in this problem. The time complexity is `O(n)` 
 
