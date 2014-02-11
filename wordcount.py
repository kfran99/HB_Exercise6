#open a file named on command line 

#print those counts to screen

#open file
#for line in twain: do something
twain = open('twain.txt')
twain_read = twain.read()
    

#count how many times each space-separated word occurs in file
value = 0
twain_dictionary = {}
#split all space-separated words

   
   
for word in twain_read.split():
     #clean up double dash connected words
    #split words at double dashes
    #cleaned_word = twain_read.split("-")

    #stripping the punctuation from the document, but only if it is at the end of a word
    stripped_word = word.strip("!,.';:-\"?_")
        #print stripped_word
    #modifies dictionary and adds the count
    twain_dictionary[stripped_word] = twain_dictionary.get(stripped_word, 0) + 1
 
#loops through each word and value in the dictionary and prints them
for word, value in twain_dictionary.iteritems():
    print word, value



