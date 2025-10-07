class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize index, sign, and result
        i = 0
        sign = 1
        res = 0

        # Skip leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # Return 0 if only spaces are found
        if i == len(s):
            return 0

        # Check for optional '+' or '-' sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Convert characters to integer while valid digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            # Clamp to 32-bit signed integer range
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -2**31:
                return -2**31

            i += 1

        # Return final result after applying sign
        return sign * res

if __name__ == "__main__":
    sol = Solution()
    input_str = "   -42"
    result = sol.myAtoi(input_str)
    print("Converted integer:", result)
