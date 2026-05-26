'''
problem: Reverse a String
Description:

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''
from collections import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # take two pointers start and end , opposite pointers and swap them
        start=0
        end=len(s)-1

        while(start<end):
            temp=s[start]
            s[start]=s[end]
            s[end]=temp
            start+=1
            end-=1
        