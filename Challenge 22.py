#This problem was asked by Microsoft.

#Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
#If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, 
#then return null.

#For example, given the set of words ‘quick’, ‘brown’, ‘the’, ‘fox’, and the string “thequickbrownfox”, 
#you should return [‘the’, ‘quick’, ‘brown’, ‘fox’].

#Given the set of words ‘bed’, ‘bath’, ‘bedbath’, ‘and’, ‘beyond’, and the string “bedbathandbeyond”, 
#return either [‘bed’, ‘bath’, ‘and’, ‘beyond] or [‘bedbath’, ‘and’, ‘beyond’].


#create function to split string to words
def get_sentence_split(s, words):
    #if imputs wronds return empty
    if not s or not words:
        return []
   
    #make set of words
    word_set = set(words)
    #make empty list to store words in string
    sentence_words = list()
    #loop for each chachter in string
    for i in range(len(s)):
        #if string slice in the word set
        if s[0:i + 1] in word_set:
            #then append to the empty list
            sentence_words.append(s[0:i + 1])
            #and remove from the word set so not used again
            word_set.remove(s[0:i + 1])
            #then move along the string by using the function again on the sliced string
            sentence_words += get_sentence_split(s[i + 1:], word_set)
            break
    #return the setence words
    return sentence_words


assert get_sentence_split("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == [
    'the', 'quick', 'brown', 'fox']
assert get_sentence_split("bedbathandbeyond", [
                          'bed', 'bath', 'bedbath', 'and', 'beyond']) == ['bed', 'bath', 'and', 'beyond']
