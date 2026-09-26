words = ["python", "sql", "machine", "learning", "data", "engineering"]

def longest_word(words):
    longest = ""
    
    for word in words:
        if longest == "" or len(word) > len(longest):
            longest = word            
        
    return {longest: len(longest)}

print(longest_word(words))