import aes_tools
import aes_encr


# Main AES Decryption Method
def aesDecrypt(cipher_text,key):
    key = aes_tools.text2Unicode(key)
    decrypted_text = ""
    length = len(cipher_text)
    # splitting  cipher text into substrings of length 16 each    
    cipher_text_split = []
    for i in range(length//16):
        cipher_text_split.append(cipher_text[0+16*i:16+16*i])
    
    # decrypting each substring
    for sub_string in cipher_text_split:
        cipher_text = aes_tools.text2Unicode(sub_string)
        A39 = aes_tools.removeRoundKey(cipher_text,key)
        A38= aes_tools.invMixCol(A39)
        A37 = aes_tools.invShiftRows(A38)
        A36 = aes_tools.invSubBytes(A37)
        # print("Inv round key1: " + str(A4))
        A35 = aes_tools.removeRoundKey(A36,key)
        A34 = aes_tools.invMixCol(A35)
        A33 = aes_tools.invShiftRows(A34)
        A32 = aes_tools.invSubBytes(A33)
        # print("Inv round key1: " + str(A4))
        A31 = aes_tools.removeRoundKey(A32,key)
        A30= aes_tools.invMixCol(A31)
        A29 = aes_tools.invShiftRows(A30)
        A28 = aes_tools.invSubBytes(A29)
        # print("Inv round key1: " + str(A4))
        A27 = aes_tools.removeRoundKey(A28,key)
        A26= aes_tools.invMixCol(A27)
        A25 = aes_tools.invShiftRows(A26)
        A24 = aes_tools.invSubBytes(A25)
        # print("Inv round key1: " + str(A4))
        A23 = aes_tools.removeRoundKey(A24,key)
        A22 = aes_tools.invMixCol(A23)
        A21 = aes_tools.invShiftRows(A22)
        A20 = aes_tools.invSubBytes(A21)
        # print("Inv round key1: " + str(A4))
        A19 = aes_tools.removeRoundKey(A20,key)
        A18 = aes_tools.invMixCol(A19)
        A17 = aes_tools.invShiftRows(A18)
        A16 = aes_tools.invSubBytes(A17)
        # print("Inv round key1: " + str(A4))
        A15 = aes_tools.removeRoundKey(A16,key)
        A14= aes_tools.invMixCol(A15)
        A13 = aes_tools.invShiftRows(A14)
        A12 = aes_tools.invSubBytes(A13)
        # print("Inv round key1: " + str(A4))
        A11 = aes_tools.removeRoundKey(A12,key)
        A10= aes_tools.invMixCol(A11)
        A9 = aes_tools.invShiftRows(A10)
        A8 = aes_tools.invSubBytes(A9)
        # print("Inv round key1: " + str(A4))
        A7 = aes_tools.removeRoundKey(A8,key)
        A6= aes_tools.invMixCol(A7)
        A5 = aes_tools.invShiftRows(A6)
        A4 = aes_tools.invSubBytes(A5)
        # print("Inv round key1: " + str(A4))
        A3 = aes_tools.removeRoundKey(A4,key)
        A2 = aes_tools.invMixCol(A3)
        A1 = aes_tools.invShiftRows(A2)
        A0 = aes_tools.invSubBytes(A1)
        # print("Inv round key2: " + str(A0))
        decrypted_text+=aes_tools.unicode2Text(A0)
    return decrypted_text