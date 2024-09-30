#Homework2 task2
from collections import deque

def is_palindrome(input_string: str):
    if not len(input_string):
        print("Empty string")
        return False
    
    print(f"Input string is {input_string}")
    d = deque()
    #remove all spaces
    stripped_string = input_string.strip()
    lower_string = stripped_string.lower()

    for i in lower_string:
        d.append(i)
    
    while len(d) > 1:
        if d.pop() == d.popleft():
            print("Elements are equal")
        else:
            print("Elements are not equal, return false")
            return False
    
    return True

def check_result(result: bool, test_string):
    if result:
        print(f"Test string {test_string} is a palindrome\n")
    else:
        print(f"Test string {test_string} is not a palindrome\n")

test_string = "aabaa"
result = is_palindrome(test_string)
check_result(result, test_string)

test_string = "aaaa"
result = is_palindrome(test_string)
check_result(result, test_string)

test_string = "a  aebbaa"
result = is_palindrome(test_string)
check_result(result, test_string)