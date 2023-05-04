#!/usr/bin/python3

# You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in
# the same order except that you take the first letter of each word and put it on the end, then you
# add 'ay' to the end of that. ("road" = "oadray") 
# Task
# Your task is to take a sentence in English and turn it into the same sentence in Pig Latin! 
# Input Format 
# A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization)
# Output Format 
# A string of the same sentence in Pig Latin.
# Sample Input 
# "nevermind youve got them"
# Sample Output 
# "evermindnay ouveyay otgay hemtay

# Write your program belo
def converter(strchr):
    if strchr == "":
        return
    str_list = list(strchr.split())
    final_word = []
    for ch in str_list:
        word = ch[0]
        new_word = []
        for c in range(1, len(ch)):
            new_word.append(ch[c])
        new_word.append(word)
        new_word.append("ay")
        final_word.append(str("".join(new_word)))
    return str(" ".join(final_word))


user_str = input("Enter a Sentence: ")
new_str = converter(user_str).strip()
print(f"Original Sentence:\n\"{user_str}\"\n")
print(f"Pig Latin Sentence:\n\"{new_str}\"")
