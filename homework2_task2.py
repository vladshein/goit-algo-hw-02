#Homework2 task2
from collections import deque

def is_palindrome(input_string: str):
    if not len(input_string):
        print("Empty string")
        return False
    
    d = deque()
    #remove all spaces
    stripped_string = input_string.strip()

    for i in stripped_string:
        d.append(i)
    print(d)
    print(len(d))

    while len(d) > 1:
        if d.pop() == d.popleft():
            print("Elements are equal")
        else:
            print("Else case")
            return False
    
    return True

def check_result(result: bool):
    if result:
        print("Input string is a palindrome")
    else:
        print("Input string is not a palindrome")

test_string = "aabaa"
result = is_palindrome(test_string)
check_result(result)

test_string = "aaaa"
result = is_palindrome(test_string)
check_result(result)

test_string = "a  aebbaa"
result = is_palindrome(test_string)
check_result(result)