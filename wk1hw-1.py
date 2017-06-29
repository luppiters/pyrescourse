#1a
"""Instructions:Import the string library.
Create a variable alphabet that consists of the lowercase and uppercase letters in the English alphabet
using the ascii_letters attribute of the string library.
"""
import string

alphabet = string.ascii_letters


#1b
"""The lower and upper cases of the English alphabet is stored as alphabet.
Consider the sentence 'Jim quickly realized that the beautiful gowns are expensive'. 
Create a dictionary count_letters with keys consisting of each unique letter in the sentence and 
values consisting of the number of times each letter is used in this sentence. 
Count both upper case and lower case letters separately in the dictionary.
"""

sentence = 'Jim quickly realized that the beautiful gowns are expensive'
sentence = sentence.replace(' ', '')

count_letters = {i:sentence.count(i) for i in set(sentence)}
#write your code here!


print(count_letters)

"""

1c
"""Rewrite your code from 1b to make a function called counter that takes a string input_string and
returns a dictionary of letter counts count_letters. If you were unable to complete 1b,
you can use the solution by selecting Show Answer.
Use your function to call counter(sentence)."""

import string
sentence = 'Jim quickly realized that the beautiful gowns are expensive'


# Create your function here!
def counter(input_string):
    count_letters = {i:input_string.count(i) for i in set(input_string)}
    return count_letters

counter(sentence)



#1d
"""Abraham Lincoln was a president during the American Civil War. His famous 1863 Gettysburg Address 
has been stored as address, and the counter function defined in part 1c has been loaded. 
Use these to return a dictionary consisting of the count of each letter in this address, and save this as address_count.
Print address_count."""

# Write your code here!
address_count=dict()
address_count= counter(address)
print(counter(address))
print(address_count)


#1e

"""The frequency of each letter in the Gettysburg Address is already stored as address_count. 
Use this dictionary to find the most common letter in the Gettysburg address."""

most_frequent_letter=max(address_count, key=address_count.get)

print(most_frequent_letter)


Store this letter as most_frequent_letter, and print your answer.
