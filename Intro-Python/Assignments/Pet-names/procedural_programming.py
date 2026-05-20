# Algorithm for a palindrome

str = "racecar"

def isPalindrome(str):
    startIndex=0
    endIndex = len(str) -1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex+=1
        endIndex-=1
    
    return True

print(isPalindrome('racescar'))
# str2 = str.reverse()

# if str == str2:
#     print("It is a palindrome!")
# else:
#     print("word is not a palindrome!")
