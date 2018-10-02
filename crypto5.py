
# Taken from crypto3
def XOR(a, b):
    solution = ''

    for i in range(0, len(a)):
        solution += chr(ord(a[i]) ^ ord(b[i%len(b)]))

    return solution



def main():
    string1 = """Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""
    string2 = 'ICE'
    string3 = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'


    solution = XOR(string1, string2)


    solution = solution.encode('utf-8')
    solution = solution.hex()


    try:
        assert(solution == string3)
        print('Success')
    except:
        print('Error')


if __name__== "__main__":
  main()
