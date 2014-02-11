#import file
from sys import argv
script, filename = argv
#open and read file and then convert it all to lower case
f = open (filename, "r")
myfile = f.read()

f.close()
#make string of words lower case
myfile = myfile.lower()
#get rid of punctuation replacing characters outside of lower case letters in ord with space
#builds a new string called clean
clean = ""
"""read through string called myfile character by character 
and if the character is a letter (between ord of a to z)
it will be added to the string clean 
if it's not a letter it will add a space and not add that character
"""
for character in myfile:
 
    if ord(character) < ord("a") or ord(character) > ord("z"):       
        clean = clean + " "
    else:
        clean = clean + character

#the following will split the long string of words at whitespace into a list of words
split_words = clean.split()

#make an empty dictionary
d = {}
#iterate through split_words and add each word to dictionary if it's not there
for word in split_words:
    if d.get(word):
        d[word] += 1
        #print "this word is in dictionary already added 1", word   
    else:   
        d[word] = 1  
        #print "added to dictionary:", word  
#print our dictionary with word counts
for key, value in d.iteritems():
    print key, value


#for word in twain_read_lower:
    #if ord(word) > 122 or < 97:
#        word.replace()






