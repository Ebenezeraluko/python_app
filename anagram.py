# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def is_anagram(word, anagram):
    # [assignment] Add your code here
    if (sorted(word) == sorted(anagram)):
        return True
    else:
        return False
result = is_anagram("hello", "check")
print(f"The anagram is {result}")

def is_anagram(str1, str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False
    
outcome = is_anagram("below", "elbow")
print(f"The anagram is {outcome}")