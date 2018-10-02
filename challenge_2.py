def decode(string):
    s = bytearray.fromhex(string).decode()
    return s


def encode(string):
    s = string.encode()
    s = s.hex()
    return s


def XOR(a,b):
    if len(a) != len(b):
        return ('Strings aren\'t the same length')


    result1 = decode(a)
    result2 = decode(b)


    solution = ''

    for x,y in zip(result1,result2):
        solution += chr(ord(x) ^ ord(y))


    return encode(solution)

def main():
    string = '1c0111001f010100061a024b53535009181c'
    string2 = '686974207468652062756c6c277320657965'
    string3 = '746865206b696420646f6e277420706c6179'

    r = XOR(string, string2)
    # print(r)

    try:
        assert(r == string3)
        print('Success')
    except:
        print('Error')

if __name__== "__main__":
  main()
