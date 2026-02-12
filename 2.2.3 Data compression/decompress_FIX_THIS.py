
'''
Original text:
'''
original = "row row row your boat, gently down the stream, merrily merrily merrily merrily life is but a dream"

#TODO: Print length of original text
print("original length: " + ?)


#TODO: Fill out the rest of this dictionary based on original text, above.
# ** most frequent words should come first **
# do NOT include spaces or punctuation
dictionary = {
    "1": "merrily",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "dream"
}

#TODO: Fill out the rest of this compressed_text string with numbers and values, based on the dictionary
# Punctuation should just written directly. Also spaces.
compressed_text = """
2 2 2 
"""
#TODO: Print length of compressed text
print("compressed length: " + ?)

def decompress(text, dictionary):
    tokens = text.split() #returns list of substrings. By default, splits on spaces & other whitespace
    output_words = []
    
    #TODO Complete the for loop in line 53, which should iterate over the tokens list just created
    for ? in ?
        word = token
        punctuation = ""
        
        # If the token ends with punctuation, separate it
        if not token[-1].isalnum():
            word = token[:-1]
            punctuation = token[-1]
        
        # Replace numeric codes with dictionary words
        if word in dictionary:
            decompressed = dictionary[word]
        else:
            decompressed = word
        
        # Reattach any punctuation
        #TODO: Add the *end* of the output variable the decompressed word plus any punctuation:
        output_words.?
    
    return " ".join(output_words)

#TODO: Assign to the following variable the result of calling the decompress function with the appropriate variables 
decompressed_output = ?

print("\n" + decompressed_output + "\n")
