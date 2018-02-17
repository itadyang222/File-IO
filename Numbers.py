'''
Created on February 3, 2018

@author: ITAUser
'''

filename = "number.txt"
numberfile=open("number.txt","r+");


numberline = 0;
numberwords = 0;
numberchar = 0;

for line in numberfile:
    words = line.split();
    numberline = numberline + 1;
    numberwords = len(line);
    
    print(numberwords);
    
    
filename = "constituton.txt"
numberfile = open("constituton.txt","r+");


numberwords = 0;


for line in numberfile:
    words = line.split();
    numberline = numberline + 1;
    numberwords = len(line);
    
    print(numberwords);