#import file
from sys import argv
script, filename = argv
#open and read file and then convert it all to lower case
f = open (filename, "r")
myfile = f.read()

f.close()
#the following will split the long string of words at whitespace into a list of words
split_words = myfile.split()
#make an empty dictionary
d = {}
#iterate through split_words and add each word to dictionary if it's not there
for word in split_words:
    if d.get(word):
        d[word] += 1
        print "this word is in dictionary already added 1", word   
    else:   
        d[word] = 1  
        print "added to dictionary:", word  




#twain_read_lower = twain_read.lower()
#twain_replace = twain_read_lower.replace("--", " ")   

#for word in twain_read_lower:
    #if ord(word) > 122 or < 97:
#        word.replace()






