# # two pointer 

s = "Hello World"
s_list = list(s)

left = 0
right = len(s_list) -1

while left < right:
    s_list[left], s_list[right] = s_list[right], s_list[left]

    left += 1
    right -= 1

resuklt = "".join(s_list)

print("Original : Hello World")
print("Modified : ", {resuklt})

# Two Sum

class Solution:
    def twosum(self , nums : list[int] , target : int) -> list[int]:

        seen ={}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
sol = Solution()
nums = [2, 7 , 10, 15]
target = 9
print(sol.twosum(nums, target))




class Solution:
    def largestInteger(self , nums: list[int] , k: int) -> list[int]:

        if k == len(nums):
            return [max(nums)]

        if k == 1:
            arr = [x for x in nums if nums.count(x) ==1]
        else:
            arr = [x for x in (nums[0] , num[-1] if nums.count(x) == 1]

        return max(arr) if arr else -1