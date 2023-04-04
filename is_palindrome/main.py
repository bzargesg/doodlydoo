

# def is_palindrome(input_str: str) -> bool:
#     a, b = 0, len(input_str)-1
#     while(a<b):
#         if input_str[a] != input_str[b]:
#             return False
#         a=a+1
#         b=b-1
#     return True

def is_palindrome(input_str: str) -> bool:
    return input_str == input_str[::-1]