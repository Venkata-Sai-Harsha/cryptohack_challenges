import base64
hex="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
data = bytes.fromhex(hex)
flag=base64.b64encode(data)
print(flag)

#b'crypto/Base+64+Encoding+is+Web+Safe/'
#b'crypto{Base+64_Encoding_is_Web_Safe}'
