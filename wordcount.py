#open and read file and then convert it all to lower case

twain = open('twain.txt')
twain_read = twain.read()
twain_read_lower = twain_read.lower()
twain_replace = twain_read_lower.replace("--", " ")   

for word in twain_read_lower:
    if ord(word) > 122 or < 97:
        word.replace()


#count how many times each space-separated word occurs in file
value = 0
twain_dictionary = {}
#split all space-separated words
   
for word in twain_replace.split():
    #stripping the punctuation from the document, but only if it is at the end of a word
    stripped_word = word.strip("!,.';:-\"?_")
    #print stripped_word
    #modifies dictionary and adds the count
    twain_dictionary[stripped_word] = twain_dictionary.get(stripped_word, 0) + 1
 
#loops through each word and value in the dictionary and prints them
for word, value in twain_dictionary.iteritems():
    print word, value



