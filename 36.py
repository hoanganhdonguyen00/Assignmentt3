def middle_character(s):
    length = len(s)
    mid = length // 2

    if length % 2 == 0:
        return s[mid - 1: mid + 1]
    else:
        return s[mid]
text = input("Enter a word: ")
result = middle_character(text)
print("Middle character(s):", result)
