# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        while True:
            row = rand7()
            col = rand7()
            num = (row - 1) * 7 + col

            if num <= 40:
                return (num - 1) % 10 + 1
                
        