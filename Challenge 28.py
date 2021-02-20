#Question 28

#This problem was asked by Palantir.

#Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
#return a list of strings which represents each line, fully justified.

#More specifically, you should have as many words as possible in each line. 
#There should be at least one space between each word. 
#Pad extra spaces when necessary so that each line has exactly length k. 
#Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

#If you can only fit one word on a line, then you should pad the right-hand side with spaces.

#Each word is guaranteed not to be longer than k.

#For example, given the list of words [“the”, “quick”, “brown”, “fox”, “jumps”, “over”, “the”, “lazy”, “dog”] and k = 16, 
#you should return the following:

#[“the quick brown”, # 1 extra space on the left “fox jumps over”, # 2 extra spaces distributed evenly “the lazy dog”]
# 4 extra spaces distributed evenly



#function intake list of words and a k integer value
def justify_text(words, max_line_length):
    
    #create empty list to store the lines
    lines = list()
    
    #-1 in cumulative length
    cumulative_length = -1
    #empty list to store current words
    current_words = list()
    #empty list store line length
    line_lengths = list()
    
    #for each words in list of words
    for word in words:
#########if k less than length of words
        if cumulative_length + (len(word) + 1) > max_line_length:
            #appends empty list to lines
            lines.append(current_words)
            #append cumulative length to line lengths
            line_lengths.append(cumulative_length)
            #set cumulativ length to -1
            cumulative_length = -1
            #make current word list empty
            current_words = list()
###########however if less than - make cumulative length the length of words
########cumulative_length += (len(word) + 1)
#########and then append to current word list
        current_words.append(word)
        print(current_words)
        print(cumulative_length)
    #if current words not empty
    if current_words:
        #append to the line
        lines.append(current_words)
        #and append the cuulaitve length to line lenghts
        line_lengths.append(cumulative_length)

    print(lines)
    print(line_lengths)
    
    #make new line empty list
    justified_lines = list()
    #loop through  the lines and line lengths progressivley
    for words, length in zip(lines, line_lengths):
        #find amount of spcaces to add
        spaces_to_add = max_line_length - length
        # do divison not to get raminder spcces/by length word
        guaranteed_spaces = 1 + (spaces_to_add // (len(words) - 1))
        # do dvsion just to get remainder
        bonus_space_recipients = spaces_to_add % (len(words) - 1)
        print("spaces_to_add: {}".format(spaces_to_add))
        #make empty string for line
        line = ""
        #loop throguh words in line for a last removed char in string
        for (index, word) in enumerate(words[:-1]):
            #add word to line
            line += word
            #add guranted spcae
            line += guaranteed_spaces * " "
            #if index not bonus spcae recipeint
            if index < bonus_space_recipients:
                #just add space
                line += " "
        
        line += words[-1]
        print(line)
        justified_lines.append(line)

    print(justified_lines)
    return justified_lines


assert justify_text(["the", "quick", "brown", "fox", "jumps",
                     "over", "the", "lazy", "dog"], 16) == \
    ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
assert justify_text(["the", "quick", "brown", "fox", "jumps", "over"], 16) == \
    ['the  quick brown', 'fox  jumps  over']
assert justify_text(["the", "quick"], 16) == ['the        quick']
