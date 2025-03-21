# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

class Solution:
    def getSum(self, a, b) :
        bitshortner = 0xFFFFFFFF

        while (b & bitshortner) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & bitshortner) if b > 0 else a

sum = Solution()
print(sum.getSum(1,2))
