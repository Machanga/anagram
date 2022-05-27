# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    text1 = word.replace(" ", "")
    text2 = anagram.replace(" ", "")
    
    if sorted(text1) == sorted(text2):
        return True
    else:
        return False
        
# Anagrams
find_anagram("listen", "silent")
find_anagram("astronomer", "moon starer") 
find_anagram("a gentleman", "elegant man") 

# Not anagrams
find_anagram("Mouse", "House")
find_anagram("School Master", "The classroom")
    

