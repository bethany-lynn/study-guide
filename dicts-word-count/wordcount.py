"""Count words in file."""


# put your code here.

# split(" ")
#case differences to everything should be lower or upper case

#make function below
def word_count(filename):
    #generate counter dictionary
    counter = {}

    #open file
    file = open(filename)
    #loops through each line in the file
    for line in file:
        clean_line= line.strip()
        word_lst = clean_line.split(" ")
        #loop through each word in each line add count to dictionary count{}
        for word in word_lst:
            counter[word] = counter.get(word, 0) + 1
    return counter
#created function where we use the file as a parameter to call alter as argument
# created empty dictionary to return the new dictionary of key: value = word: count
# key = word
# value = count
# items = word:count or key:value 
# dict[key] = value
# counter[word] = count
#open the file
# looping through each line
# strip - gets rid of empty space on the outsides, not between keys
# separating at each space 
# nested for loop to dictionary[key] to find value
# line 22 dictionary is getting the word if its there, adding if its not

# my_dict[letter] = my_dict.get(letter, 0) +1


## if word no in word_lst:
    #word_lst[word] = 1
# else:
#   word_lst[word] += 1

#call function
print(word_count("test.txt"))