#This problem was asked by Twitter.

#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#Hint: Try preprocessing the dictionary  into a more efficient data structure to speed up queries.

#function which does the adding to the trie 
def add_to_trie(word, trie):
    # if no word return the trie as it is
    if not word:
        return trie
    #take first charchter
    character = word[0]
    #if charchater not in trie then make node for that value
    if character not in trie:
        trie[character] = dict()
        
    #otherwise process rest of word and make into trie
    trie[character] = add_to_trie(word[1:], trie[character])
    
    #return trie
    return trie

#function which creates the whole trie
def get_dictionary_trie(dictionary):
    #trie is a dictinary
    trie = dict()
    #for each word in dictionaary
    for word in dictionary:
        #add to the trie using the above function
        trie = add_to_trie(word, trie)

    return trie

# getting possible completeions from the trie
def get_possible_completions(trie):
    #set off as empty list
    possible_completions = list()
    #for each node in tree/ charchter in the trie
    for character in trie:
        # if node exists
        if trie[character]:
            # get child completions from that point onward exluding previous
            child_completions = get_possible_completions(trie[character])
            #for each child completion from that point onward and etc. add to possible combos
            for child_completion in child_completions:
                possible_completions.append(character + child_completion)
        #otherwise just add the chatahchter
        else:
            possible_completions.append(character)
    #return word    
    return possible_completions

# function which puts it all together
def get_autocomplete_suggestions(s, dictionary):
    # make the data strcuture/trie
    trie = get_dictionary_trie(dictionary)
    
    # go through the trie
    current_trie = trie
    #for charachter in prefix
    for character in s:
        #if charchter not in trie return empty
        if character not in current_trie:
            return []
        #otherise get the following suffix and combine to suffic
        current_trie = current_trie[character]
    completions = get_possible_completions(current_trie)
    completions = [s + x for x in completions]
    
    #return completeion
    return completions 

assert get_autocomplete_suggestions("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_autocomplete_suggestions("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert get_autocomplete_suggestions("ae", ["cat", "car", "cer"]) == []
assert get_autocomplete_suggestions("ae", []) == []

