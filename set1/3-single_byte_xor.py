import sys

# todo - add bigrams, trigrams, quadgrams
#   have them be weighed more than monograms?

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
def score(freq_chart):
    freq_modified = "" 
    score = 0

    freq_chart_str = ""

    for char in freq:
        if char in freq_chart:
            freq_modified += char

    for x in freq_chart.keys():
        freq_chart_str += x

    #scoring by distance
    # same index => score += len(freq_string) minus absolute value
    for char in freq_chart_str:
        a = freq_chart_str.index(char)
        b = freq_modified.index(char)
        score += len(freq_chart_str) - abs(a-b)
    
    return score;

#returns dictionary sorted in descending order of values
#key = char; value = int, frequency of that char
def sort_by_freq(res):
    res = res.upper()
    d = {}

    for char in res:
        if char in d:
            d[char] += 1
        elif char in freq: # eliminating non-letters
            d[char] = 1
    
    sorted_d = {}
    sorted_keys = sorted(d, key=d.get, reverse=True)
    for w in sorted_keys:
        sorted_d[w] = d[w]

    return sorted_d

if __name__ == '__main__':
    # 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
    
    if len(sys.argv) == 1:
        print("Expecting a hex string!")
        sys.exit()

    text = sys.argv[1]
    byte_array = bytearray.fromhex(sys.argv[1])    

    most_english = ""
    most_english_char = ''
    highest_score = 0
    
    for xor_byte in range(0, 0xff):
        result = ""
        for byte in byte_array:
            res = byte ^ xor_byte   
            if (res > 31 and res < 127) or res == 9 or res == 10: # tab, newline
                result += chr(res)
            else:
                break # dont bother processing results with non-ascii characters

        if len(result) == len(byte_array):
            freq_chart = sort_by_freq(result)
            s = score(freq_chart)
            if s > highest_score:
                most_english =  result
                most_english_char = xor_byte
                highest_score = s
            # edge case - highest score is the same for two xor_chars?

    # len(text) * 2; is arbitrary
    # also - move into new function, detect_english()?
    if (highest_score > len(text) * 2):
        print(repr(most_english), end = "\t")
        print(highest_score, end="\t")
        print("original = " + text)
