class Solution:
    def romanToInt(self, s: str) -> int:
        
        ans = 0

        def ri(letter):
            match letter:
                case "I" :
                    return 1
                case "V" :
                    return 5
                case "X" :
                    return 10
                case "L" :
                    return 50
                case "C" :
                    return 100
                case "D" :
                    return 500
                case "M" :
                    return 1000
                case default:
                    return 0

        for i in range(len(s)-1):
            if ri(s[i]) < ri(s[i+1]) : 
                ans -=  ri(s[i])
            else:
                ans +=  ri(s[i])
        
        ans += ri(s[len(s)-1])

        return ans
                





