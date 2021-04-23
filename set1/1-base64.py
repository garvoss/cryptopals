import sys

chart = {
0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J',
10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T',
20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z', 26:'a', 27:'b', 28:'c', 29:'d',
30:'e', 31:'f', 32:'g', 33:'h', 34:'i', 35:'j', 36:'k', 37:'l', 38:'m', 39:'n',
40:'o', 41:'p', 42:'q', 43:'r', 44:'s', 45:'t', 46:'u', 47:'v', 48:'w', 49:'x',
50:'y', 51:'z', 52:'0', 53:'1', 54:'2', 55:'3', 56:'4', 57:'5', 58:'6', 59:'7',
60:'8', 61:'9', 62:'+', 63:'/'}
# padding =

# base64 converts 3x8bits into 4x6bits; the 6 bits are encoded via the chart above
# and padded if necessary

def ascii_to_base64(text):
    
    res = ""

    # convert from hex to binary 
    binary_str = bin(int(text, base=16))[2:] # remove leading 0b

    # add back leading zeroes
    binary_str = "0" * (len(text) * 4 - len(binary_str)) + binary_str
    
    # so the padding is done in 2 steps - fill out the binary string to be divisible by 6
    # and then add ='s so that it is % 24 
    while len(binary_str) % 6 != 0:
        binary_str = binary_str + "00"
        #padding += 1

    # converts 24 bits into 4 groups of 6 bits
    for bit_section in range(0, len(binary_str), 24):
        for bit in range(0, 24, 6):
            if bit_section + bit >= len(binary_str):
                res += '='
            else:
                res += chart[int(binary_str[bit_section + bit:bit_section + bit + 6], base=2)]
    
    return res

if __name__ == '__main__':
    # text = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    text = sys.argv[1] 
    if len(text) % 2 != 0:
        print("Not a hex string - improper length")
    else:
        print(ascii_to_base64(text))
