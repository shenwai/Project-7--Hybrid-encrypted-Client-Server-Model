import aes_encr
import aes_decr
import aes_tools
import rsa_main_encr
import rsa_main_decr
import json

# driver code :
def encrypter(plain_text):

    cipher_key = '1234567890123456'
    # print("Encrypting the string using AES: ")    
    cipher_text = aes_encr.aesEncrypt(plain_text,cipher_key)
    print("The encrpyted text is : {}".format(cipher_text))
    print(" ")

    ##    sending the AES key to RSA  ############################
     
    # Data to be written
    dictionary = {
        "aes_key": cipher_key,
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("key.json", "w") as outfile:
        outfile.write(json_object)    

    rsa_main_encr.rsa_encr_main()

    rsa_main_decr.rsa_decr()


    # Data to be written
    dictionary = {
        "ENCR_MSG": cipher_text,
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("encr_msg.json", "w") as outfile:
        outfile.write(json_object) 

    return cipher_text




def decrypter(cipher_text):
    # Opening JSON file
    with open('key.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        processed_cipher_key = str(json_object['decr_aes_key'])
    

    # print("Decrypting : ")
    decrypted_text = aes_decr.aesDecrypt(cipher_text,processed_cipher_key)
    print("The decrpyted text is : {}".format(decrypted_text))

    return decrypted_text