codes = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(',
         'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '`', 'P': '~', 'Q': '{', 'R': '[', 'S': '}',
         'T': ']', 'U': ':', 'V': ';', 'W': '"', 'X': '<', 'Y': '>', 'Z': '0', 'a': '1', 'b': '2', 'c': '3',
         'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': 'a', 'k': 'b', 'l': 'c', 'm': 'd',
         'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i', 's': 'j', 't': 'k', 'u': 'l', 'v': 'm', 'w': 'n',
         'x': 'o', 'y': 'p', 'z': 'q', '.': '*', ' ': ' ', ':': ':'}

outfile = open(
    r'C:\Users\zobia\Desktop\MIS 4322 01 Advanced Python\DICTIONARIES HW\PythonRecap\info_security.txt', 'r')

read_outfile = outfile.read()

#outfile = outfile.rstrip('\n')


outfile.close()

encryption_file = open('encryption_file.txt', 'w')


for letter in read_outfile:
    # if letter in codes:
    encryption_file.write(codes[letter])

encryption_file.close()
