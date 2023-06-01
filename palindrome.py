word=input("Please enter the word to check: ")
def reverse(word):
    reversedWord=""
    ##Looping through the characters backward
    for character in range(len(word)-1,-1,-1):
        ##Storing the characters of the wtring backward
        reversedWord+=word[character]
        
    if reversedWord == word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"
    
print(reverse(word))
