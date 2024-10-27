#5) Palindrome Checker (3 ქულა)
#Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, #punctuation, and capitalization.
#Examples:
#"A man a plan a canal Panama" --> True
#"Hello" --> False
def palindrome(x):
    x=str(x)
    if x[::-1]==x:
        return True
    else:
        return False
stung="AAAAAA"
new_strug=palindrome(stung)

print(new_strug)