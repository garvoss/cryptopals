import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("{} <filename> <key>".format(sys.argv[0]))
        print("This program takes a filename, and xor's the contents " +
            "with the key repeatedly.")
        sys.exit()

    filename = sys.argv[1]

    text = '' 
    with open(filename, 'r') as f:
        text = f.read()

    # strip any new lines at the end
    if text.endswith("\n"):
        text = text[:-1]

    text_byte_array = bytearray(text, "ascii")

    print(text_byte_array)

    # look at this mess of code!
    # expanding key to fit size of text
    # the +1 is there because integer division truncates
    # then slice down to size of text via [0:len(text...)]
    key_byte_array = (bytearray(sys.argv[2], "ascii") * 
    (int(len(text_byte_array) / len(sys.argv[2]))+ 1))[0:len(text_byte_array)]

    res = ""

    for i in range(len(text_byte_array)):
        # dropping the '0x' with [2:], adding in leading 0's with zfill
        res += str(hex(text_byte_array[i] ^ key_byte_array[i]))[2:].zfill(2) 

    print(res) 
