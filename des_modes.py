from tables import *
from des import *
import des as DES
from convertions import *

def padding(encoded_text,padding_type):
    padded_bytes = 8 - (len(encoded_text) % 64) // 8
    if padded_bytes == 8:
        return encoded_text + (f"{8:064b}" if padding_type != "symmetric" else f"{8:08b}" * padded_bytes) 
    return encoded_text + (f"{padded_bytes:0{padded_bytes*8}b}" if padding_type != "symmetric" else f"{padded_bytes:08b}" * padded_bytes)

''''
    Encrypt the whole plain text using DES.
    parameters:
        input_text: input plain text in case of encryption ad cipher text in case of decryption.
        key: encryption key in hexa.
        iv: intialization verctor in hexa.
        input_type: the type of the plain text. ex hexa, base64 and utf-8.
        output_type: the type of the output cipher text. ex hexa and base64.
        padding_type: the padding method used when the plain text is not multiple of 64bits. ex symmetric or zeros.
        mode: the mode of opertaion. ex CBC or ECB.
        encryption: True for encryption and False for decryption.
    output:
        cipher text in case of encryption and plain text in case of decryption.

'''
def Des(input_text, key, iv = "", input_type = "hexa", output_type = "hexa", padding_type = "symmetric", mode = "ECB", encryption = True): 
    # convert the input_text into binary depending on the input_type
    if input_type == "hexa":
        binary_input_text = hexa_to_binary(input_text)
    if input_type == "utf-8":
        binary_input_text = utf8_to_binary(input_text) 
    if input_type == "base64":
        binary_input_text = base64_to_binary(input_text)
    # convert the key in to binary
    key = hexa_to_binary(key)
    # convert the iv in to binary
    iv = hexa_to_binary(iv)
    # pad the binary plain text in case of encryption
    if encryption:  
        padded_text = padding(binary_input_text, padding_type)
        # encrypt the plain text depending on the mode of operation
    else:
        padded_text = binary_input_text
    output_text = ECB(padded_text, key, encryption) if mode == "ECB" else CBC(padded_text, key, iv, encryption)
    # remove padded_text in case of decryption
    if not encryption:
        output_text = output_text[:-int(output_text[-8:],2)*8]
    # convert the binary output_text into the output_type needed.
    if output_type == "hexa":
        return binary_to_hexa(output_text)
    if output_type == "base64":
        return binary_to_base64(output_text)
    if output_type == "utf-8":
        return binary_to_utf8(output_text)

def CBC(padded_text, key, iv, encryption):
    output_text = ""
    block_size = 64
    for block_index in range(len(padded_text) // block_size):
        text_block = padded_text[block_index * block_size : (block_index + 1) * block_size]
        if encryption:
            xor_output = xor(text_block, iv) if block_index == 0 else xor(text_block, cipher_block)
            cipher_block = DES.encrypt(xor_output, key)
            output_text += cipher_block
        else:
            decryprted_text = DES.decrypt(text_block, key)
            xor_output = xor(decryprted_text, iv) if block_index == 0 else xor(prev_text_block, decryprted_text)
            prev_text_block = text_block
            output_text += xor_output
    return output_text


def ECB(padded_text, key, encryption):
    output_text = ""
    block_size = 64
    for block_index in range(len(padded_text) // block_size):
        text_block = padded_text[block_index * block_size : (block_index + 1) * block_size]
        output_text += DES.encrypt(text_block, key) if encryption else DES.decrypt(text_block, key) 
    return output_text

