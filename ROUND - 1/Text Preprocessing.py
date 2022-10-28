#!/usr/bin/env python
# coding: utf-8

import string
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# This converts all text into lower case
input_str = open('updated_extract.txt')
str1 = input_str.readlines()
txt = ""
for line in str1:
    txt += line.lower()

# This removes all the numbers
txt = re.sub(r"\d+", "", txt)

# This removes all the special characters
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
txt = txt.translate(translator)

# This will lemmatize the text
lemmatizer = WordNetLemmatizer()
final_txt = ""
input_str = word_tokenize(txt)
for word in input_str:
    final_txt += " " + lemmatizer.lemmatize(word)

# This removes all the extra whitespaces
txt = txt.strip()

# Writes the processed text in the new processed_text.txt file
file = open(r"processed_text.txt" , "a")
file.writelines(txt)
file.close()