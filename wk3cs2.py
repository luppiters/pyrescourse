###case study 2: TRANSLATIONS of HAMLET

#In this case study, we will find and plot the distribution of word frequencies for each translation of Hamlet.
#Perhaps the distribution of word frequencies of Hamlet depends on the translation --- let's find out!
#For these exercises, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos
#(Videos 3.2.x).

##part 1
"""
Write a function word_count_distribution(text) that takes a book string and returns a dictionary with items corresponding to the count of times a collection of words appears in the translation, and values corresponding to the number of number of words that appear with that frequency.
First use count_words_fast(text) to create a dictionary called word_counts with unique words in the dictionary as keys and their frequency in the book as values.
Next, create and return a new dictionary count_distribution with unique values from word_counts as keys and their frequency as values. For example, 'you are what you eat' contains three words that occur once and one word that occurs twice, so word_count_distribution('you are what you eat') should return a dictionary {1:3, 2:1}.
'Romeo and Juliet' is preloaded as text. Call word_count_distribution(text), and save the result as distribution."""

# input your code here!
from collections import Counter

def word_count_distribution(text): #text is a string
     word_counts = count_words_fast(text)
     count_distribution = Counter(word_counts.values())
     return count_distribution

distribution = word_count_distribution(text)

##PART 2
"""Create a function more_frequent(distribution) that takes a word frequency dictionary (like that made in Exercise 1)
and outputs a dictionary with the same keys as those in distribution (the number of times a group of words appears in the text),
and values corresponding to the fraction of words that occur with more frequency than that key.
Call more_frequent(distribution), and store as cumulative."""

# input your code here!
import numpy as np

def more_frequent(distribution):
    freq_key = list(distribution.keys())
    counts_freq = list(distribution.values())
    cum_freq = np.cumsum(counts_freq)
    more_frequent = 1 - (cum_freq/cum_freq[-1])
    
    return dict(zip(freq_key, more_frequent))
    
cumulative = more_frequent(distribution)


##part 3
"""Edit the code used to read though each of the books in our library, and store the word frequency distribution for each
translation of William Shakespeare's "Hamlet" as a Pandas dataframe hamlets with columns named "language" and "distribution".
word_count_distribution is preloaded from Exercise 1. How many translations are there? Which languages are they translated
into?"""

import pandas as pd
hamlets = pd.DataFrame(columns = ("language", "distribution")) #added
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text) #added
                hamlets.loc[title_num] = language, distribution 
                title_num += 1
##There are three translations: English, German, and Portuguese.###

##part 4
#Plot the word frequency distributions of each translations on a single log-log plot. Note that we have already done most
#of the work for you. Do the distributions of each translation differ?
import matplotlib.pyplot as plt

colors = ["crimson", "forestgreen", "blueviolet"]
handles, hamlet_languages = [], []
for index in range(hamlets.shape[0]):
    language, distribution = hamlets.language[index+1], hamlets.distribution[index+1]
    dist = more_frequent(distribution)
    plot, = plt.loglog(sorted(list(dist.keys())),sorted(list(dist.values()),
        reverse = True), color = colors[index], linewidth = 2)
    handles.append(plot)
    hamlet_languages.append(language)
plt.title("Word Frequencies in Hamlet Translations")
xlim    = [0, 2e3]
xlabel  = "Frequency of Word $W$"
ylabel  = "Fraction of Words\nWith Greater Frequency than $W$"
plt.xlim(xlim); plt.xlabel(xlabel); plt.ylabel(ylabel)
plt.legend(handles, hamlet_languages, loc = "upper right", numpoints = 1)
# show your plot using `plt.show`!
plt.show() #is this for real the only thing i need


"""The distributions differ somewhat, but their basic shape is the same. By the way, distributions that look like a straight
line like these are called 'scale-free,' because the line looks the same no matter where on the x-axis you look!"""
