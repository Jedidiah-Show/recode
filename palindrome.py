Ldef is_palindrome(text, left=0, right=0):
    if right == 0:
        right = len(text)-1

    if left >= right:
        return "Palindrome"

    if not text[left].isalnum():
        return is_palindrome(text, left + 1, right)
    if not text[right].isalnum():
        return is_palindrome(text, left, right - 1)
        
    if text[left].lower() != text[right].lower():
        return "Not a Palindrome"
    
    return is_palindrome(text, left + 1, right - 1)

print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Hello, World!"))


