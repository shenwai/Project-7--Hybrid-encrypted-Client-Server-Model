import json


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)



def rsa_decr():

    # Opening JSON file
    with open('key.json', 'r') as openfile:

        # Reading from json file
        json_object = json.load(openfile)
        encrypted_msg =  (json_object['encr_aes_key'])
        public = (json_object['public_rsa_key'])
        private = (json_object['private_rsa_key'])


    ####### WRITING THE Decrypted AES KEY ########
    # Data to be written
    dictionary = {
        "decr_aes_key": decrypt(private, encrypted_msg),
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("key.json", "w") as outfile:
        outfile.write(json_object)    


