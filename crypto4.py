# Assigns a score to the possible XOR's answer
def score(possible):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    score = 0
    for char in possible:
        if char in charset or char == ' ' or char == '\'':
            score += 1

    return score

# Decode function taken from crypto3.py and modified to ignore non utf-8 chars
def decode(string):
    s = bytearray.fromhex(string).decode('utf-8', 'ignore')

    return s

# XOR function taken from crypto2.py and modified
def XOR(a, b):
    solution = ''

    for i in range(0, len(a)):
        solution += chr(ord(a[i]) ^ ord(b[i%len(b)]))

    return solution



def main():
    answer = ''
    b = 0
    fhand = open('crypto4.txt')

    for line in fhand:
        line = line.rstrip()
        result = decode(line)

        # Loops through the ASCII table starting with the space char, trying them all
        for i in range(32, 127):
            possible = XOR(result, chr(i))

            # Finds the max score assigned and makes it the answer
            if score(possible) > b:
                b = score(possible)
                answer = possible


    print(answer)

if __name__ == "__main__":
	main()
