def is_palindrome(s: str) -> str:
    left = 0
    right = len(s) - 1

    while left < right:
        # Move left pointer rightward if it points to a non-alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1

        # Move right pointer leftward if it points to a non-alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return "Not a palindrome"

        left += 1
        right -= 1

    return "Palindrome"


print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Hello, World!"))