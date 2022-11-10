import aes_tools
import json



# Main AES Encrtption Method
def aesEncrypt(plain_text,key):
    key = aes_tools.text2Unicode(key)
    length = len(plain_text)
    cipher_text = "" 
    
    # splitting  plain_text into substrings of length 16 each and adding whitspaces to shorter substrings    
    plain_text_split = []
    for i in range(length//16):
        plain_text_split.append(plain_text[0+16*i:16+16*i])
    if not length%16==0:        
        plain_text_split.append(plain_text[16*(length//16):])
    if len(plain_text_split[-1])<16:
        while(len(plain_text_split[-1])<16):
            plain_text_split[-1]+=' '
    


    

    # encrypting each sub string
    for sub_string in plain_text_split : 
        A0 = aes_tools.text2Unicode(sub_string)
        A1 = aes_tools.subBytes(A0)
        A2 = aes_tools.shiftRows(A1)
        A3 = aes_tools.mixCol(A2)
        A4 = aes_tools.addRoundKey(A3, key )
        # print("round key1: "+ str(A4))
        A5 = aes_tools.subBytes(A4)
        A6 = aes_tools.shiftRows(A5)
        A7 = aes_tools.mixCol(A6)
        A8 = aes_tools.addRoundKey(A7, key)
        # print("round key2: "+ str(A7))
        A9 = aes_tools.subBytes(A8)
        A10 = aes_tools.shiftRows(A9)
        A11 = aes_tools.mixCol(A10)
        A12 = aes_tools.addRoundKey(A11, key)
        # print("round key3: "+ str(A11))
        A13 = aes_tools.subBytes(A12)
        A14 = aes_tools.shiftRows(A13)
        A15 = aes_tools.mixCol(A14)
        A16 = aes_tools.addRoundKey(A15, key)
        # print("round key4: "+ str(A15))
        A17 = aes_tools.subBytes(A16)
        A18 = aes_tools.shiftRows(A17)
        A19 = aes_tools.mixCol(A18)
        A20 = aes_tools.addRoundKey(A19, key)
        # print("round key5: "+ str(A19))
        A21 = aes_tools.subBytes(A20)
        A22 = aes_tools.shiftRows(A21)
        A23 = aes_tools.mixCol(A22)
        A24 = aes_tools.addRoundKey(A23, key)
        # print("round key6: "+ str(A24))
        A25 = aes_tools.subBytes(A24)
        A26 = aes_tools.shiftRows(A25)
        A27 = aes_tools.mixCol(A26)
        A28 = aes_tools.addRoundKey(A27, key)
        # print("round key7: "+ str(A28))
        A29 = aes_tools.subBytes(A28)
        A30= aes_tools.shiftRows(A29)
        A31 = aes_tools.mixCol(A30)
        A32 = aes_tools.addRoundKey(A31, key)
        # print("round key8: "+ str(A32))
        A33 = aes_tools.subBytes(A32)
        A34 = aes_tools.shiftRows(A33)
        A35 = aes_tools.mixCol(A34)
        A36 = aes_tools.addRoundKey(A35, key)
        # print("round key9: "+ str(A36))
        A37 = aes_tools.subBytes(A36)
        A38 = aes_tools.shiftRows(A37)
        A39 = aes_tools.mixCol(A38)
        A40 = aes_tools.addRoundKey(A39, key)
        # print("round key9: "+ str(A40))
        cipher_text+=aes_tools.unicode2Text(A40)

    return cipher_text
    


