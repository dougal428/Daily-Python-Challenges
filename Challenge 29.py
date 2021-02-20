#Question 29

#This problem was asked by Amazon.

#Run-length encoding is a fast and simple method of encoding strings. 
#The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string “AAAABBBCCDAA” would be encoded as “4A3B2C1D2A”.

#Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely,
# of alphabetic characters. You can assume the string to be decoded is valid.

#Answer 29

#create function to encdoe
def encode_string(s):
    
    #empty list of encoded chars
    encoded_chars = list()

    #set up a count
    count = 0
    #set prev char to none
    prev_char = None
    
    #loop through string
    for char in s:
        #add one to count for char if prev or a new one
        if char == prev_char or not prev_char:
            count += 1
        #else apprend string of count and previosu cahr to encode chars, and rset count to 1 to contue adding
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(prev_char)
            count = 1
        prev_char = char

    #if count append
    if count:
        encoded_chars.append(str(count))
        encoded_chars.append(prev_char)
        
    #return joined string
    return "".join(encoded_chars)

#decode function
def decode_string(s):

    #decode chars empty list
    decoded_chars = list()
    #set index to 0
    index = 0

    #while index psotion less then strign
    while index < len(s):
        #take number and times it to letter and then add that yo decoded chars list
        decoded_chars.append(int(s[index]) * s[index + 1])
        #move two along encoded string to next number and letter
        index += 2
        
    #return decoded string
    return "".join(decoded_chars)


encode_string("AAABB") 
assert encode_string("AAAABBBCCDAA") == "4A3B2C1D2A"
encode_string("AAABB")
