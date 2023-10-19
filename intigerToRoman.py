class Solution:
    def intToRoman(self, num :int = 0, text : str = '') -> str:
        if num // 1000 >= 1:
            return self.intToRoman(num - 1000, text + 'M')
        elif num // 900 >= 1:
            return self.intToRoman(num - 900, text+'CM')
        elif num // 500 >= 1:
            return self.intToRoman(num - 500, text + 'D')
        elif num // 400 >= 1:
            return self.intToRoman(num-400, text+'CD')
        elif num // 100 >= 1:
            return self.intToRoman(num- 100, text+'C')
        elif num // 90 >= 1:
            return self.intToRoman(num- 90, text + 'XC')
        elif num // 50 >= 1:
            return self.intToRoman(num- 50, text+ 'L')
        elif num // 40 >= 1 :
            return self.intToRoman(num -40, text+ 'XL')
        elif num // 10 >= 1 :
            return self.intToRoman(num - 10, text + 'X')
        elif num // 9 >= 1 :
            return self.intToRoman(num- 9, text + 'IX')
        elif num // 5 >= 1 :
            return self.intToRoman(num-5, text + 'V')
        elif num // 4 >= 1 :
            return self.intToRoman(num - 4, text + 'IV')
        elif num // 1 >= 1 :
            return self.intToRoman(num - 1, text + 'I')
        else:
            return text

Solution().intToRoman(1994)
# class Roman:
#     def __init__(self, val=0, text=''):
#         self.val = val
#         self.text = text
    

