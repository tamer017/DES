import base64
import binascii
from tables import *

'''
    Convert the binary text in to utf-8.
    parameters:
        binary_text: binary text to convert in to utf-8.
    output:
        utf-8 text.
'''
def binary_to_utf8(binary_text):
    utf8_output = ""
    for i in range(0, len(binary_text), 8):
        utf8_output += chr(int(binary_text[i:i+8], 2))
    return utf8_output

'''
    Convert the binary text in to base64.
    parameters:
        binary_text: binary text to convert in to base64.
    output:
        base64 text.
'''

def binary_to_base64(binary_text):
    HEX_STRING = binary_to_hexa(binary_text)
    BYTE_ARRAY = bytearray.fromhex(HEX_STRING)
    BASE64_VAL = base64.b64encode(BYTE_ARRAY)
    return str(BASE64_VAL)[2:-1]

'''
    Convert the base64  text in to binary.
    parameters:
        base64_text: base64 text to convert in to binary.
    output:
        binary text.
'''
def base64_to_binary(base64_text):
    BYTE_ARRAY = base64.b64decode(base64_text)
    HEX_STRING = str((binascii.hexlify(BYTE_ARRAY)))[2:-1].upper()
    return hexa_to_binary(HEX_STRING)

'''
    Convert the utf-8 text in to binary.
    parameters:
        utf8_text: utf-8 text to convert in to binary.
    ouput: 
        binary text.
'''
def utf8_to_binary(utf8_text):
    return ("".join(f"{ord(i):08b}" for i in utf8_text))

'''
    Convert the hexa text in to binary.
    parameters:
        hexa_text: hexa text to convert in to binary.
    output: 
        binary text.
'''
def hexa_to_binary(hexa_text):
    binary = ""
    for char in hexa_text:
        if hexa_map.__contains__(char):
            binary += hexa_map[char]
    return binary

'''
    Convert the binary text in to hexa.
    parameters:
        binary_text: binary text to convert in to hexa.
    output:
        hexa text.
'''
def binary_to_hexa(binary_text):
    hexa = ""
    for index in range(len(binary_text) // 4):
        hexa += binary_map[binary_text[4 * index : (index + 1) * 4]]
    return hexa