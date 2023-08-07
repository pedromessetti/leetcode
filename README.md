# Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, we return [0, 1].
```

### Solutions

1. **Brute Force** - Iter through all possible pairs of elements in the array and checking if their sum is equal to the target. If a pair is found, it returns their indices. The time complexity of this approach is O(n^2) because it iterates through all possible pairs of elements in the array, and the space complexity is O(1) because it does not use any additional data structures. However, isn't an efficient solution for large arrays. For example, if the array has 1000 elements, this approach would need to check 999.000 pairs of elements, which would take a long time to execute. 

    ```
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    ```
2. **One-Pass Hash Table** - Best algorithm to solve the Two Sum problem. First initialize an empty hash table to store the indices of the elements in the input array, then iter over the input array `nums`. For each element `nums[i]`, compute its complement as `target - nums[i]` and check if the complement is already in the hash table. If it's, return the indices of `complement` and `nums[i]`. If it's not, add `nums[i]` to the hash table with its index `i` as the value. This way, we can look up the index of the complement in constant time using the hash table. The time complexity of this algorithm is O(n), where n is the length of the nums list. The space complexity of this algorithm is also O(n), because we need to store the index map (hash table), which has at most n entries.

    ```
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[nums[i]] = i
        return []
    ```

3. **Two-Pass Hash Table** - A variation of the One-Pass Hash Table algorithm that involves two passes over the input array. In the first pass, add each element of `nums` to a hash table along with its index. In the second pass, iterate over `nums` again and check if the complement of each element is in the hash table. If it's, we return the indices of the two numbers that add up to the target. The time complexity of this algorithm is O(n), where n is the length of the input array. The space complexity of this algorithm is also O(n), because we need to store the hash table, which has at most n entries.

    ```
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table and hash_table[complement] != i:
                return [i, hash_table[complement]]
        return []
    ```

### Conclusion
The advantage of using the **One-Pass Hash Table** algorithm over the **Two-Pass Hash Table** algorithm for the Two Sum problem is that it has a better time complexity. The **One-Pass Hash Table** algorithm has a time complexity of O(n), where n is the length of the input array, while the **Two-Pass Hash Table** algorithm also has a time complexity of O(n), but requires two passes over the input array. This means that the **One-Pass Hash Table** algorithm is faster than the **Two-Pass Hash Table** algorithm for large input arrays.

# Palindrome Number
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise. A palindrome is a number that reads the same backward as forward.

Example :

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### Solutions

1. **String Reversal** - Convert the input integer `x` to a string. Then check if the string is equal to the reverse of the string using the slicing operator `[::-1]`. If the string is equal to its reverse, then the input integer `x` is a palindrome and return `True`. Otherwise, return `False`. The time complexity of this algorithm is O(n), where n is the number of digits in the input integer `x` and the space complexity is also O(n), because of the string representation of the input integer in memory.

    ```
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
    ```

2. **Reversal** - The idea behind this algorithm is to reverse the input integer `x` by extracting its digits one by one and adding them to the `reversed_num` in reverse order. If the `reversed_num` is equal to the original input integer, then the input integer is a palindrome. This algorithm has a time complexity of O(log10(n)), where n is the input integer, because we need to extract one digit from the input integer in each iteration. The space complexity of the algorithm is O(1), because we only need to store a few variables in memory.

    ```
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        original_num = x
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return original_num == reversed_num
    ```

### Conclusion
The **Reversal** algorithm can be more efficient than the **String Reversal** algorithm for large input integers, because it doesn't require converting the input integer to a string, which can be more efficient in terms of time and space complexity. However, the **String Reversal** algorithm can be simpler to implement and easier to understand.

# 3 Sum
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i` different from `j`, `i` different from `k`, and `j` different from `k`, and also `nums[i] + nums[j] + nums[k] == 0`.

**OBS**: The solution set must not contain duplicate triplets. The order of the output and the order of the triplets does not matter.

Example:

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

### Solutions

1. **Two-Pointer** - First sort the input array `nums` in non-decreasing order, which takes O(n log n) time, where n is the length of the input array. Then iterate over the input array using a for loop, and for each element `nums[i]`, use two pointers, start and end, to find all unique pairs of elements `nums[start]` and `nums[end]` that add up to `-nums[i]`. We do this by incrementing start if the sum of the three elements is less than zero, decrementing end if the sum is greater than zero, and adding the triplet to the result list if the sum is equal to zero. We also skip over any duplicate elements to avoid duplicate triplets. The time complexity of the algorithm is O(n^2), where n is the length of the input array, because of the for loop iteration over the input array, and for each element, we need to use two pointers to iterate over the remaining elements in the array. The space complexity of the algorithm is O(n), because we need to store the result list in memory.

    ```
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i+1
            end = len(nums)-1

            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1

                else:
                    end -= 1

        return result
    ```

### Conclusion
The **Two-Pointer** approach is a common algorithmic technique used to solve problems that involve searching for a pair or a triplet of elements in an array that satisfy a certain condition. The idea behind the **Two-Pointer** approach is to use two pointers to iterate over the array from both ends, and to move the pointers towards each other based on the value of the elements at the current positions. This approach is often used to solve problems that involve finding pairs or triplets of elements that add up to a certain target value, or that satisfy some other condition.

    