def is_palindrome(s: str):
    left = 0
    right = len(s) - 1

    while left < right:
# ************  Move left pointer rightward if it points to a non-alphanumeric character ************ 
        if not s[left].isalnum():
        # if not (("a" <= s[left] <= "z") or ("A" <= s[left] <= "Z") or ("0" <= s[left] <= "9")):
        # if s[left] in ",. !?":
            left += 1
# ************  Move right pointer leftward if it points to a non-alphanumeric character ************ 
        if not s[right].isalnum():
        # if s[right] in (",", ".", " ", "!", "?"):
            right -= 1

# ************ Compare characters ignoring case ************
        if s[left].lower() != s[right].lower():
            return "Not a palindrome"

        left += 1
        right -= 1

    return "Palindrome"


print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Hello, World!"))