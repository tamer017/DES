from tables import *

def encrypt(binary_plain_text, key):
    # key generation 
    keys = key_generation(key)
    # intial permutation
    permuted_text = permutation(binary_plain_text,ip)
    # encryption function
    encrypted_text = round_function(permuted_text, keys)
    # Swap left and right
    swapped_text = swap_left_and_right(encrypted_text)
    # inverse permutation
    cipher_text = permutation(swapped_text,ip_inv)
    # result 
    return cipher_text

def decrypt(binary_cipher_text, key):
    # key generation 
    keys = key_generation(key)
    # reverse the order of the keys
    keys.reverse()
    # intial permutation
    permuted_text = permutation(binary_cipher_text,ip)
    # encryption function
    encrypted_text = round_function(permuted_text, keys)
    # Swap left and right
    swapped_text = swap_left_and_right(encrypted_text)
    # inverse permutation
    plain_text = permutation(swapped_text,ip_inv)
    # result 
    return plain_text

def permutation(input,permutation):
    length = len(permutation)
    output = ""
    for i in range(length):
        output += input[permutation[i]-1]
    return output

def swap_left_and_right(input):
    return input[32:] + input[:32]

def rotate_left(key, n_bits):
    return key[n_bits:] + key[:n_bits]

def key_generation(key):
    # Key permutation
    key = permutation(key, key_permutation)
    C, D = key[:28], key[28:]
    rounds_keys = []
    for round in range(1,17):
        # Rotate left
        if round in [1,2,9,16]:
            C, D = rotate_left(C, 1), rotate_left(D, 1)
        else:
            C, D = rotate_left(C, 2), rotate_left(D, 2)
        # Combine the two halfs and choose key bits
        round_key = permutation(C + D,key_choice)
        # Add the round key to keys list
        rounds_keys.append(round_key)
    return rounds_keys
    
def xor(A, B):
    out = ""
    for a,b in zip(A,B):
        if a == b:
            out += "0"
        else:
            out += "1"
    return out
    
def S_Box(Bs):
    Ss = []
    for index, B in enumerate(Bs):
        s = s_box[index][int(B[0] + B[5], 2)][int(B[1 : 5], 2)]
        s = str(bin(s))[2:]
        if len(s) == 1:
            Ss.append("000" + s)
        elif len(s) == 2:
            Ss.append("00" + s)
        elif len(s) == 3:
            Ss.append("0" + s)
        else:
            Ss.append(s)
    return Ss
    
def round_function(text,keys):
    for round in range(16):
        L, R = text[:32], text[32:]
        R_new = f_function(R, keys[round])
        R_new = xor(R_new, L)
        text = R + R_new
    return text

def f_function(Rn, keyn):
    # Rn is expanded into 48 bits 
    Rn = permutation(Rn, expansion_table)
    # The expanded Rn is XOR’ed with Kn 
    result = xor(Rn,keyn)
    # The result of the XOR operation is split into 8 blocks, each one is 6-bits long
    B1, B2, B3, B4, B5, B6, B7, B8 = result[:6], result[6:12], result[12:18], result[18:24], result[24:30], result[30:36], result[36:42], result[42:]
    # Use S_box table to find S1, S2, S3, S4, S5, S6, S7, S8
    [S1, S2, S3, S4, S5, S6, S7, S8] = S_Box([B1, B2, B3, B4, B5, B6, B7, B8])
    # Combine all S's
    combined_s = S1 + S2 + S3 + S4 + S5 + S6 + S7 + S8
    # F permutation
    return permutation(combined_s, f_permutation)



