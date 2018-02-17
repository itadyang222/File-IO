'''
Created on Feb 17, 2018

@author: ITAUser
'''
fname = "constituton.txt"
f=open(fname, "r+")


for line in f:
    words = line.split()
    num_words = len(words)+ num_words
    for word in words:
        i += word.count("p")

print(i)