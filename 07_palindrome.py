# Program 7: Check whether a word is a palindrome using a function

def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
