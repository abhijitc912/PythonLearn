# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "The quick brown fox jumps over the lazy dog."
 
# Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1
 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
