from typing import List
from functools import reduce


# def find_largest_int(int_list: List[int]) -> int:
#     int_list.sort()
#     print(int_list)
#     result = int_list[-1]
#     print(f"returning result {result}")
#     return result
    
# def find_largest(a, b):
#     return max(a,b)

# def find_largest_int(int_list: List[int]) -> int:
#     result = reduce(find_largest, int_list)
#     print(f"returning result {result}")
#     return result

# def find_largest_int(int_list: List[int]) -> int:
#     result = reduce(lambda x, y: max(x, y), int_list)
#     print(f"returning result {result}")
#     return result

# def find_largest_int(int_list: List[int]) -> int:
#     result = max( int_list )
#     print(f"returning result {result}")
#     return result

def find_largest_int(int_list: List[int]) -> int:
    max = None
    for x in int_list:
        if isinstance(x, int):
            if max is None or x > max:
                max = x
    print(f"returning result {max}")
    return max

