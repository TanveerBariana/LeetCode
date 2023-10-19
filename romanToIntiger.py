class Solution:
    def romanToInt(self, s: str) -> int:
        input = list(s)
        result = 0 
        last_value = 0
        for numeral in input:
            if numeral == 'I':
                result = result +1
                last_value = 1 
            elif numeral == 'V':
                if last_value == 1:
                    result = result + 3
                    last_value = 4
                else:
                    result = result + 5
                    last_value = 5
            elif numeral == 'X':
                if last_value == 1:
                    result = result + 8
                    last_value = 9 
                else:
                    result = result + 10
                    last_value = 10
            elif numeral == 'L' :
                if last_value == 10:
                    result = result+30
                    last_value = 40
                else:
                    result = result + 50
                    last_value = 50
            elif numeral == 'C' :
                if last_value == 10:
                    result = result+80
                    last_value = 90
                else:
                    result = result + 100
                    last_value = 100
            elif numeral == 'D' :
                if last_value == 100:
                    result = result+300
                    last_value = 300
                else:
                    result = result + 500
                    last_value = 500
            elif numeral == 'M' :
                if last_value == 100:
                    result = result+800
                    last_value = 800
                else:
                    result = result + 1000
                    last_value = 1000
        return result

    