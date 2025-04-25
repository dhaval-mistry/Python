
# logic to check if two strings are anagrams of each other
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")

