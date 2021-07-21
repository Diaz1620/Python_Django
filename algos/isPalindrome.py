def reverseString(strInput):
    newString = ""
    for i in range(len(strInput)-1, -1, -1):
        newString += strInput[i]
    return newString


def isPalindrome(strInput):
    if strInput == reverseString(strInput):
        return True
    else:
        return False


def isPal2(strInput):
    for i in range(0, len(strInput)//2, 1):
        if strInput[i] != strInput[len(strInput)-1-i]:
            return False
    return True

# print(reverseString("hello"))

# print(isPalindrome("hello"))
# print(isPalindrome("racecar"))
# print(isPalindrome("x 0 x"))

print(isPal2("racecar"))
print(isPal2("hello"))
print(isPal2("x 0 x"))