from Crypto.Cipher import AES
from base64 import b64decode

textString = []
fhand = open('crypto7.txt')
for line in fhand:
    line = line.rstrip()
    textString.append(line)


textString = ''.join(textString)
textString = b64decode(textString)

key = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)
answer = key.decrypt(textString)
answer = answer.decode()
print(answer)
