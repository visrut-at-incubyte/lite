# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    def __init__(self):
        self.mappings = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'                
        }

    def intToRoman(self, num: int) -> str:
        sol = ''
        modules = list(self.mappings.keys())

        i = len(modules) - 1

        while i >= 0:
            if num % modules[i] != num and (num % modules[i] != 0):
                sol += self.mappings[modules[i]]
                num -= modules[i]
            else:
                sol += self.mappings[modules[i]] * (num // modules[i])
                num %= modules[i]
                i -= 1

        return sol

if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(56))