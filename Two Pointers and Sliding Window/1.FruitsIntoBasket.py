# Problem description
""" Leetcode 904: Fruits into basket
🍇 Problem Description
You're walking along a row of fruit trees 🍎🍌🍐... and can pick fruits with only two baskets 🧺🧺.

Each basket can only carry one type of fruit, but unlimited quantity of that type.

Starting from any tree, you must pick exactly one fruit per tree, moving only to the right 👉.

You stop picking when a tree has a fruit type that doesn't fit in your two baskets.

Your task?
Return the maximum number of fruits you can collect under these rules.

Approach
We initialize two pointers: start and end to define our sliding window.

A HashMap stores the count of each fruit type in the current window.

Expand the window by moving end ➡️ and adding fruits to the map.

If the map has more than 2 fruit types, shrink the window from start until we're back to only two types 🍎🍌.

Keep updating the maximum length (maxLen) at each valid window.

🧮 Complexity
Time complexity: O(n)
👉 Each fruit is added and removed from the map at most once.

Space complexity: O(1)
👉 The map stores at most 3 keys at any point (though 2 is the limit, temporarily it might hold 3 during adjustment).

🎉 Example
👉 Input:

fruits = [🍎, 🍌, 🍌, 🍇, 🍇, 🍇, 🍌, 🍌, 🍎, 🍎, 🍎, 🍇]
             0   1   2   3   4   5   6   7   8   9  10  11
✅ Pick : Picked window: [🍌, 🍌, 🍇, 🍇, 🍇, 🍌, 🍌]
Index range :                1   2   3   4   5   6   7

"""
'''
input and output:
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''


# initializing two pointers
def fruitIntoBasket():
    fruits=[1,2,3,2,2]
    #intializing the hashmap or dictionary
    hashmap={}
    start=0 #it start from zero
    maxLen=0 #maximum fruits you can obtain from the basket

    for end in range(len(fruits)):
        if fruits[end] in hashmap:
            hashmap[fruits[end]]+=1 #if the one type of fruit already in basket just add same type
        else:
            hashmap[fruits[end]]=1 #if no this type then add to 1
        while len(hashmap)>2: #if basket contain more than 2 type of fruits then remove from hashmap
            hashmap[fruits[start]]-=1 #decrease the freuency of fruit by 1
            if hashmap[fruits[start]]==0: # if frequency is zero then remove from the hashmap
                del hashmap[fruits[start]]
            start+=1 # move to next index
        
        if len(hashmap)<=2:
            maxLen=max(maxLen,end-start+1) # get the maximum fruits or elements

    return maxLen

print(fruitIntoBasket())


