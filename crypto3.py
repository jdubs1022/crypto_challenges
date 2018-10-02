# Assigns a score to the possible XOR's answer
def score(possible):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    score = 0
    for char in possible:
        if char in charset or char == ' ' or char == '\'':
            score += 1

    return score

# Decode function taken from crypto2.py
def decode(string):
    s = bytearray.fromhex(string).decode()
    return s

# XOR function taken from crypto2.py and modified
def XOR(a, b):
    solution = ''

    for i in range(0, len(a)):
        solution += chr(ord(a[i]) ^ ord(b[i%len(b)]))

    return solution



def main():
    answer = ''
    current_max = 0
    string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    #string = 'IConIT0xdSoldit1GTJ2GTIudRkxdigidTQgMyoZMXY0KiIZdiAZJTQ/NjJ2Zzs='
    result = decode(string)


    # Loops through the ASCII table starting with the space char, trying them all
    for i in range(32, 127):
        possible = XOR(result, chr(i))

        # Finds the max score assigned and makes it the answer
        if score(possible) > current_max:
            current_max = score(possible)
            answer = possible

    print(answer)

if __name__ == "__main__":
	main()
