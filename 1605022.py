# -*- coding: utf-8 -*-
"""BitVector Demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18MOtTMOl78t08PSpHkEQBQ7rmFk9Z8l6

Install The BitVector Library
"""
#pip install BitVector


"""Tables"""
from collections import deque
from BitVector import *
import numpy as np
import time
import os

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


mixer=np.array([["02","03","01","01"],
                ["01","02","03","01"],
                ["01","01","02","03"],
                ["03","01","01","02"]])
inv_mixer=np.array([["0E","0B","0D","09"],
                ["09","0E","0B","0D"],
                ["0D","09","0E","0B"],
                ["0B","0D","09","0E"]])              


def matrix_xor(mat1,mat2):
    return_mat=np.empty((4,0),str)
    for i in range(4):
        column_list_1=[]
        for j in range(4):
            x=(hex(int(mat1[j][i],16)^int(mat2[j][i],16))[2:]).rjust(2,"0")
            column_list_1.append(x)
        return_mat = np.append(return_mat, np.array([column_list_1]).transpose(), axis=1)
    return return_mat


def matrix_sub_bytes(n,mat):
    return_mat=np.empty((4,0),str)
    for i in range(4):
        column_list_1=[]
        for j in range(4):
            b = BitVector(hexstring=mat[j][i])
            int_val = b.intValue()
            if(n==1):
                s = Sbox[int_val]
            else:
                s=InvSbox[int_val]    
            s = BitVector(intVal=s, size=8)
            x=s.get_bitvector_in_hex()
            column_list_1.append(x)

        return_mat = np.append(return_mat, np.array([column_list_1]).transpose(), axis=1)

    return return_mat




def matrix_shif_row(x,mat):
    if x==1:
        mat[0,:]=np.roll(mat[0,:],0,0)
        mat[1,:]=np.roll(mat[1,:],3,0)
        mat[2,:]=np.roll(mat[2,:],2,0)
        mat[3,:]=np.roll(mat[3,:],1,0)
    else:
        mat[0,:]=np.roll(mat[0,:],0,0)
        mat[1,:]=np.roll(mat[1,:],1,0)
        mat[2,:]=np.roll(mat[2,:],2,0)
        mat[3,:]=np.roll(mat[3,:],3,0)

    return mat    
        

def matrix_mix_columns(mat1,mat2):
    return_mat=np.empty((0,4),str)
    AES_modulus = BitVector(bitstring='100011011')
    for i in range(4):
        cell=[]
        for j in range(4):
            bv3 = BitVector(hexstring="00")
            for k in range(4):
                bv1 = BitVector(hexstring=mat1[i][k])
                bv2 = BitVector(hexstring=mat2[k][j])
                bv3=bv3.__xor__(bv1.gf_multiply_modular(bv2,AES_modulus,8))
            
            ins=(hex(int(bv3))[2:]).rjust(2,"0")
            cell.append(ins)

        return_mat = np.append(return_mat, np.array([cell]), axis=0)

    return return_mat            




    


#key generation

key=input("Enter Key:")
plaintext=input("Enter plaintext:")

if(os.path.isfile(plaintext)):
    print("ItS a file")

key_generation_start_time=time.time()


key_length=len(key)


if(key_length>16):
    key=key[0:16]

if(key_length<16):
   key=key.ljust(16,"0")




key_in_hex=("".join("{:02x}".format(ord(c)) for c in key)).rjust(32,"0")
plaintext_in_hex=("".join("{:02x}".format(ord(c)) for c in plaintext)).rjust(32,"0")

print("PlaintText in hex="+plaintext_in_hex)
print("Key in hex="+key_in_hex)

round_const = [1,0,0,0]

w=[]
w.append(key_in_hex[0:8])
w.append(key_in_hex[8:16])
w.append(key_in_hex[16:24])
w.append(key_in_hex[24:32])

input_index=3
process_index=0
for i in range(10):
    input=w[input_index]
    # print("Input="+input)
    
      
    Lfirst = input[0 :2]  
    Lsecond = input[2 :] 

    circ=Lsecond+Lfirst
    

#Thats my Kung Fu
# Two One Nine Two

    byte_sub=""
    j=0
    while True:
        x=BitVector(hexstring=circ[j:j+2])
        int_val=x.intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        s=s.get_bitvector_in_hex()
        byte_sub+=s
        j=j+2
        if(j==8):
            break

    
    g=""

    g += (hex(int(byte_sub[0:2], 16) ^ round_const[0])[2:]).rjust(2,"0")
    g += (hex(int(byte_sub[2:4], 16) ^ round_const[1])[2:]).rjust(2,"0")
    g += (hex(int(byte_sub[4:6], 16) ^ round_const[2])[2:]).rjust(2,"0")
    g += (hex(int(byte_sub[6:8], 16) ^ round_const[3])[2:]).rjust(2,"0")



    w.append((hex(int(w[input_index-3],16)^int(g,16))[2:]).rjust(8,"0"))
    w.append((hex(int(w[input_index-3+4],16)^int(w[input_index-3+1],16))[2:]).rjust(8,"0"))
    w.append((hex(int(w[input_index-3+5],16)^int(w[input_index-3+2],16))[2:]).rjust(8,"0"))
    w.append((hex(int(w[input_index-3+6],16)^int(w[input_index-3+3],16))[2:]).rjust(8,"0"))

    
    AES_modulus = BitVector(bitstring='100011011')
    round_const[0] =  BitVector(intVal=round_const[0]).gf_multiply_modular(BitVector(hexstring = "02"),AES_modulus,8).intValue()
    input_index+=4



key_generation_end_time=time.time()

#encryption

encryption_start_time=time.time()

roundKey0_matrix=np.empty((4,0),str)


for i in range(4):
    column_list_1 = [w[i][0:2],w[i][2:4] , w[i][4:6], w[i][6:8]]
    roundKey0_matrix = np.append(roundKey0_matrix, np.array([column_list_1]).transpose(), axis=1)



plaintext_matrix=np.empty((4,0),str)


for i in range(4):
    x=i*8
    temp_w=plaintext_in_hex[x:x+8]
    column_list_1 = [temp_w[0:2],temp_w[2:4] , temp_w[4:6], temp_w[6:8]]
    plaintext_matrix = np.append(plaintext_matrix, np.array([column_list_1]).transpose(), axis=1)    




state_matrix=matrix_xor(plaintext_matrix,roundKey0_matrix)




#round 1-9
for i in range(1,10):
    state_matrix=matrix_sub_bytes(1,state_matrix)
    state_matrix=matrix_shif_row(1,state_matrix)
    state_matrix=matrix_mix_columns(mixer,state_matrix)
    x=i*4
    roundKey_matrix=np.empty((4,0),str)
    for j in range(x,x+4):
        column_list_1 = [w[j][0:2],w[j][2:4] , w[j][4:6], w[j][6:8]]
        roundKey_matrix = np.append(roundKey_matrix, np.array([column_list_1]).transpose(), axis=1)

    state_matrix=matrix_xor(state_matrix,roundKey_matrix)



#for round 10

state_matrix=matrix_sub_bytes(1,state_matrix)
state_matrix=matrix_shif_row(1,state_matrix)
roundKey_matrix=np.empty((4,0),str)
for i in range(40,44):
    column_list_1 = [w[i][0:2],w[i][2:4] , w[i][4:6], w[i][6:8]]
    roundKey_matrix = np.append(roundKey_matrix, np.array([column_list_1]).transpose(), axis=1)

cipertext=matrix_xor(roundKey_matrix,state_matrix)
cipertext_in_hex=''.join(ele for sub in np.transpose(cipertext) for ele in sub)
print("\n\nCiphertext in hex="+cipertext_in_hex)
cipertext_in_ascii=''.join([chr(int(''.join(c), 16)) for c in zip(cipertext_in_hex[0::2],cipertext_in_hex[1::2])])
print("Ciphertext in ASCII="+cipertext_in_ascii)

encryption_end_time=time.time()


#decryption

decryption_start_time=time.time()
state_matrix=matrix_xor(cipertext,roundKey_matrix)

# round 1-9
for i in range(9,0,-1):
    state_matrix=matrix_shif_row(0,state_matrix)
    state_matrix=matrix_sub_bytes(0,state_matrix)
    roundKey_matrix=np.empty((4,0),str)
    x=i*4
    for j in range(x,x+4):
        column_list_1 = [w[j][0:2],w[j][2:4] , w[j][4:6], w[j][6:8]]
        roundKey_matrix = np.append(roundKey_matrix, np.array([column_list_1]).transpose(), axis=1)

    state_matrix=matrix_xor(state_matrix,roundKey_matrix)
    state_matrix=matrix_mix_columns(inv_mixer,state_matrix)


# round 10

state_matrix=matrix_shif_row(0,state_matrix)
state_matrix=matrix_sub_bytes(0,state_matrix)

roundKey_matrix=np.empty((4,0),str)
for i in range(0,4):
    column_list_1 = [w[i][0:2],w[i][2:4] , w[i][4:6], w[i][6:8]]
    roundKey_matrix = np.append(roundKey_matrix, np.array([column_list_1]).transpose(), axis=1)

decipertext=matrix_xor(roundKey_matrix,state_matrix)

decipertext_in_hex=''.join(ele for sub in np.transpose(decipertext) for ele in sub)
print("\n\nDeciphertext in hex="+decipertext_in_hex)
decipertext_in_ascii=''.join([chr(int(''.join(c), 16)) for c in zip(decipertext_in_hex[0::2],decipertext_in_hex[1::2])])
print("Deciphertext in ASCII="+decipertext_in_ascii)

decryption_end_time=time.time()

print("\n\nExecution time")
print("Key generation:"+str(key_generation_end_time-key_generation_start_time)+" seconds")
print("Encryption:"+str(encryption_end_time-encryption_start_time)+" seconds")
print("Decryption:"+str(decryption_end_time-decryption_start_time)+" seconds")

# print(decipertext)




# generating s-box

Self_Sbox=[]

AES_modulus = BitVector(bitstring='100011011')

Self_Sbox.append(hex(99))



for i in range(1,256):
    bv=BitVector(hexstring=((hex(i)[2:]).rjust(2,"0")))
    bv1=bv.gf_MI(AES_modulus, 8)
    s = (BitVector(hexstring="63")) ^ bv1 ^ (bv1<<1) ^ (bv1<<1) ^ (bv1<<1) ^ (bv1<<1)
    Self_Sbox.append(hex(int(s.get_bitvector_in_hex(), 16)))

print("\n\nSbox generation\n")
print(Self_Sbox)
print("\n\n")


# generating InvSbox

Self_InvSbox=[]

AES_modulus = BitVector(bitstring='100011011')


for i in range(256):
    if i==0x63:
        Self_InvSbox.append(0x00)
    else:    
        s = BitVector(intVal=i, size=8)
        bv = ( BitVector(intVal=5, size=8)) ^ (s<<1) ^ (s<<2) ^(s<<3)
        bv = bv.gf_MI(AES_modulus, 8)
        Self_InvSbox.append(hex(int(bv.get_bitvector_in_hex(),16)))

print("Inverse Sbox Generation")
print(Self_InvSbox)
print("\n\n")








