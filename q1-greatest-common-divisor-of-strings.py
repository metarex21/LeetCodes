# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2==str2+str1:
            return str1[:gcd(len(str1),len(str2))]
        else:return ""

    def gcd(a,b):
        for i in range(min(a,b),0,-1):
            if a%i==0 and b%i==0:
                return i
