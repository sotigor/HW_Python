"""Creating a dictionary from a string with unique words and there occurrences in the string"""

# Open a file with text which considered as a string
with open('Text_for_Task_1.txt', 'r') as text:
    dict_words = {}
# Iterating through all lines in a file
    for line in text.readlines():
        list_of_words = line.split()
# Iterating through words in each line
        for word in list_of_words:
            word = word.lower()
# Iterating through characters in each word
# Checking whether the word is word but not a digit or number
            for char in word:
                if char.isdigit():
                    word = 'ignore'
                    break
            if word == 'ignore':
                break
# Deleting symbols ',' and '.'
            if ',' in word or '.' in word:
                word = word[:-1]
# Making the required dictionary
                if word not in dict_words:
                    dict_words[word] = 1
                else:
                    dict_words[word] += 1
            elif word not in dict_words:
                dict_words[word] = 1
            else:
                dict_words[word] += 1
print(dict_words)
