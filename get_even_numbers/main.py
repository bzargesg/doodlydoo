# def get_even_numbers(nums: list[int]) -> list[int]:

# def get_even_numbers(nums: list[int]) -> list[int]:
#     result = []
#     for x in nums:
#         if x % 2 == 0:
#             result.append(x)
#     return result


# def get_even_numbers(nums: list[int]) -> list[int]:
#     return list(filter(lambda x: x % 2 == 0, nums))

def get_even_numbers(nums: list[int]) -> list[int]:
    return [x for x in nums if x % 2 == 0]