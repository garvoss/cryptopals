import sys

if __name__ == '__main__':
    
    if len(sys.argv[1]) != len(sys.argv[2]):
        print("Error: The two strings are not equal length")
        sys.exit()

    # convert arguments from hex string to int (base 2)
    binary1 = int(sys.argv[1], base=16) # remove leading 0b 
    binary2 = int(sys.argv[2], base=16) 

    result = 0
    mask = 1
    while (mask < binary2 or mask < binary1):
        result += (binary1 & mask) ^ (binary2 & mask)
        mask = mask << 1

    print(hex(result))
