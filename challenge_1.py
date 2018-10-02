import base64

def Hextob64(hex):
    b64 = base64.b64encode(hex)
    return b64

# makes a string to bytes
def StringToHex(string):
    hex = bytes.fromhex(string)
    return hex


def main():
    string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    string2 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    decoded = base64.b64decode(string2)

    result = StringToHex(string)
    
    result1 = Hextob64(result)
    result2 = Hextob64(decoded)


    try:
        assert(result1 == result2)
        print('Success')
    except:
        print('Error')

if __name__== "__main__":
  main()
