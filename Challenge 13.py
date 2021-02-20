#This problem was asked by Amazon.

#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

#For example, given s = “abcba” and k = 2, the longest substring with k distinct characters is “bcb”.


#create function with variable string, and number of distinct charachters
def get_longest_sub_with_k_dist(s, k):
    #if false return empty
    if not s:
        return ""
    #if length string less or equal to number of distinct charchaters return the string
    elif len(s) <= k:
        return s
    # if  one distinct charchter return first charchter of string
    elif k == 1:
        return s[0]
    
    #set counter for distict charchters and add to the seen chars sets
    distinct_char_count = 0
    seen_chars = set()
    # set candidate string to none, and remaing string to none
    candidate = None
    remaining_string = None

    # to keep track of where the second character occurred
    first_char = s[0]
    second_char_index = 0
    while s[second_char_index] == first_char:
        second_char_index += 1
        
    #assess the charchters in string which are distinct, and add to counter for distinct chars if so
    candidate = s
    for index, char in enumerate(s):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char_count += 1
            
        #if the distinct char count greater than k variable,  make new candadate string and remaing string
        #for each index in loop
        if distinct_char_count > k:
            candidate = s[:index]
            remaining_string = s[second_char_index:]
            break
            
    # put remaining string in fucntion         
    longest_remaining = get_longest_sub_with_k_dist(remaining_string, k)
    
    #set longest substring to none and asess wether candidate or longest remaing string is longer and then return
    longest_substring = None
    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring


assert get_longest_sub_with_k_dist("abcba", 2) == "bcb"
assert get_longest_sub_with_k_dist("abccbba", 2) == "bccbb"
assert get_longest_sub_with_k_dist("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_sub_with_k_dist("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_sub_with_k_dist("abccbba", 3) == "abccbba"
