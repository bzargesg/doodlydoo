
# def is_anagram(str1:str, str2:str)->bool:
#     if len(str1) != len(str2):
#         return False
#     list1=list(str1)
#     list1.sort()
#     list2=list(str2)
#     list2.sort()
#     for index,value in enumerate(list1):
#         if value != list2[index]:
#             return False
        
#     return True

# def is_anagram(str1: str, str2: str) -> bool:
#     return sorted(str1) == sorted(str2)

# from collections import Counter

# def is_anagram(str1: str, str2: str) -> bool:
#     return Counter(str1) == Counter(str2)

def str_to_dict(str: str) -> dict[str, int]:
    result = {}
    for char in str:
        if char not in result:
            result[char] = 1
        else:
            result[char] = result[char] + 1
    return result

def is_anagram(str1: str, str2: str) -> bool:
    return str_to_dict(str1) == str_to_dict(str2)