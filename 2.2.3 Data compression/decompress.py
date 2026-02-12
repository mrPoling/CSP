# Dictionary from the activity
dictionary = {
    "1": "the",
    "2": "trail",
    "3": "hikers",
    "4": "forest",
    "5": "trees",
    "6": "as",
    "7": "and",
    "8": "was",
    "9": "walked",
    "10": "along",
    "11": "narrow",
    "12": "path",
    "13": "curved",
    "14": "around",
    "15": "rocks",
    "16": "admired",
    "17": "tall",
    "18": "continued",
    "19": "grew",
    "20": "darker",
    "21": "stayed",
    "22": "close",
    "23": "together",
    "24": "but"
}

compressed_text = """
1 4 2 8 quiet 6 1 3 9 10 1 11 12.
1 2 13 gently 14 5 7 15, 7 1 3 16 1 17 5.
6 1 2 18, 1 4 19 20, 24 1 3 21 22 23 10 1 2.
"""

def decompress(text, dictionary):
    tokens = text.split() #returns list of substrings. By default, splits on spaces & other whitespace
    output_words = []
    
    for token in tokens:
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
        output_words.append(decompressed + punctuation)
    
    return " ".join(output_words)

decompressed_output = decompress(compressed_text, dictionary)
print("\n" + decompressed_output + "\n")