import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Enter Your Number : "))

        if user_num == lucky_num:
            print("You Win")
            break
        elif user_num < lucky_num:
            print("Your Number is Low")
        elif user_num > lucky_num:
            print("Your Number is High")


play_game()
print("Game Over , Thanks For Playing")


# Leetcode problem find missing numbers
class Solution:
    
    def findMissingAndRepeatedValues(self, x):
        
        minimum = min(x)
        maximum = max(x)

        s = set(x)

        ans = []

        for i in range(minimum, maximum + 1):
            if i not in s:
                ans.append(i)

        return ans
sol = Solution()
x = [1, 3, 2, 5]
print(sol.findMissingAndRepeatedValues(x))
print("Thank You.")

# leetcode problem length of last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = "hello world"
        words = s.split()

        last_word = words[-1]
        return len(last_word)
    
s = input("Enter Your Name : ")
result = Solution().lengthOfLastWord(s)
print(result)
