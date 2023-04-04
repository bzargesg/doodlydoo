
def reverse_string(input_string: str):
    result = ''.join(list(input_string)[::-1])
    print(f"result is: {result}")
    return result