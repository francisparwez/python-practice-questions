# from collections import Counter

# def first_non_repeating_char(s: str):
#     char_counts = Counter(s)
    
#     for char in s:
#         if char_counts[char] == 1:
#             return char
            
#     return None

def first_non_repeating_char(s: str):
    counts = {}
    for char in s:
        # counts[char] = counts.get(char, 0) + 1
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1


    for char in s:
        if counts[char] == 1:
            return char
            
    return None 

print(first_non_repeating_char("swiss"))
print(first_non_repeating_char("leetcode"))
print(first_non_repeating_char("loveleetcode"))
print(first_non_repeating_char("aabbcc"))   